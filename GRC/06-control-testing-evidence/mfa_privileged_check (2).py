"""
MFA check for privileged accounts — VindobonaPay GmbH
=====================================================

Control tested : A.8.2 / A.8.5 — privileged accounts must authenticate with a
                 phishing-resistant MFA method
                 (see Deliverable 02, Statement of Applicability)
Related risk   : R-02 — compromise of a privileged account
                 (see Deliverable 01, Risk Register)
Test reference : CT-01 (Deliverable 06, control test plan)

What this script does
---------------------
1. Reads the list of privileged accounts (the population to test).
2. Reads the MFA enrollment report exported from the identity provider.
3. Compares the two and decides, for each account, PASS or EXCEPTION.
4. Prints a short report and writes two CSV files: full results and
   exceptions only.

What this script does NOT do
----------------------------
It automates the comparison step of an evidence-based test. It does not test
the control itself, does not confirm that a privileged account belongs to an
authorised person, and does not perform the audit. The tester remains
responsible for validating the input data, investigating exceptions and
reaching the final conclusion.

Usage
-----
    python mfa_privileged_check.py

The two input CSV files are expected in the same folder as this script.
You can also point to different files:

    python mfa_privileged_check.py --accounts privileged_accounts.csv \
                                   --mfa mfa_enrollment.csv \
                                   --outdir output

Note: this is a didactic exercise. All accounts and enrollment data are
fictional and were written for this exercise. They do not come from a real
Microsoft 365 or Entra ID tenant.
"""

import argparse
import csv
import os
import sys
from collections import defaultdict
from datetime import date

# ---------------------------------------------------------------------------
# What counts as a strong method
# ---------------------------------------------------------------------------
# Strong = phishing-resistant. A FIDO2 security key and certificate-based
# authentication are bound to the origin, so a fake login page cannot replay
# them.
STRONG_METHODS = {"fido2_key", "certificate", "windows_hello"}

# Weak = a valid second factor, but replayable by an attacker who controls a
# phishing page or the phone number. Accepted for standard users in this
# scenario, NOT accepted for privileged access.
WEAK_METHODS = {"authenticator_app", "totp", "sms", "voice_call", "email"}

# Accounts in the privileged list that are not active are excluded from the
# population, with the reason recorded.
ACTIVE_STATUSES = {"enabled", "active"}

ACCOUNT_COLUMNS = {"account"}
MFA_COLUMNS = {"account", "mfa_enabled", "method"}


def read_csv(path, required_columns, label):
    """Read a CSV file and return a list of dictionaries (one per row).

    Fails early with a clear message if the file or a required column is
    missing: a silent KeyError halfway through a test is worse than a stop.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"{label} file not found: {path}")

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = set(reader.fieldnames or [])

    missing = required_columns - headers
    if missing:
        raise ValueError(
            f"{label} file {path} is missing required column(s): "
            f"{', '.join(sorted(missing))}"
        )
    if not rows:
        raise ValueError(f"{label} file {path} contains no data rows")
    return rows


def normalise(value):
    """Lowercase and strip a field so comparisons are not broken by casing."""
    return (value or "").strip().lower()


def build_mfa_lookup(mfa_rows):
    """Turn the MFA export into account -> list of registered methods.

    An account can appear more than once: identity exports often contain one
    row per registered method, and duplicated rows are a common export
    artifact. Collecting them in a list keeps every registration visible.
    """
    lookup = defaultdict(list)
    for row in mfa_rows:
        lookup[normalise(row.get("account"))].append(row)
    return lookup


def split_population(account_rows):
    """Separate active privileged accounts from inactive ones.

    Disabled accounts stay out of the tested population, but the exclusion is
    recorded so the population figure can be reconciled with the source file.
    """
    active, excluded = [], []
    seen = set()
    for row in account_rows:
        account = normalise(row.get("account"))
        if not account:
            continue
        if account in seen:
            excluded.append((row, "Duplicate row in the privileged account list"))
            continue
        seen.add(account)
        status = normalise(row.get("status")) or "enabled"
        if status in ACTIVE_STATUSES:
            active.append(row)
        else:
            excluded.append((row, f"Account status is '{status}', not active"))
    return active, excluded


def evaluate_account(account_row, mfa_lookup):
    """Decide whether one privileged account passes the control.

    The reason is returned with the result, so that it becomes part of the
    evidence and not only of the analyst's memory.
    """
    account = normalise(account_row.get("account"))
    registrations = mfa_lookup.get(account, [])

    methods = sorted({
        normalise(r.get("method"))
        for r in registrations
        if normalise(r.get("mfa_enabled")) == "yes"
        and normalise(r.get("method")) not in ("", "none")
    })
    strong = [m for m in methods if m in STRONG_METHODS]
    weak = [m for m in methods if m in WEAK_METHODS]
    unknown = [m for m in methods if m not in STRONG_METHODS | WEAK_METHODS]

    if not registrations:
        result = "EXCEPTION"
        reason = "Account not found in the MFA enrollment report"
    elif not methods:
        result = "EXCEPTION"
        reason = "MFA not enabled"
    elif unknown:
        result = "EXCEPTION"
        reason = f"Unrecognised MFA method, manual review required: {', '.join(unknown)}"
    elif not strong:
        result = "EXCEPTION"
        reason = f"MFA method is not phishing-resistant: {', '.join(weak)}"
    elif weak:
        # A phishing-resistant method is registered, but a weaker one is still
        # available as a fallback and can be targeted instead.
        result = "EXCEPTION"
        reason = (f"Phishing-resistant method present ({', '.join(strong)}), "
                  f"but a weak fallback is also registered: {', '.join(weak)}")
    else:
        result = "PASS"
        reason = f"Phishing-resistant MFA registered ({', '.join(strong)})"

    return {
        "account": account_row.get("account", ""),
        "owner": account_row.get("owner", ""),
        "department": account_row.get("department", ""),
        "account_type": account_row.get("account_type", ""),
        "registrations_found": len(registrations),
        "methods": ", ".join(methods) if methods else "none",
        "result": result,
        "reason": reason,
    }


def find_duplicate_registrations(mfa_lookup, tested_accounts):
    """Report accounts with more than one row in the MFA export.

    Not an exception on its own: it is a data-quality note for the tester.
    """
    duplicates = []
    for account in tested_accounts:
        rows = mfa_lookup.get(account, [])
        if len(rows) > 1:
            methods = sorted({normalise(r.get("method")) for r in rows})
            duplicates.append((account, len(rows), ", ".join(methods)))
    return duplicates


def write_csv(path, rows, fieldnames):
    """Write rows to a CSV file, creating the output folder if needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_report(results, exceptions, excluded, duplicates, source_rows):
    """Print a short summary in the terminal."""
    total = len(results)
    passed = total - len(exceptions)
    rate = (passed / total * 100) if total else 0

    print("=" * 68)
    print("MFA CHECK — PRIVILEGED ACCOUNTS")
    print("VindobonaPay GmbH — control A.8.2 / A.8.5 — test CT-01")
    print(f"Test date: {date.today().isoformat()}")
    print("=" * 68)
    print(f"Rows in privileged account list : {source_rows}")
    print(f"Excluded from population        : {len(excluded)}")
    print(f"Accounts tested                 : {total}")
    print(f"PASS                            : {passed}")
    print(f"EXCEPTION                       : {len(exceptions)}")
    print(f"Compliance rate                 : {rate:.1f}%")

    if excluded:
        print("-" * 68)
        print("EXCLUDED FROM POPULATION")
        for row, reason in excluded:
            print(f"  - {row.get('account', ''):<20} {reason}")

    if duplicates:
        print("-" * 68)
        print("DATA QUALITY NOTES (not exceptions)")
        for account, count, methods in duplicates:
            print(f"  - {account:<20} {count} rows in the MFA export ({methods})")

    if exceptions:
        print("-" * 68)
        print("EXCEPTIONS")
        for e in exceptions:
            print(f"  - {e['account']:<20} {e['reason']}")

    print("-" * 68)
    if exceptions:
        conclusion = ("Control operating with exceptions. Each exception must be "
                      "remediated by the control owner or formally retained by "
                      "management with an approver and a review date.")
    else:
        conclusion = "No exceptions identified in the tested population."
    print(f"Conclusion: {conclusion}")
    print("The tester validates the input data and reaches the final conclusion;")
    print("this script automates the comparison step only.")
    print("=" * 68)


def main():
    parser = argparse.ArgumentParser(
        description="Check MFA enrollment for privileged accounts.")
    parser.add_argument("--accounts", default="privileged_accounts.csv",
                        help="CSV with the list of privileged accounts")
    parser.add_argument("--mfa", default="mfa_enrollment.csv",
                        help="CSV with the MFA enrollment export")
    parser.add_argument("--outdir", default="output",
                        help="Folder where the result files are written")
    args = parser.parse_args()

    try:
        account_rows = read_csv(args.accounts, ACCOUNT_COLUMNS, "Privileged accounts")
        mfa_rows = read_csv(args.mfa, MFA_COLUMNS, "MFA enrollment")
    except (FileNotFoundError, ValueError) as error:
        print(f"ERROR: {error}")
        return 2

    active, excluded = split_population(account_rows)
    mfa_lookup = build_mfa_lookup(mfa_rows)

    results = [evaluate_account(row, mfa_lookup) for row in active]
    exceptions = [r for r in results if r["result"] == "EXCEPTION"]
    duplicates = find_duplicate_registrations(
        mfa_lookup, [normalise(r.get("account")) for r in active])

    fields = ["account", "owner", "department", "account_type",
              "registrations_found", "methods", "result", "reason"]
    results_path = os.path.join(args.outdir, "mfa_check_results.csv")
    exceptions_path = os.path.join(args.outdir, "mfa_exceptions.csv")
    write_csv(results_path, results, fields)
    write_csv(exceptions_path, exceptions, fields)

    print_report(results, exceptions, excluded, duplicates, len(account_rows))
    print(f"Results written to    : {results_path}")
    print(f"Exceptions written to : {exceptions_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

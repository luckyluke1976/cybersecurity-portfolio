"""
MFA check for privileged accounts — VindobonaPay GmbH
=====================================================

Control tested : A.8.2 / A.8.5 — privileged accounts must use multi-factor
                 authentication (see Deliverable 01, Statement of Applicability)
Related risk   : R-02 — compromise of a privileged account (Deliverable 02)
Test reference : CT-01 (Deliverable 06, control test plan)

What this script does
---------------------
1. Reads the list of privileged accounts (the population to test).
2. Reads the MFA enrollment report exported from the identity provider.
3. Compares the two and decides, for each account, PASS or EXCEPTION.
4. Prints a short report and writes two CSV files: full results and
   exceptions only.

Why this is useful
------------------
Testing this control by hand means opening two exports and comparing them
line by line, every quarter. The script does the comparison in a repeatable
way, so the test can be re-run at any time and always produces the same
evidence.

Usage
-----
    python mfa_privileged_check.py

The two input CSV files are expected in the same folder as this script.
You can also point to different files:

    python mfa_privileged_check.py --accounts privileged_accounts.csv \
                                   --mfa mfa_enrollment.csv \
                                   --outdir output

Note: this is a didactic exercise on fictional data.
"""

import argparse
import csv
import os
from datetime import date

# Methods that we accept as valid MFA for a privileged account.
# "sms" is deliberately not in this list: it is considered weak.
ACCEPTED_METHODS = {"authenticator_app", "fido2_key", "certificate"}


def read_csv(path):
    """Read a CSV file and return a list of dictionaries (one per row)."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_mfa_lookup(mfa_rows):
    """Turn the MFA export into a dictionary: account -> row.

    A dictionary makes the comparison fast and avoids nested loops.
    """
    return {row["account"].strip().lower(): row for row in mfa_rows}


def evaluate_account(account_row, mfa_lookup):
    """Decide whether one privileged account passes the control.

    Returns a dictionary with the result and the reason, so that the reason
    is part of the evidence and not only of the analyst's memory.
    """
    account = account_row["account"].strip().lower()
    mfa_row = mfa_lookup.get(account)

    if mfa_row is None:
        result, reason = "EXCEPTION", "Account not found in the MFA enrollment report"
    elif mfa_row["mfa_enabled"].strip().lower() != "yes":
        result, reason = "EXCEPTION", "MFA not enabled"
    elif mfa_row["method"].strip().lower() not in ACCEPTED_METHODS:
        result, reason = "EXCEPTION", f"Weak MFA method: {mfa_row['method']}"
    else:
        result, reason = "PASS", f"MFA enabled ({mfa_row['method']})"

    return {
        "account": account_row["account"],
        "owner": account_row.get("owner", ""),
        "department": account_row.get("department", ""),
        "account_type": account_row.get("account_type", ""),
        "mfa_enabled": mfa_row["mfa_enabled"] if mfa_row else "not found",
        "method": mfa_row["method"] if mfa_row else "not found",
        "result": result,
        "reason": reason,
    }


def write_csv(path, rows, fieldnames):
    """Write rows to a CSV file, creating the folder if needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_report(results, exceptions):
    """Print a short summary in the terminal."""
    total = len(results)
    passed = total - len(exceptions)
    rate = (passed / total * 100) if total else 0

    print("=" * 62)
    print("MFA CHECK — PRIVILEGED ACCOUNTS")
    print("VindobonaPay GmbH — control A.8.2 / A.8.5 — test CT-01")
    print(f"Test date: {date.today().isoformat()}")
    print("=" * 62)
    print(f"Accounts tested   : {total}")
    print(f"PASS              : {passed}")
    print(f"EXCEPTION         : {len(exceptions)}")
    print(f"Compliance rate   : {rate:.1f}%")

    if exceptions:
        print("-" * 62)
        print("EXCEPTIONS")
        for e in exceptions:
            print(f"  - {e['account']:<22} {e['reason']}")

    print("-" * 62)
    if not exceptions:
        conclusion = "Control operating effectively for the tested population."
    else:
        conclusion = ("Control operating with exceptions. Each exception must be "
                      "remediated or formally accepted (see exceptions register).")
    print(f"Conclusion: {conclusion}")
    print("=" * 62)


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

    accounts = read_csv(args.accounts)
    mfa_lookup = build_mfa_lookup(read_csv(args.mfa))

    results = [evaluate_account(row, mfa_lookup) for row in accounts]
    exceptions = [r for r in results if r["result"] == "EXCEPTION"]

    fields = ["account", "owner", "department", "account_type",
              "mfa_enabled", "method", "result", "reason"]
    write_csv(os.path.join(args.outdir, "mfa_check_results.csv"), results, fields)
    write_csv(os.path.join(args.outdir, "mfa_exceptions.csv"), exceptions, fields)

    print_report(results, exceptions)
    print(f"Results written to: {args.outdir}/mfa_check_results.csv")
    print(f"Exceptions written to: {args.outdir}/mfa_exceptions.csv")


if __name__ == "__main__":
    main()

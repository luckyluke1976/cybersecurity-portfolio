# mfa_privileged_check.py

A small Python script that automates the comparison step of control test
**CT-01** (see [Deliverable 06 — Control Testing & Evidence Automation](./README.md)).

| | |
|---|---|
| **Control tested** | A.8.2 / A.8.5 — privileged access rights and secure authentication |
| **Related risk** | R-02 — compromise of a privileged account (Deliverable 01) |
| **Documented in** | Deliverable 02 — Statement of Applicability |
| **Test frequency** | Quarterly |

> ⚠️ All accounts and enrollment data in this folder are **fictional** and were
> written for this exercise. They do not come from a real Microsoft 365 or
> Entra ID tenant, and no output here represents a real assessment.

## What it does

Reads two CSV exports, compares them account by account, and marks each
privileged account as **PASS** or **EXCEPTION**. It prints a summary and writes
two files: full results and exceptions only.

## What it does not do

It automates a comparison. It does **not**:

- test the control itself — it processes evidence someone else exported;
- confirm that a privileged account belongs to an authorised person;
- verify that the exports are complete or accurate;
- perform the audit or reach the conclusion.

The tester validates the input data, investigates every exception and reaches
the final conclusion.

## Definitions used in this exercise

**Privileged account** — an account with administrative rights over the payment
platform, the Azure subscription or the Microsoft 365 tenant. In the fictional
scenario this covers three types: named administrator accounts (`adm.*`),
service accounts (`svc.*`) and the break-glass emergency account (`brk.*`).
The population comes from the privileged account list, not from the script.

**Strong MFA method** — a *phishing-resistant* method, which is bound to the
origin and cannot be replayed by an attacker controlling a fake login page:

| Classification | Methods |
|---|---|
| **Strong (accepted)** | `fido2_key`, `certificate`, `windows_hello` |
| **Weak (not accepted for privileged access)** | `authenticator_app`, `totp`, `sms`, `voice_call`, `email` |

TOTP authenticator apps are a valid second factor for standard users in this
scenario, but they are **not** accepted for privileged accounts: a user can be
tricked into typing the code into a proxy page.

An account is also raised as an exception when a strong method is registered
**and** a weak one is still available as a fallback: an attacker will target the
weaker path.

## Input files

Both files are plain CSV, expected in the same folder as the script.

### `privileged_accounts.csv` — the population to test

| Column | Required | Notes |
|---|---|---|
| `account` | yes | Account name, matched case-insensitively |
| `owner` | no | Person or role responsible for the account |
| `department` | no | Reported in the output for context |
| `account_type` | no | `admin`, `service` or `break_glass` |
| `status` | no | `enabled` / `active` are tested; anything else is excluded and reported. Defaults to `enabled` if the column is absent |

### `mfa_enrollment.csv` — the identity provider export

| Column | Required | Notes |
|---|---|---|
| `account` | yes | Matched against the privileged account list |
| `mfa_enabled` | yes | `yes` / `no` |
| `method` | yes | One of the values in the table above |
| `display_name`, `last_registration` | no | Ignored by the script, kept for the human reader |

The export normally covers **all** users, not only privileged ones. The script
filters it against the privileged list.

## How to run it

```bash
python mfa_privileged_check.py
```
Runs with the default file names in the current folder.

```bash
python mfa_privileged_check.py --accounts privileged_accounts.csv --mfa mfa_enrollment.csv --outdir output
```
Same check with explicit paths and a chosen output folder.

Python 3.8 or later. No third-party libraries — only the standard library.

## Example output

```
====================================================================
MFA CHECK — PRIVILEGED ACCOUNTS
VindobonaPay GmbH — control A.8.2 / A.8.5 — test CT-01
Test date: 2026-07-28
====================================================================
Rows in privileged account list : 13
Excluded from population        : 1
Accounts tested                 : 12
PASS                            : 9
EXCEPTION                       : 3
Compliance rate                 : 75.0%
--------------------------------------------------------------------
EXCLUDED FROM POPULATION
  - adm.former           Account status is 'disabled', not active
--------------------------------------------------------------------
DATA QUALITY NOTES (not exceptions)
  - adm.sbauer           2 rows in the MFA export (fido2_key)
--------------------------------------------------------------------
EXCEPTIONS
  - adm.tmayer           MFA method is not phishing-resistant: sms
  - svc.backup           MFA not enabled
  - brk.emergency        Account not found in the MFA enrollment report
--------------------------------------------------------------------
```

Two files are written to `output/`:

- `mfa_check_results.csv` — every tested account with its result and reason
- `mfa_exceptions.csv` — the exceptions only, ready to be carried into the
  exceptions register

The reason is written next to each result on purpose: it becomes part of the
evidence instead of living only in the tester's memory.

## Edge cases handled

| Situation | What the script does |
|---|---|
| Disabled or inactive account in the list | Excluded from the population, with the reason printed and the row count reconciled |
| Duplicate rows in the privileged list | First occurrence tested, duplicate reported |
| Duplicate rows in the MFA export | All registrations collected and evaluated together; reported as a data-quality note, not as an exception |
| Account missing from the MFA export | Exception — this is how the break-glass account surfaces |
| `mfa_enabled` set to `no`, or method empty / `none` | Exception — MFA not enabled |
| Method not in either list | Exception flagged for manual review, rather than silently passed |
| Input file missing, empty, or missing a required column | Stops with a clear message and exit code 2 |
| Mixed casing or stray spaces in account names | Normalised before comparison |

## Limitations

- It compares exports. If an export is incomplete, the result is incomplete —
  and the script cannot tell.
- It does not connect to Entra ID. Adding a Graph API call would remove the
  manual export step, but also the ability to re-run the test against the exact
  evidence retained for the period.
- Method classification is a policy decision hard-coded at the top of the file.
  It must be kept aligned with the MFA policy; if the policy changes, the two
  constants change with it.
- It says nothing about whether each privileged account should exist at all.
  That is the access review control (A.5.18, test CT-03), not this one.

## Sample data

`privileged_accounts.csv` and `mfa_enrollment.csv` in this folder are synthetic
files built to exercise every branch of the script: a weak method, a missing
enrollment, an account absent from the export, a disabled account and a
duplicated export row. Running the script against them reproduces the three
CT-01 exceptions recorded in Deliverable 06.

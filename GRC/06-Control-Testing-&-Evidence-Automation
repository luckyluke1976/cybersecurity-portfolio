# Deliverable 06 — Control Testing & Evidence Automation

## What this is

A control testing exercise for **VindobonaPay GmbH**, the fictional
Vienna-based fintech used across this portfolio.

The previous deliverables describe controls. This one asks a different
question: **do those controls actually work?** Eight controls are tested
for design and operating effectiveness, exceptions are recorded with
root cause and remediation, and one test is automated with a Python
script.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. All data in this deliverable is fictional.

## Methodology

- **Two kinds of test.** *Test of design* asks whether the control, as
  described, would prevent or detect the risk. *Test of operating
  effectiveness* asks whether it actually worked during the period. A
  control that fails at design stage does not need a sample: it cannot
  be effective.
- **Sampling follows common audit practice**: 2 occurrences for a
  quarterly control, 15 items for a continuously operating manual
  control, and 100% where the population is small or fully available
  from a system export.
- **Evidence is requested before testing starts**, through an evidence
  request list addressed to the control owners.
- **Exceptions are not closed by the tester.** Each one is assigned to
  the control owner for remediation, or formally accepted by management.

## What's inside

**File:** [`VindobonaPay_Control_Testing.pdf`](./VindobonaPay_Control_Testing.pdf)

- **Test plan:** 8 controls with objective, test type, procedure,
  population, sample size and rationale, evidence required and tester.
- **Evidence request list:** 14 items, with source system and owner.
- **Test results:** outcome of each test — Effective, Effective with
  exceptions, or Not effective.
- **Exceptions and remediation:** 7 exceptions with severity, root
  cause, remediation, owner, target date and the related risk from the
  Risk Register.
- **Summary:** results by conclusion and exceptions by severity.

## The automation

**Script:** [`mfa_privileged_check.py`](./mfa_privileged_check.py)

Test CT-01 checks that every privileged account uses multi-factor
authentication with a strong method. Done by hand it means comparing two
exports line by line, every quarter. The script does the same comparison
in a repeatable way.

```
python mfa_privileged_check.py
```

Input (sample data included in `data/`):

- `privileged_accounts.csv` — the population of privileged accounts
- `mfa_enrollment.csv` — the MFA enrollment export from the identity
  platform

Output:

- a summary in the terminal
- `output/mfa_check_results.csv` — the full result for every account
- `output/mfa_exceptions.csv` — the exceptions only, ready to be added
  to the exceptions register

The script flags three situations as exceptions: MFA not enabled, an
account missing from the enrollment report, and a weak MFA method (SMS
is not accepted for privileged access). On the sample data it finds one
of each.

The point is not the code. It is that the same test can be re-run at any
time and always produces the same evidence, with the reason for every
decision written down rather than remembered.

## Key decisions

- **Not everything passed.** One control failed at design stage
  (quarterly access reviews are described in the SoA but have no
  procedure and no records), and four passed with exceptions. A test
  cycle where everything passes usually means the tests were too easy.

- **Testing confirmed the risk assessment.** All three High exceptions
  relate to privileged access, which is the highest residual risk
  (R-02) in the Risk Register. The documents agree because they describe
  the same organization.

- **Service accounts and break-glass accounts are part of the
  population.** They are the accounts most often left out of an MFA
  rollout, and therefore the ones worth testing.

- **The exception severity drives the target date**, not the other way
  around.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not an audit.

The test results and the sample data are constructed to be realistic for
the scenario described in the Organization Context: they are not
extracted from real systems. In a real engagement the evidence would be
pulled from the actual identity platform, device management and HR
systems, and the tester would need to be independent from the control
owner.

What this deliverable is meant to show is the method: how a control
moves from a line in a Statement of Applicability to a test, a sample,
a result, an exception and a remediation action with an owner.

## Portfolio

⬅️ Deliverable 05 — DORA Compliance Mapping

This is the final deliverable in the current set.

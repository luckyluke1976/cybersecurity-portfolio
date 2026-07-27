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

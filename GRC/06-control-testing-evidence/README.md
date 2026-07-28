# Deliverable 06 — Control Testing & Evidence Automation

## What this is

A control testing exercise for **VindobonaPay GmbH**, the fictional
Vienna-based licensed payment institution used across this portfolio.

The previous deliverables describe controls. This exercise demonstrates
how their **design and operating effectiveness would be tested**, using
fictional but realistic evidence. Eight controls are tested, exceptions
are recorded with root cause and remediation, and one evidence-testing
procedure is automated with a Python script.

> ⚠️ **Assumptions and limitations**
> VindobonaPay GmbH is a fictional company created for educational
> purposes. All populations, samples, evidence and test results in this
> deliverable are fictional. They demonstrate a testing methodology and
> do not represent assurance work performed on a real Microsoft 365 or
> Azure environment.

## Methodology

- **Two kinds of test.** *Test of design* asks whether the control, as
  described, would prevent or detect the risk. *Test of operating
  effectiveness* asks whether the control operated as intended during
  the simulated review period, based on fictional evidence.
  If a control is not adequately designed, formal operating-effectiveness
  testing is normally not meaningful until the design weakness is
  addressed — although limited evidence may still be reviewed to
  understand the issue and support remediation.

- **Sampling is illustrative and risk-based.** Sample sizes were selected
  for this fictional exercise considering the control frequency,
  population size, level of automation and associated risk. They are not
  presented as universal audit thresholds. The exercise uses two
  occurrences for selected quarterly controls, 15 items for selected
  high-frequency manual controls, and full-population testing where a
  complete system export is available.

- **Evidence is requested before testing starts**, through an evidence
  request list addressed to the control owners.

- **The tester is assumed to be independent** from the control owner and
  from the activities being tested. In an organization of this size this
  would not mean a dedicated internal audit department — only that the
  test is performed by a function other than the one operating the
  control.

- **Exceptions are not closed by the tester.** Each one is assigned to
  the control owner for remediation, or formally accepted by management.
  An exception is not automatically an ISO/IEC 27001 nonconformity:
  exceptions are evaluated against the test criteria and assessed for
  significance before being reported as control deficiencies or
  nonconformities.

### Conclusion criteria

Design and operating effectiveness are concluded separately, because a
control can be well designed and still fail in operation.

| Conclusion | Meaning |
|---|---|
| **Effective** | Design adequate and no material operating exceptions identified |
| **Effective with exceptions** | Design adequate, but limited deviations were found that do not invalidate the control overall |
| **Not effective** | Design is inadequate, or operating deviations are significant or frequent enough to prevent reliance on the control |

## What's inside

**File:** [`VindobonaPay_Control_Testing.pdf`](./VindobonaPay_Control_Testing.pdf)

- **Test plan:** 8 controls with objective, test type, procedure,
  population, sample size and rationale, evidence required and tester.
- **Evidence request list:** 14 items, with source system and owner.
- **Test results:** design conclusion and operating-effectiveness
  conclusion for each test.
- **Exceptions and remediation:** 7 exceptions with severity, root
  cause, remediation, owner, target date and the related risk from the
  Risk Register.
- **Summary:** results by conclusion and exceptions by severity.

## The automation

**Script:** [`mfa_privileged_check.py`](./mfa_privileged_check.py)

Test CT-01 checks that every privileged account is protected by a
phishing-resistant multi-factor authentication method. Done by hand it
means comparing two exports line by line, every quarter. The script
automates that comparison step.

**What "strong" means in this exercise.** MFA is enforced for all users
in the defined scenario (see
[00 — Organization Context](../00-organization-context/README.md)), so
the test is not about whether MFA exists. It is about *method strength*:
phishing-resistant methods — FIDO2 security keys and certificate-based
authentication — are classified as strong. Other registered methods are
reported separately for review rather than treated as a pass.

**What the script does and does not do.** It automates the comparison
step. The tester remains responsible for validating the input data,
investigating exceptions and reaching the final conclusion. The script
does not test the control itself, does not confirm that a privileged
account belongs to an authorised person, and does not perform the audit.

Input format, required columns, execution command, sample output and
known limitations are documented in the script's own README.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not assurance work.

All populations, samples, evidence and test results are fictional. The
deliverable demonstrates the control-testing methodology; it does not
represent testing performed on a real environment, and no conclusion
here should be read as an audit opinion.

In a real engagement the evidence would be obtained directly from the
source systems, its completeness and accuracy would be validated, and
the conclusions would be reviewed before being reported to management.

## Portfolio complete

⬅️ Back to the [portfolio overview](../README.md)

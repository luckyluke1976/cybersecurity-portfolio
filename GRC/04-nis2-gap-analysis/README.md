# Deliverable 04 — NIS2 Applicability & Gap Analysis

*Comparative analysis for a DORA financial entity*

## What this is

An applicability and gap analysis of the **NIS2 Directive (EU) 2022/2555**
for **VindobonaPay GmbH**, the fictional Vienna-based licensed payment
institution used across this portfolio.

The analysis answers two questions, in this order:

1. **Does NIS2 apply to VindobonaPay, and to what extent?**
2. **Where the directive does apply, what is missing today?**

> ⚠️ **Assumptions and limitations**
> VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used. Applicability conclusions,
> implementation status and remediation actions are illustrative
> assessments based on the defined scenario — they are not legal advice
> and do not represent a compliance assessment.
>
> No regulatory text is reproduced in this repository. Articles are
> referenced by number, with descriptions written in my own words.

## Headline finding: the lex specialis carve-out

VindobonaPay is a **financial entity**, and this changes the answer to
question 1.

- **NIS2 Article 4** provides that where sector-specific Union law
  imposes cybersecurity risk-management or incident-notification
  requirements at least equivalent in effect, the corresponding NIS2
  provisions do not apply.
- **DORA Article 1(2)** states that DORA is such a sector-specific act
  for financial entities, and **DORA Recital 16** describes DORA as
  *lex specialis* in relation to NIS2. **NIS2 Recital 28** mirrors this.
- The European Commission has published guidelines on the application of
  Article 4(1) and (2), confirming the areas covered by the carve-out:
  ICT risk management, ICT incident management and major incident
  reporting, digital operational resilience testing, information-sharing
  arrangements and ICT third-party risk.

**In practice for VindobonaPay:** DORA is the primary framework. Incident
reports go to the financial competent authority, not to the

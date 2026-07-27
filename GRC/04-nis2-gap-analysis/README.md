# Deliverable 04 — NIS2 Applicability & Gap Analysis

## What this is

An applicability and gap analysis of the **NIS2 Directive (EU) 2022/2555**
for **VindobonaPay GmbH**, the fictional Vienna-based fintech used across
this portfolio.

The analysis answers two questions, in this order:

1. **Does NIS2 apply to VindobonaPay, and to what extent?**
2. **Where the directive does apply, what is missing today?**

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used.
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
reports go to the financial competent authority, not to the national
CSIRT under the NIS2 regime, and the ICT risk framework follows DORA.

**But the carve-out is not total.** NIS2 remains relevant because:

- it is a **directive**, so national transposition may add requirements
  (in Austria, the national NIS implementation)
- obligations that are not the subject of the carve-out — such as
  registration duties — may still apply
- **customers and suppliers** in other sectors are in NIS2 scope and
  pass requirements down the supply chain, which VindobonaPay must be
  able to answer

This is why the analysis was still worth doing: knowing that a
requirement is carved out is itself a compliance finding, and it has to
be documented rather than assumed.

## Methodology

- Assessment of the **10 risk-management measures of Article 21(2)(a)
  to (j)**, plus **Article 20** (management body accountability and
  training) and **Article 23** (incident notification).
- For each requirement:
  - **Applicability**: does it apply directly, or is it superseded by
    DORA under the carve-out?
  - **Current status**: Compliant / Partial / Gap, based on the
    Statement of Applicability (Deliverable 01) and the Risk Register
    (Deliverable 02)
  - **Supporting evidence** — the ISMS controls and documents involved
  - **Gap description** and **remediation action**, with owner and
    target date
- Status decisions are consistent with the SoA: a requirement supported
  only by controls marked "Partially implemented" cannot be reported as
  fully compliant.

## What's inside

**File:** [`VindobonaPay_NIS2_Gap_Analysis.pdf`](./VindobonaPay_NIS2_Gap_Analysis.pdf)

- **Applicability analysis:** requirement by requirement, which NIS2
  provisions apply directly and which are superseded by DORA.
- **Gap analysis:** current status of each requirement, evidence, gap
  description, remediation action, owner and target date.
- **Summary:** requirements by status and by applicability.

## Key decisions

- **Applicability is assessed before compliance.** Running a gap
  analysis against requirements that do not apply would produce
  remediation work with no legal basis.

- **Carved-out requirements are documented, not deleted.** They stay in
  the analysis with their status, because the equivalent DORA obligation
  is usually stricter — and because the reasoning must be visible to an
  auditor.

- **Two areas are weak regardless of which framework applies:** supply
  chain security (Art. 21(2)(d)) and management body accountability and
  training (Art. 20). Both appear as gaps in the SoA as well, which is
  a consistency check between deliverables rather than a coincidence.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not legal advice.

NIS2 is a directive: its practical effect depends on national
transposition, and the interaction between the national implementation
and DORA is exactly the kind of question that would be confirmed with
legal counsel in a real project. The analysis reflects how I read the
relationship between the two frameworks, with the references needed for
anyone to check it.

## Next step in the portfolio

➡️ Deliverable 05 — DORA Compliance Mapping

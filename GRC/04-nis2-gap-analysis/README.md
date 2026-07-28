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
reports go to the financial competent authority, not to the national
CSIRT under the NIS2 regime, and the ICT risk framework follows DORA.

**But the carve-out does not remove every interaction with the NIS2
ecosystem:**

- NIS2 is a **directive**, so national legislation must still be reviewed
  to identify any separate administrative, sectoral or national
  cybersecurity obligations — without assuming that requirements
  displaced by DORA automatically become applicable again.
- Any remaining **national administrative or registration obligation**
  must be assessed under the applicable Austrian legislation rather than
  inferred from the directive alone.
- **NIS2-regulated customers** may impose cybersecurity, assurance and
  incident-notification requirements on VindobonaPay contractually, as
  part of their own supply-chain risk management. These are commercial
  and contractual requirements, not direct NIS2 obligations for
  VindobonaPay — a distinction that matters when answering vendor
  questionnaires.

This is why the analysis was still worth doing: knowing that a
requirement is carved out is itself a compliance finding, and it has to
be documented rather than assumed.

### Austrian legal status (assessed as of July 2026)

Austria transposed NIS2 through the **NISG 2026** (Article 1 of BGBl. I
No. 94/2025, published 23 December 2025), which replaces the NISG 2018
and the NIS-Verordnung. Its substantive provisions enter into force on
**1 October 2026**, with registration of in-scope entities required
within three months of that date.

Whether — and to what extent — a DORA financial entity carries residual
administrative or registration duties under the NISG 2026 is a question
of Austrian national law and is not resolved in this exercise. It is
flagged here as an open point that would be confirmed with legal counsel.
This section should be reviewed whenever the national legal framework
changes.

## Methodology

- Assessment of the **10 risk-management measures of Article 21(2)(a)
  to (j)**, plus **Article 20** (management body accountability and
  training) and **Article 23** (incident notification).
- Each requirement is assessed along **two separate dimensions**, because
  legal applicability and implementation maturity are different
  questions:

**1. Legal applicability**

| Value | Meaning |
|---|---|
| **Directly applicable** | The NIS2 provision applies to VindobonaPay as written |
| **Disapplied — DORA lex specialis** | Superseded by an equivalent DORA obligation under NIS2 Article 4 |
| **Indirect / contractual relevance** | Not a direct obligation, but may reach VindobonaPay through customer contracts |
| **Not applicable** | Outside the defined organizational scope |

**2. Implementation assessment** (against the applicable obligation —
DORA where the NIS2 provision is disapplied)

| Value | Meaning |
|---|---|
| **Implemented** | Supported by controls assessed as fully implemented in the SoA |
| **Partially implemented** | Supported by controls assessed as partially implemented |
| **Gap** | No supporting control or process in place |
| **Not assessed** | Outside the scope of this exercise |

- For each requirement the matrix also records the **corresponding DORA
  article**, the **supporting evidence** (ISMS controls and documents
  involved), a **gap description** and a **remediation action** with
  owner and target date.
- Status decisions are consistent with the SoA: a requirement supported
  only by controls marked "Partially implemented" cannot be reported as
  fully implemented.

This separation means the analysis never states that VindobonaPay has a
"NIS2 gap" on a provision that does not apply to it. It states that the
NIS2 provision is disapplied, and that the corresponding DORA obligation
shows a gap.

## What's inside

**File:** [`VindobonaPay_NIS2_Gap_Analysis.pdf`](./VindobonaPay_NIS2_Gap_Analysis.pdf)

- **Applicability analysis:** requirement by requirement, which NIS2
  provisions apply directly and which are disapplied under the DORA
  carve-out, with the corresponding DORA article.
- **Gap analysis:** implementation status of each obligation, evidence,
  gap description, remediation action, owner and target date.
- **Summary:** requirements by legal applicability and by implementation
  status.

## Key decisions

- **Applicability is assessed before compliance.** Running a gap
  analysis against requirements that do not apply would produce
  remediation work with no legal basis.

- **Carved-out requirements are documented, not deleted.** They stay in
  the analysis with their corresponding DORA obligation and its
  implementation status, because the corresponding DORA obligation may
  be more detailed, prescriptive or sector-specific — and because the
  reasoning must be visible to an auditor.

- **Two areas are weak regardless of which framework applies.**
  - **ICT third-party risk management** — assessed as a **DORA Chapter V
    gap**; NIS2 Article 21(2)(d) is retained as the comparative
    reference.
  - **Management body accountability and training** — assessed as a
    **DORA Article 5 gap**; NIS2 Article 20 is retained as the
    comparative reference. DORA Article 5 already requires the
    management body to define, approve and oversee the ICT risk
    management framework and to maintain adequate knowledge through
    regular training, so the directly applicable legal basis is DORA,
    not the directive.

  Both also appear as gaps in the SoA, which is a consistency check
  between deliverables rather than a coincidence.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not legal advice.

NIS2 is a directive: its practical effect depends on national
transposition, and the interaction between the Austrian implementation
and DORA is exactly the kind of question that would be confirmed with
legal counsel in a real project. The analysis reflects how I read the
relationship between the two frameworks, with the references needed for
anyone to check it.

The cross-framework view of the same domains is covered in
[Deliverable 03 — Control Mapping Matrix](../03-control-mapping/README.md).

## Next step in the portfolio

➡️ Deliverable 05 — DORA Compliance Mapping

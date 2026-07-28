# Deliverable 05 — DORA Compliance Mapping

*A regulation-level mapping against Regulation (EU) 2022/2554*

## What this is

A compliance mapping of the **Digital Operational Resilience Act —
Regulation (EU) 2022/2554** for **VindobonaPay GmbH**, the fictional
Vienna-based licensed payment institution used across this portfolio.

DORA is the framework that actually governs VindobonaPay: the NIS2
analysis (Deliverable 04) concluded that, as a financial entity, the
equivalent NIS2 obligations are disapplied under the *lex specialis*
principle. This deliverable is where those obligations are assessed
against the regulation that applies.

> ⚠️ **Assumptions and limitations**
> VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used. Applicability conclusions,
> implementation status and remediation actions are illustrative
> assessments based on the defined scenario — they are not legal advice
> and do not represent a compliance assessment.
>
> No regulatory text is reproduced in this repository. Articles are
> referenced by number, with descriptions written in my own words.

## Applicability: which regime applies

Before assessing compliance, the applicable tier has to be established.

- **In scope.** DORA applies to the categories of financial entities
  listed in Article 2. As an authorised payment institution,
  VindobonaPay is in scope.
- **General framework, not the simplified one.** Article 16 provides a
  simplified ICT risk management framework for specific entity types,
  including payment institutions *exempted* under PSD2. VindobonaPay is
  authorised and not exempt, so it is subject to the **general ICT risk
  management framework under Articles 5 to 15**.
- **Not a microenterprise.** Article 3(60) defines a microenterprise as
  an entity which employs fewer than 10 persons and has an annual
  turnover and/or annual balance-sheet total not exceeding EUR 2 million.
  With ~80 employees, VindobonaPay does not qualify. Because it is not a
  microenterprise, responsibility for managing and overseeing ICT risk
  must be assigned to an appropriately independent control function.
  Under the general framework, the ICT risk management framework is also
  subject to periodic review and internal audit.
- **Competent authority:** the Austrian Financial Market Authority (FMA).
- **Applicable since 17 January 2025.**

Establishing the tier first matters: a generic DORA checklist built for
a large bank would produce requirements that do not apply, and a
simplified-regime checklist would understate the obligations.

## Methodology

The mapping follows the structure of the regulation, pillar by pillar:

| Pillar | Chapter | Articles | Applicable to VindobonaPay |
|---|---|---|---|
| 1 — ICT risk management | II | 5–15 | Yes (Art. 16 simplified framework does not apply) |
| 2 — ICT-related incident management, classification and reporting | III | 17–23 | Yes |
| 3 — Digital operational resilience testing | IV | 24–27 | Arts. 24–25 yes; Arts. 26–27 (TLPT) conditional |
| 4 — Management of ICT third-party risk | V | 28–30 | Yes — direct entity obligations |
| | V | 31–44 | Oversight of critical ICT providers — supervisory context |
| 5 — Information-sharing arrangements | VI | 45 | Optional provision |

### Applicability type

Not every article of a regulation creates a direct obligation for every
entity. Each requirement is therefore classified as:

| Type | Meaning |
|---|---|
| **Direct entity obligation** | Applies to VindobonaPay as written |
| **Conditional obligation** | Applies only if a triggering condition occurs (e.g. designation by the competent authority) |
| **Optional provision** | The regulation permits, but does not require, the activity |
| **Supervisory context** | Addressed to the ESAs, the Lead Overseer or ICT providers — included for completeness, not assessed as a compliance obligation |
| **Not applicable** | Outside the defined organizational scope |

**Articles 31–44 are included for context but are not assessed as direct
compliance obligations of VindobonaPay**, since they primarily govern the
designation and oversight of critical ICT third-party service providers,
the Lead Overseer and the powers of the supervisory authorities. The
direct third-party obligations of a financial entity sit in Articles
28–30: general principles, preliminary assessment of concentration risk
and the contractual provisions required for ICT services.

### Status vocabulary

For each requirement the mapping records:

- the **article** and what it requires, in plain terms
- the **applicability type** (see above)
- **implementation status**: Implemented / Partially implemented / Gap /
  Not assessed — the same vocabulary used in Deliverables 01, 02 and 04
- **supporting evidence** from the ISMS — relevant ISO/IEC 27001 clauses,
  Annex A controls, policies, procedures, records and technical
  configurations documented across the portfolio
- the **gap**, where one exists
- the **action**, with owner and target date

Status decisions stay consistent with the rest of the portfolio: a
requirement supported only by controls marked "Partially implemented"
in the SoA (Deliverable 02) is not reported as implemented.

## What's inside

**File:** [`VindobonaPay_DORA_Mapping.pdf`](./VindobonaPay_DORA_Mapping.pdf)

- **Compliance mapping:** requirements across the five pillars, with
  applicability type, implementation status, evidence, gap, action,
  owner and target date.
- **Priority actions:** the gaps that carry the highest regulatory
  exposure, in the order they should be addressed.
- **Summary:** requirements by applicability type, by status and by
  pillar.

## Key decisions

- **The tier is established before the assessment.** Proportionality
  under DORA is not an exemption from compliance. It affects both the
  applicable framework and how requirements are implemented, taking into
  account the entity's size, overall risk profile and the nature, scale
  and complexity of its activities. That decision has to be documented.

- **The ISMS carries most of Pillar 1.** ICT risk management, protection,
  detection and recovery map closely onto requirements and controls
  already documented in the SoA — including the management-system
  clauses of ISO/IEC 27001 covering leadership, competence, monitoring,
  internal audit and management review, which support the governance and
  control-function requirements of Chapter II. This is where ISO/IEC
  27001 pays off.

- **The gaps concentrate in Pillars 2, 3 and 4** — incident
  classification and regulatory reporting, the resilience testing
  programme, and ICT third-party risk (register of information,
  contractual provisions, concentration risk, exit strategies). These
  are the same three domains rated *No direct support* in Deliverable 03
  and assessed as gaps in Deliverable 04. The three documents agree
  because they describe the same organization.

- **TLPT status: not currently designated.** Threat-led penetration
  testing under Articles 26–27 applies to financial entities identified
  by the competent authority. VindobonaPay has not been assumed to have
  received a TLPT designation under the fictional scenario. The
  requirement is conditional and would become applicable if the FMA
  identified the company under Article 26 and the relevant selection
  criteria — which consider systemic impact, ICT risk profile and
  technology characteristics, not headcount alone. It is recorded rather
  than ignored, because that status can change.

- **Article 45 is treated as an optional enabling provision.**
  VindobonaPay is not required to participate in a threat-information-
  sharing arrangement, so the article is neither a gap nor a compliance
  achievement. If the company joined one, the applicable governance
  conditions and the obligation to notify the competent authority of
  entry into and exit from the arrangement would then be assessed.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not legal advice.

**This is a high-level assessment against Regulation (EU) 2022/2554. It
is not a complete DORA compliance assessment**, because the regulatory
and implementing technical standards have not been assessed requirement
by requirement. Those standards specify much of the operational detail —
incident classification thresholds, reporting templates, the format and
content of the register of information, and the conduct of resilience
testing. The mapping stays at the level of the regulation itself and
notes where the technical standards govern the detail.

In a real project these would be worked through with the compliance
function and legal counsel, and kept under review as the standards
evolve.

## Next step in the portfolio

➡️ Deliverable 06 — Control Testing & Evidence Automation

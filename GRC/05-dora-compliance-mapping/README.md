# Deliverable 05 — DORA Compliance Mapping

## What this is

A compliance mapping of the **Digital Operational Resilience Act —
Regulation (EU) 2022/2554** for **VindobonaPay GmbH**, the fictional
Vienna-based fintech used across this portfolio.

DORA is the framework that actually governs VindobonaPay: the NIS2
analysis (Deliverable 04) concluded that, as a financial entity, most
NIS2 obligations are superseded by DORA under the *lex specialis*
principle. This deliverable is where those obligations are assessed
against the regulation that applies.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used.
>
> No regulatory text is reproduced in this repository. Articles are
> referenced by number, with descriptions written in my own words.

## Applicability: which regime applies

Before assessing compliance, the applicable tier has to be established.

- **In scope.** DORA applies to the categories of financial entities
  listed in Article 2. As an authorised payment institution,
  VindobonaPay is in scope.
- **Full regime, not the simplified one.** Article 16 provides a
  simplified ICT risk management framework for specific entity types,
  including payment institutions *exempted* under PSD2. VindobonaPay is
  authorised, not exempted, so **Articles 5 to 15 apply in full**.
- **Not a microenterprise.** Article 3(60) defines a microenterprise as
  an entity with fewer than 10 employees and turnover or balance sheet
  total not exceeding EUR 2 million. With ~80 employees, VindobonaPay
  does not qualify, so the obligations reserved for non-microenterprises
  apply: an independent ICT risk control function, yearly review of the
  framework and internal audit of it.
- **Competent authority:** the Austrian Financial Market Authority (FMA).
- **Applicable since 17 January 2025.**

Establishing the tier first matters: a generic DORA checklist built for
a large bank would produce requirements that do not apply, and a
simplified-regime checklist would understate the obligations.

## Methodology

The mapping follows the structure of the regulation, pillar by pillar:

| Pillar | Chapter | Articles |
|---|---|---|
| 1 — ICT risk management | II | 5–16 |
| 2 — ICT-related incident management, classification and reporting | III | 17–23 |
| 3 — Digital operational resilience testing | IV | 24–27 |
| 4 — Management of ICT third-party risk | V | 28–44 |
| 5 — Information-sharing arrangements | VI | 45 |

For each requirement the mapping records:

- the **article** and what it requires, in plain terms
- **current status**: Compliant / Partial / Gap
- **supporting evidence** from the ISMS — the Annex A controls,
  policies and configurations already documented in Deliverables 01
  and 02
- the **gap**, where one exists
- the **action**, with owner and target date

Status decisions stay consistent with the rest of the portfolio: a
requirement supported only by controls marked "Partially implemented"
in the SoA is not reported as compliant.

## What's inside

**File:** [`VindobonaPay_DORA_Mapping.pdf`](./VindobonaPay_DORA_Mapping.pdf)

- **Compliance mapping:** requirements across the five pillars, with
  status, evidence, gap, action, owner and target date.
- **Priority actions:** the gaps that carry the highest regulatory
  exposure, in the order they should be addressed.
- **Summary:** requirements by status and by pillar.

## Key decisions

- **The tier is established before the assessment.** Proportionality
  under DORA is not a discount: it determines which articles apply, and
  that decision has to be documented.

- **The ISMS carries most of Pillar 1.** ICT risk management, protection,
  detection and recovery map closely onto controls already implemented
  and documented in the SoA. This is where ISO/IEC 27001 pays off.

- **The gaps concentrate in Pillars 2, 3 and 4** — incident
  classification and regulatory reporting, the resilience testing
  programme, and ICT third-party risk (register of information,
  contractual provisions, concentration risk, exit strategies). These
  are the same three areas flagged as "Beyond ISMS" in Deliverable 03
  and as gaps in Deliverable 04. The three documents agree because they
  describe the same organization.

- **TLPT is assessed as not currently applicable.** Threat-led
  penetration testing under Articles 26–27 applies to entities
  identified by the competent authority. VindobonaPay would not expect
  to be identified at its current size, but the requirement is recorded
  rather than ignored, because that status can change.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not legal advice.

DORA is completed by a set of regulatory and implementing technical
standards that specify details such as incident classification
thresholds, reporting templates and the format of the register of
information. The mapping stays at the level of the regulation itself
and notes where the technical standards govern the detail. In a real
project these would be worked through with the compliance function and
legal counsel, and kept under review as the standards evolve.

## Next step in the portfolio

➡️ Deliverable 06 — Control Testing & Evidence Automation

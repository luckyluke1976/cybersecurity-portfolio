# Deliverable 03 — Control Mapping Matrix (ISO/IEC 27001 ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0)

## What this is

A cross-framework mapping for **VindobonaPay GmbH**, the fictional
Vienna-based licensed payment institution used across this portfolio.

The matrix shows how the security domains of the company are addressed by
four frameworks at the same time: the ISO/IEC 27001 requirements and Annex
A controls documented in the SoA (Deliverable 02), the NIS2 Directive, the
DORA Regulation and the NIST Cybersecurity Framework 2.0.

The goal is practical: a company does not run four separate compliance
programs. It operates one integrated governance, risk and control
environment, reuses common evidence across frameworks, and implements
additional processes where specific legal obligations require them.

> ⚠️ **Assumptions and limitations**
> VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used. The mapping reflects my own
> reading of the relationship between these frameworks under the defined
> scenario — it is not legal advice and does not represent a compliance
> assessment.
>
> No standard or regulatory text is reproduced in this repository. The
> matrix references articles and control identifiers only, with
> descriptions written in my own words.

## Why this matters for VindobonaPay

VindobonaPay is a **financial entity**, which changes the regulatory
picture:

- **DORA applies as sector-specific Union legislation.** For the purposes
  of Article 4 of NIS2, DORA is sector-specific Union legislation covering
  financial entities. Where DORA provides ICT risk-management and
  incident-reporting requirements that are at least equivalent in effect,
  the corresponding NIS2 obligations do not apply to the same entity. NIS2
  is retained in this portfolio as a comparative framework and as the
  broader EU cybersecurity baseline; the applicability question itself is
  examined in Deliverable 04.
- **ISO/IEC 27001** is not a legal requirement, but it is the management
  system that produces most of the evidence both regulations expect —
  and it is what enterprise merchants ask for in vendor assessments.
- **NIST CSF 2.0** is not mandatory in the EU. It is included because it
  provides a complementary outcome-based view that helps identify
  potential gaps across Govern, Identify, Protect, Detect, Respond and
  Recover.

## Methodology

- The mapping is organized by **security domain**, not control by
  control. Mapping 93 Annex A controls one-to-one against regulatory
  articles would force artificial matches: the frameworks are written at
  different levels of detail.
- For each domain the matrix shows:
  - the relevant **ISO/IEC 27001 clauses (4–10)** — the management-system
    requirements that support the domain
  - the relevant **ISO/IEC 27001 Annex A controls** (as documented in the SoA)
  - the corresponding NIS2 article
  - the corresponding DORA article
  - the corresponding NIST CSF 2.0 function and category
  - a **coverage rating** with a short note on what the regulations
    require in addition
- References were checked against the official texts (EUR-Lex for NIS2
  and DORA, NIST for CSF 2.0).

### Annex A is not the whole standard

Several regulatory requirements — governance and accountability of the
management body, competence and awareness, monitoring and measurement,
internal audit, management review and continual improvement — map to the
**management-system clauses of ISO/IEC 27001 (4–10)** rather than to Annex
A controls. The matrix includes a dedicated clause column for this reason:
treating Annex A as the entire standard would misrepresent where an ISMS
actually addresses these obligations.

### Coverage ratings

| Rating | Meaning |
|---|---|
| **Strong support** | ISO requirements and controls substantially support the obligation, but regulatory validation is still required |
| **Partial support** | ISO covers part of the requirement; additional processes or evidence are required |
| **No direct support** | A dedicated regulatory process or deliverable is required |
| **Out of scope** | Not relevant to the defined organizational scope |

### What a mapping does and does not mean

A mapping indicates that one requirement or control **may support** another
framework outcome. It does not establish equivalence, implementation
effectiveness or legal compliance. `A.5.19 → DORA Article 28` means that
the control contributes to the obligation — not that implementing the
control satisfies the article.

## What's inside

**File:** [`VindobonaPay_Control_Mapping.pdf`](./VindobonaPay_Control_Mapping.pdf)

- **Mapping matrix:** security domains mapped across the four
  frameworks, with ISO clause and Annex A references and a coverage
  rating for each domain.
- **Gap view:** the DORA obligations that an ISO/IEC 27001 ISMS does not
  automatically satisfy — the areas where additional work is needed.
- **Summary:** domains with strong mapping coverage, partial coverage, or
  no direct ISO coverage under the fictional scenario.

## Key decisions

- **Overlap is documented, not assumed.** ISO/IEC 27001 provides a
  strong foundation for many NIS2 and DORA requirements, but it does not
  guarantee full compliance. No coverage percentage is claimed: the
  actual overlap depends on scope, implementation and interpretation.

- **The DORA-specific areas are called out explicitly.** Digital
  operational resilience testing, regulatory incident reporting within
  defined deadlines, contractual requirements for ICT third-party
  providers and the register of information are obligations that no
  Annex A control satisfies on its own.

- **The mapping reflects VindobonaPay's own scope.** It is not a generic
  crosswalk: domains that do not apply to the company (for example
  industrial control systems) are not included.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not legal advice.

Mapping frameworks always involves interpretation: two analysts can
place the same requirement in slightly different positions, and national
implementations of NIS2 differ between Member States. The matrix shows
how I read the relationship between these frameworks, with the
references needed for anyone to check it.

In a real project this document would be reviewed with legal counsel and
kept up to date as regulatory technical standards evolve.

## Next step in the portfolio

➡️ Deliverable 04 — NIS2 Applicability & Gap Analysis

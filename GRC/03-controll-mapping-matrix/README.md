# Deliverable 03 — Control Mapping Matrix (ISO/IEC 27001 ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0)

## What this is

A cross-framework mapping for **VindobonaPay GmbH**, the fictional
Vienna-based fintech used across this portfolio.

The matrix shows how the security domains of the company are addressed
by four frameworks at the same time: the ISO/IEC 27001 controls already
documented in the SoA (Deliverable 01), the NIS2 Directive, the DORA
Regulation and the NIST Cybersecurity Framework 2.0.

The goal is practical: a company does not run four separate compliance
programs. It runs one set of controls and demonstrates them against
several frameworks.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used.
>
> No standard or regulatory text is reproduced in this repository. The
> matrix references articles and control identifiers only, with
> descriptions written in my own words.

## Why this matters for VindobonaPay

VindobonaPay is a **financial entity**, which changes the regulatory
picture:

- **DORA applies as sector-specific legislation.** For ICT risk
  management and incident reporting, DORA takes precedence over NIS2 for
  financial entities. NIS2 remains relevant as the general framework and
  for national implementation.
- **ISO/IEC 27001** is not a legal requirement, but it is the management
  system that produces most of the evidence both regulations expect —
  and it is what enterprise merchants ask for in vendor assessments.
- **NIST CSF 2.0** is not mandatory in the EU. It is included because it
  organizes the same material by function (Govern, Identify, Protect,
  Detect, Respond, Recover), which is a useful way to check that nothing
  is missing.

## Methodology

- The mapping is organized by **security domain**, not control by
  control. Mapping 93 Annex A controls one-to-one against regulatory
  articles would force artificial matches: the frameworks are written at
  different levels of detail.
- For each domain the matrix shows:
  - the relevant ISO/IEC 27001 Annex A controls (as documented in the SoA)
  - the corresponding NIS2 article
  - the corresponding DORA article
  - the corresponding NIST CSF 2.0 function and category
  - a short note on **coverage**: whether ISO/IEC 27001 alone is
    sufficient, or what the regulations require in addition
- References were checked against the official texts (EUR-Lex for NIS2
  and DORA, NIST for CSF 2.0).

## What's inside

**File:** [`VindobonaPay_Control_Mapping.pdf`](./VindobonaPay_Control_Mapping.pdf)

- **Mapping matrix:** security domains mapped across the four
  frameworks, with a coverage note for each domain.
- **Gap view:** the DORA obligations that an ISO/IEC 27001 ISMS does not
  automatically satisfy — the areas where additional work is needed.
- **Summary:** how many domains are fully supported by the existing
  ISMS, partially supported, or need dedicated work.

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

➡️ Deliverable 04 — NIS2 Gap Analysis

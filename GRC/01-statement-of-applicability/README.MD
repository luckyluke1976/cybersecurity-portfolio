# Deliverable 01 — Statement of Applicability (ISO/IEC 27001:2022)

## What this is

A Statement of Applicability (SoA) for **VindobonaPay GmbH**, a fictional
Vienna-based fintech (~80 employees) used as the case study across this
whole portfolio.

The document uses the **93 controls of ISO/IEC 27001:2022 Annex A as a
reference set** and documents their applicability to the defined
organization: whether each control applies, why, its implementation
status, owner, supporting evidence and open remediation actions.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used.
>
> Control descriptions have been independently paraphrased for
> educational purposes. No ISO/IEC standard text is reproduced in this
> repository.

## Assumptions

The decisions in this SoA are based on the following scenario:

- Fictional company, built for learning purposes
- Cloud-first infrastructure (Microsoft 365 + Azure)
- All software is developed in-house
- Payroll is outsourced to an external provider
- Hybrid work model (office in Vienna + remote)
- The company processes payment and customer data

Full scenario — company profile, roles, technology and current security
posture: [00 — Organization Context](../00-organization-context/README.md).

## What's inside

**File:** [`VindobonaPay_SoA.pdf`](./VindobonaPay_SoA.pdf)

- **Statement of Applicability:** all 93 Annex A controls with:
  - Applicable? (Yes / No)
  - Justification for inclusion or exclusion
  - Implementation status (Implemented / Partially implemented / Planned),
    color-coded
  - Control owner
  - Related Risk ID (linked to the Risk Register — Deliverable 02)
  - Evidence / Reference (policy, procedure or configuration supporting
    the control)
  - Remediation action with target date (for controls not yet fully
    implemented)
- **Summary page:** applicable and excluded controls, implementation
  status and open remediation actions.

## Key decisions

- **A.8.30 was assessed as not applicable.**
  Under the defined scenario, software development is performed entirely
  by internal personnel and no development activities are outsourced.
  The exclusion and its justification are documented in the SoA.

- **92 Annex A controls were assessed as applicable**, based on the
  organization's business context, information security risks,
  regulatory exposure and reliance on cloud and third-party services.

- **Implementation is still in progress.**
  About 60% of applicable controls are currently implemented. The
  remaining controls are partially implemented or planned, with owners
  and remediation actions assigned.

- **The Risk ID column links the SoA to the Risk Register (v2.0).**
  Each applicable control now references the risks it treats (R-01 to
  R-16, see Deliverable 02). Controls without a Risk ID support the ISMS
  as baseline controls. This update reflects how an SoA evolves in
  practice: it is a living document, not a one-time deliverable.

## Why it matters

The Statement of Applicability links the organization's risks to the
selected Annex A controls and explains why each control has been included
or excluded. It shows that these decisions were made consciously, not by
default.

ISO/IEC 27001 also provides a strong foundation for many NIS2
requirements, but it does not guarantee full compliance — the
cross-framework analysis is covered in Deliverable 03.

## Scope and limits of this exercise

This is a didactic exercise on a fictional company, not consulting work.

I had no real documents or data to work from, so for each control I tried
to reach the conclusion that would be realistic for a comparable company:
given a fintech of this size, with this technology and this stage of its
ISMS, which controls would apply, what state would they realistically be
in, who would own them, and what kind of evidence would support them.

The Evidence / Reference column therefore indicates the **type of
evidence expected** for each control — a policy, a procedure, a
configuration or a record — rather than documents that physically exist.
In a real ISMS every reference would point to an actual document under
document control (ISO/IEC 27001 Clause 7.5), and each one would be
verified.

What I wanted to show here is that I understand how an ISMS holds
together: how context, risk, controls, ownership and evidence connect.
The rest comes from working with a real organization.

## Next step in the portfolio

➡️ Deliverable 02 — Risk Assessment & Risk Register

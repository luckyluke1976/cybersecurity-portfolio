# Deliverable 02 — Statement of Applicability (ISO/IEC 27001:2022)

## What this is

A Statement of Applicability (SoA) for **VindobonaPay GmbH**, a fictional
Vienna-based licensed payment institution (~80 employees) used as the case
study across this whole portfolio.

The document uses the **93 controls of ISO/IEC 27001:2022 Annex A as a
reference set** and documents their applicability to the defined
organization: whether each control applies, why, its implementation
status, owner, supporting evidence and open remediation actions.

> ⚠️ **Assumptions and limitations**
> VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used. Control applicability,
> implementation status and remediation actions are illustrative
> assessments based on the defined scenario — they do not represent
> audit findings or work performed for a real organization.
>
> Control descriptions have been independently paraphrased for
> educational purposes. No ISO/IEC standard text is reproduced in this
> repository.

## Assumptions

The decisions in this SoA are based on the following scenario:

- Fictional company, built for learning purposes
- Licensed payment institution supervised by the Austrian FMA
- Cloud-first infrastructure (Microsoft 365 + Azure), minimal on-premises
  footprint (one server room in the Vienna office)
- All software is developed in-house
- Payroll is outsourced to an external provider
- Hybrid work model (office in Vienna + remote)
- The company processes payment and customer data

Full scenario — company profile, roles, technology and current security
posture: [00 — Organization Context](../00-organization-context/README.md).

## Methodological note on portfolio numbering

The portfolio numbering reflects publication order rather than the formal
ISMS implementation sequence. In ISO/IEC 27001 the SoA is an output of the
risk treatment process (Clause 6.1.3): risks are assessed, treatment
options are selected, necessary controls are determined and then compared
against Annex A. This SoA was finalized and updated using the risk
assessment documented in Deliverable 02.

## What's inside

**File:** [`VindobonaPay_SoA.pdf`](./VindobonaPay_SoA.pdf)

- **Statement of Applicability:** all 93 Annex A controls with:
  - Applicable? (Yes / No)
  - Justification for inclusion or exclusion
  - Implementation status (Implemented / Partially implemented / Planned),
    color-coded
  - Control owner
  - Related Risk ID (linked to the Risk Register — Deliverable 02)
  - Expected Evidence / Reference (policy, procedure or configuration that
    would support the control)
  - Remediation action with target date (for controls not yet fully
    implemented)
- **Summary page:** applicable and excluded controls, implementation
  status and open remediation actions.

The owner, expected evidence, remediation and target-date fields are
practical portfolio extensions. ISO/IEC 27001 requires the SoA to document
the necessary controls, the justification for their inclusion, their
implementation status and the justification for any exclusion — the
remaining fields would normally live in a risk treatment plan or an action
tracker.

## Key decisions

- **A.8.30 was assessed as not applicable.**
  Under the defined scenario, software development is performed entirely
  by internal personnel and no development activities are outsourced.
  The exclusion and its justification are documented in the SoA.

- **92 Annex A controls were assessed as applicable**, based on the
  organization's business context, information security risks, regulatory
  exposure and reliance on cloud and third-party services. The high number
  is a consequence of the scenario rather than a precautionary choice: a
  regulated payment institution processing cardholder and personal data
  has broad legal, contractual and regulatory obligations, and the Vienna
  office — however small — keeps the physical and environmental controls
  in scope. Outsourced development is the only structural exclusion the
  context supports.

- **Implementation is still in progress.**
  Approximately 60% of applicable controls are assessed as fully
  implemented under the fictional scenario. The remaining controls are
  partially implemented or planned, with owners and remediation actions
  assigned.

- **The Risk ID column links the SoA to the Risk Register (v2.0).**
  Where applicable, the Risk ID column links controls to the risks they
  treat (R-01 to R-16, see Deliverable 02). Controls without a direct Risk
  ID support the ISMS as baseline, legal, regulatory, contractual or
  business-required controls. This update reflects how an SoA evolves in
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
given a payment institution of this size, with this technology and this
stage of its ISMS, which controls would apply, what state would they
realistically be in, who would own them, and what kind of evidence would
support them.

The Expected Evidence / Reference column therefore indicates the **type of
evidence expected** for each control — a policy, a procedure, a
configuration or a record — rather than documents that physically exist.
In a real ISMS every reference would point to an actual document under
document control (ISO/IEC 27001 Clause 7.5), and each one would be
verified.

What I wanted to show here is that I understand how an ISMS holds
together: how context, risk, controls, ownership and evidence connect.
This exercise demonstrates the methodology and reasoning behind a SoA; in
a real organization, the assumptions and expected evidence would be
validated through stakeholder interviews, document review and technical
verification.

## Next step in the portfolio

➡️ Deliverable 02 — Risk Assessment & Risk Register

# Deliverable 02 — Risk Assessment & Risk Register (ISO/IEC 27001)

## What this is

A risk assessment and risk register for **VindobonaPay GmbH**, the same
fictional Vienna-based fintech used across this whole portfolio.

The risk assessment identifies the organization's main information
security risks, scores them before and after existing controls, and
defines how each risk is treated. The result feeds directly into the
Statement of Applicability (Deliverable 01): each risk is linked to the
Annex A controls that treat it.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used.

## Methodology

- **Asset-based approach**, inspired by ISO/IEC 27005 and NIST SP 800-30
  (simplified to stay realistic for an 80-person company).
- Each risk is described as: **asset → threat → vulnerability →
  consequence**.
- Scoring uses a **5×5 matrix**: Likelihood (1–5) × Impact (1–5) =
  Risk score (1–25), grouped into four levels:
  - 1–4 Low
  - 5–9 Medium
  - 10–15 High
  - 16–25 Critical
- **Both inherent and residual risk are evaluated.** Inherent scores
  represent exposure before considering controls. Residual scores
  reflect the current environment, including controls that are only
  partially implemented (see Deliverable 01).
- Each risk receives a **treatment decision**: Mitigate, Accept,
  Transfer or Avoid. The decision is supported by a treatment action,
  a risk owner, an action owner, a target date and a status.

## What's inside

**File:** [`VindobonaPay_Risk_Register.pdf`](./VindobonaPay_Risk_Register.pdf)

- **Risk Register:** 16 risks (R-01 to R-16) covering the payment
  platform, customer data, identity and access, endpoints, cloud
  infrastructure, suppliers, people and regulatory compliance. For each
  risk:
  - Asset, risk description and consequence
  - Inherent likelihood, impact and score (color-coded)
  - Existing controls, with ISO/IEC 27001 Annex A references
  - Residual likelihood, impact and score (color-coded)
  - Treatment decision and action (or acceptance rationale)
  - Risk owner and action owner
  - Target date and status
- **Risk matrix:** two 5×5 heat maps showing where the 16 risks sit —
  inherent vs. residual.
- **Summary:** risks by inherent level, by residual level and by
  treatment decision (calculated automatically).

## Key decisions

- **Inherent and residual risk are kept separate.** Without this
  distinction the effect of existing controls would not be verifiable.
  After considering existing controls, no risk remains at Critical
  residual level — but two risks stay High and drive the main
  remediation work.

- **Existing controls are separated from treatment actions.** Existing
  controls explain the residual score; treatment actions describe what
  still needs to be done. The two are not mixed.

- **Not every risk is mitigated.** Three risks are accepted and one is
  transferred. Each acceptance includes a short rationale, the approver
  (risk acceptance is a management decision, not an analyst decision)
  and a review date.

- **Risk Owner and Action Owner are different roles.** The risk owner
  is accountable for the risk and accepts the residual level; the
  action owner is responsible for implementing the treatment action.

- **Risk IDs connect the portfolio.** The IDs in this register are the
  ones referenced in the SoA. With this deliverable complete, the SoA
  is updated to v2.0 with the Risk ID column populated.

## Why it matters

Risk assessment is one of the foundations of an ISMS: controls should be
selected in response to identified risks, legal requirements and
business needs — not applied as a generic checklist.

This register shows the complete decision chain:

**asset → threat → vulnerability → consequence → inherent risk →
existing controls → residual risk → treatment → owner**

## Next step in the portfolio

➡️ Deliverable 03 — Control Mapping Matrix (ISO 27001 ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0)

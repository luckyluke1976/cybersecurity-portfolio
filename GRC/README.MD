# ⚖️ Governance, Risk & Compliance

Applying a legal + finance background to information security governance.
GRC deliverables built around ISO/IEC 27001, NIS2 and DORA.

All deliverables use the same fictional case study: **VindobonaPay GmbH**,
a Vienna-based fintech (~80 employees, Microsoft 365 + Azure, hybrid work,
payment data processing). The full scenario — company profile, roles,
technology and current security posture — is described in
[00 — Organization Context](./00-organization-context/README.md), which is
the basis for every decision in the deliverables below.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. No real client data is used.

## 📑 Deliverables

| # | Deliverable | Framework | README | PDF |
|---|------------|-----------|--------|-----|
| 00 | Organization Context (scenario) | ISO/IEC 27001 Clause 4 | [📄 README](./00-organization-context/README.md) | — |
| 01 | Statement of Applicability (SoA) | ISO/IEC 27001 | [📄 README](./01-statement-of-applicability/README.md) | [📕 PDF](./01-statement-of-applicability/VindobonaPay_SoA.pdf) |
| 02 | Risk Assessment & Risk Register | ISO/IEC 27001 / NIST SP 800-30 | [📄 README](./02-risk-assessment-risk-register/README.md) | [📕 PDF](./02-risk-assessment-risk-register/VindobonaPay_Risk_Register.pdf) |
| 03 | Control Mapping Matrix (ISO ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0) | Multi-framework | 🔜 | 🔜 |
| 04 | NIS2 Gap Analysis | NIS2 (EU 2022/2555) | 🔜 | 🔜 |
| 05 | DORA Compliance Mapping | DORA (EU 2022/2554) | 🔜 | 🔜 |
| 06 | Control Testing & Evidence Automation | ISO 27001 / audit practice | 🔜 | 🔜 |

## 🧭 Approach

- **Context first.** The organization context (00) defines the company,
  its regulatory exposure and its current security posture. Every
  applicability decision, risk score and control owner in the following
  deliverables is derived from it.
- **One scenario, multiple frameworks** — every deliverable refers to the
  same organization, scope and risk context, as in real GRC work.
- **Framework overlap is leveraged, not assumed.** ISO/IEC 27001 provides
  a strong foundation for many NIS2 requirements, but does not guarantee
  full compliance. DORA adds financial-sector-specific obligations that
  go beyond Annex A.
- **Controls are tested, not just documented.** Deliverable 06 covers
  control testing, evidence collection and a small Python automation.

## 🤖 Note on tooling and AI use

This portfolio was produced with the support of an AI assistant
(Claude, Anthropic), used the way a GRC analyst would use any
productivity tool: drafting, structuring documents and speeding up
repetitive work such as building tables and formatting deliverables.

The scenario, the applicability and risk decisions, the control
ownership model and the priorities in this portfolio are my own. Every
statement in these documents is one I can explain and defend, and the
AI-assisted drafts were reviewed and corrected against the requirements
of ISO/IEC 27001, NIS2 and DORA.

Being explicit about this is deliberate: AI tools are already part of
day-to-day work in governance and compliance, and the relevant skill is
using them under review and accountability — not pretending they are
not used.

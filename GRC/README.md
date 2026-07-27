# ⚖️ Governance, Risk & Compliance

Applying a legal + finance background to information security governance.
GRC deliverables built around ISO/IEC 27001, NIS2 and DORA.

All deliverables use the same fictional case study: **VindobonaPay GmbH**,
a Vienna-based licensed payment institution (~80 employees, Microsoft 365 +
Azure, hybrid work) providing payment services to e-commerce merchants
through a proprietary SaaS platform.

**Regulatory landscape:** DORA, GDPR, PSD2/ZaDiG 2018; NIS2 included for
comparative compliance mapping.

The full scenario — company profile, roles, technology and current security
posture — is described in
[00 — Organization Context](./00-organization-context/README.md), which is
the basis for every decision in the deliverables below.

> ⚠️ **Assumptions and limitations**
> VindobonaPay GmbH is a fictional company created for educational purposes.
> No real client data is used. Control applicability, implementation status,
> maturity assessments and risk scores are based on fictional but realistic
> assumptions: they are illustrative and do not represent audit findings or
> work performed for a real organization.

## 📑 Deliverables

| # | Deliverable | Framework | README | PDF |
|---|------------|-----------|--------|-----|
| 00 | Organization Context (scenario) | Supports ISO/IEC 27001 Clause 4 | [📄 README](./00-organization-context/README.md) | — |
| 01 | Statement of Applicability (SoA) | ISO/IEC 27001 | [📄 README](./01-statement-of-applicability/README.md) | [📕 PDF](./01-statement-of-applicability/VindobonaPay_SoA.pdf) |
| 02 | Risk Assessment & Risk Register | ISO/IEC 27001 / NIST SP 800-30 | [📄 README](./02-risk-assessment-risk-register/README.md) | [📕 PDF](./02-risk-assessment-risk-register/VindobonaPay_Risk_Register.pdf) |
| 03 | Control Mapping Matrix (ISO ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0) | Multi-framework | [📄 README](./03-control-mapping/README.md) | [📕 PDF](./03-control-mapping/VindobonaPay_Control_Mapping.pdf) |
| 04 | NIS2 Applicability & Gap Analysis | NIS2 (EU 2022/2555) | [📄 README](./04-nis2-gap-analysis/README.md) | [📕 PDF](./04-nis2-gap-analysis/VindobonaPay_NIS2_Gap_Analysis.pdf) |
| 05 | DORA Compliance Mapping | DORA (EU 2022/2554) | [📄 README](./05-dora-compliance-mapping/README.md) | [📕 PDF](./05-dora-compliance-mapping/VindobonaPay_DORA_Mapping.pdf) |
| 06 | Control Testing & Evidence Automation | ISO 27001 / audit practice | [📄 README](./06-control-testing-evidence/README.md) | [📕 PDF](./06-control-testing-evidence/VindobonaPay_Control_Testing.pdf) |

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
  go beyond Annex A. For financial entities DORA applies as *lex specialis*.
- **Controls are tested, not just documented.** Deliverable 06 covers
  control testing, evidence collection and a small Python automation.

---

<sub>AI tools were used for drafting, formatting and repetitive tasks. All assumptions, risk decisions and compliance mappings were reviewed and remain the author's responsibility.</sub>

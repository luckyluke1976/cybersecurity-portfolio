# 00 — Organization Context: VindobonaPay GmbH

## Purpose of this document

This document defines the fictional company used across **all
deliverables in this portfolio**. Every decision in the Statement of
Applicability (Deliverable 01), the Risk Register (Deliverable 02) and
the following deliverables is derived from the context described here.

In a real ISMS this corresponds to **ISO/IEC 27001 Clause 4 — Context of
the organization**: before assessing risks or selecting controls, you
need to understand the organization itself.

> ⚠️ VindobonaPay GmbH is a fictional company created for educational
> purposes. Any similarity to real companies is coincidental. No real
> client data is used.

## 1. Company profile

| | |
|---|---|
| **Name** | VindobonaPay GmbH |
| **Founded** | 2019 |
| **Headquarters** | Vienna, Austria |
| **Employees** | ~80 |
| **Business** | Payment services for e-commerce merchants (SaaS platform) |
| **Customers** | Online merchants in Austria and Germany |
| **Supervision** | Austrian Financial Market Authority (FMA) |
| **Key regulations** | DORA, NIS2, GDPR, PSD2 |

The company processes **payment transactions and customer personal
data**, which makes information security a core business requirement,
not an IT afterthought.

## 2. Organization

Roles referenced in the SoA and in the Risk Register:

- **CEO / Management** — overall accountability, approves policies
- **CFO** — finance, risk acceptance for financial exposure
- **COO** — operations, business continuity
- **CTO** — technology strategy, owns the payment platform
- **CISO** — hired in 2025 to build the ISMS (reports to the CEO)
- **IT Manager** — infrastructure, Microsoft 365, endpoints, identity
- **Head of Engineering** — in-house development of the payment platform
- **Compliance Officer** — regulatory obligations, supplier contracts
- **HR Manager** — screening, training, disciplinary process
- **Office Manager** — physical security of the Vienna office

The security team is small (CISO + support from IT), which is realistic
for a company of this size: many controls are owned by people who also
have other responsibilities.

## 3. Technology environment

- **Cloud-first**: Microsoft 365 for collaboration, Azure for the
  payment platform (availability zones, Azure Backup, Defender)
- **Identity**: Microsoft Entra ID with MFA and Conditional Access
- **Endpoints**: company laptops managed via Intune (MDM), full-disk
  encryption, EDR (Microsoft Defender for Endpoint)
- **Development**: 100% in-house (no outsourced development), GitHub
  private repositories, CI pipeline with SAST
- **Outsourced services**: payroll (external provider), some ICT
  services (cloud and network providers)
- **Work model**: hybrid (Vienna office + remote)
- **On-premises footprint**: minimal — one small server room in the
  Vienna office

## 4. Current security posture (snapshot)

The ISMS program started in 2025 when the CISO was hired. After about
one year, the situation is **realistic for a company mid-way through
the journey**: some areas are mature, others are still being built.
This snapshot is the basis for the implementation status in the SoA and
for the residual risk scores in the Risk Register.

| Area | Current state | Related Annex A controls |
|---|---|---|
| Security policies | Core policies approved (InfoSec, Access Control, Acceptable Use, Remote Working) | A.5.1, A.5.15, A.5.10, A.6.7 |
| Identity & authentication | MFA and Conditional Access enforced for all users; enrollment for privileged accounts almost complete | A.8.5, A.8.2 |
| Access management | RBAC in place on payment systems; access reviews still ad-hoc, quarterly cycle being formalized | A.8.3, A.5.18 |
| Segregation of duties | Matrix for payment operations in draft | A.5.3 |
| Endpoint protection | EDR on all endpoints; Intune MDM with hardening baseline and encryption | A.8.7, A.8.1, A.7.9 |
| Backup & resilience | Automated Azure backups with restore tests; availability zones for the platform | A.8.13, A.8.14 |
| Data classification | Policy in draft; Microsoft Purview labelling planned | A.5.12, A.5.13 |
| Logging & monitoring | Log collection partially centralized; alerting use cases being defined | A.8.15, A.8.16 |
| Vulnerability & patching | Monthly scans running; patch SLAs by severity not yet defined | A.8.8 |
| Cloud configuration | Endpoint baselines done; cloud hardening baselines in progress | A.8.9, A.5.23 |
| Secure development | Code review + SAST in pipeline; yearly pentest; formal SDLC procedure in progress | A.8.25, A.8.28, A.8.29 |
| Supplier management | Contracts have security clauses; structured supplier reviews and ICT supply chain procedure (DORA) still to be built | A.5.19, A.5.20, A.5.21, A.5.22 |
| Incident management | Incident Response Plan with triage criteria in place; regulatory reporting procedure (DORA timelines) to be defined | A.5.24, A.5.31 |
| Awareness | Yearly training + phishing simulations for all staff | A.6.3 |
| Business continuity | BCP in draft; RTO/RPO defined; first ICT continuity test planned | A.5.29, A.5.30 |

**In short:** identity, endpoints and backup are mature; data
classification, supplier management and monitoring are under
construction; DLP and ICT supply chain management are planned. This is
why the SoA shows ~60% of controls implemented — and why some risks in
the register keep a High residual score.

## 5. Why an ISMS (and why now)

- Enterprise merchants increasingly ask for **ISO/IEC 27001
  certification** in vendor assessments
- **DORA** applies to VindobonaPay as a financial entity: ICT risk
  management, incident reporting and third-party risk obligations
- **NIS2** and **GDPR** add further legal requirements
- A single security framework avoids answering every customer
  questionnaire from scratch

## How this document is used

| Deliverable | What it takes from this context |
|---|---|
| 01 — Statement of Applicability | Applicability decisions, implementation status, control owners |
| 02 — Risk Assessment & Risk Register | Assets, existing controls, residual scores, risk/action owners |
| 03 — Control Mapping Matrix | Regulatory exposure (ISO, NIS2, DORA, NIST CSF) |
| 04 — NIS2 Gap Analysis | Entity classification and current posture |
| 05 — DORA Compliance Mapping | Financial-entity obligations, ICT third-party landscape |
| 06 — Control Testing & Evidence | Systems and configurations to test (Entra ID, Intune, Azure) |

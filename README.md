# 🛡️ Cybersecurity Portfolio — Luca Danisi

> Payments, regulated finance and cybersecurity — focused on Governance, Risk & Compliance.
> Real-world payments experience combined with applied ISO/IEC 27001, DORA and NIS2 work.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/luca-danisi-5a80a227)
[![Credly](https://img.shields.io/badge/Credly-FF6B00?style=flat\&logo=credly\&logoColor=white)](https://www.credly.com/users/luca-danisi)
[![Hack The Box](https://img.shields.io/badge/HackTheBox-9FEF00?style=flat\&logo=hackthebox\&logoColor=black)](https://app.hackthebox.com/public/users/3050365)

---

## 💼 Professional Experience — Pronto Payments, Inc.

> Real-world payments experience, revisited through a modern GRC lens.

**Pronto Payments, Inc.** was a Miami-based fintech company that I co-founded and operated between **2008 and 2013**. The platform enabled residents and property owners to pay rent, condominium and HOA fees online using credit cards, debit cards and electronic checks.

As **Co-founder & Director**, I worked across the external payment-provider chain, merchant onboarding, transaction-security controls, payment-data flows and day-to-day operational dependencies.

The business relied on an acquiring bank, payment gateway, card and ACH processors, property-management integrations and outsourced IT providers. This gave me direct exposure to issues that I now analyse formally through GRC methods, including:

* ICT third-party and supplier risk
* Merchant and counterparty due diligence
* Security and fraud-control design
* Sensitive financial and personal-data flows
* Provider dependencies and concentration risk
* Operational resilience and substitutability
* Contractual and payment-industry security requirements

### Key retrospective observation

One of the most significant dependencies was at the acquiring layer. The payment gateway was technically replaceable, while the acquiring relationship was considerably less substitutable. The acquiring bank and one of the card processors also belonged to the same corporate group.

Today I would assess this through **concentration risk, substitutability and exit planning** — areas that are central to modern ICT third-party risk management.

> **Important scope note:** DORA, NIS2 and ISO/IEC 27001:2022 did not apply to Pronto Payments during its operating period. Any comparison with current GRC frameworks is retrospective and is used to demonstrate how I would assess the same risks today.

### Case study & historical material

📄 **[Pronto Payments — Retrospective GRC Case Study](Professional-Experience/Pronto-Payments/README.md)**
📕 **[Retrospective GRC Case Study — PDF](Professional-Experience/Pronto-Payments/Pronto_Payments_Retrospective_GRC_Case_Study.pdf)**
🖼️ **[Original marketing flyer — Front](Professional-Experience/Pronto-Payments/assets/pronto_mail_flyer_FRONT.jpg)**
🖼️ **[Original marketing flyer — Back](Professional-Experience/Pronto-Payments/assets/pronto_mail_flyer_BACK.jpg)**

---

## ⚖️ Governance, Risk & Compliance — Applied Portfolio

> A connected set of GRC deliverables applying ISO/IEC 27001, NIS2 and DORA to a realistic financial-services scenario.

The following deliverables use the same fictional case study — **VindobonaPay GmbH**, a Vienna-based licensed payment institution (~80 employees, Microsoft 365 + Azure, hybrid work) providing payment services to e-commerce merchants through a proprietary SaaS platform.

Using one consistent organization means that scope, risks, controls, ownership, evidence expectations and regulatory obligations all derive from the same business context.

The deliverables broadly follow the ISO/IEC 27001 implementation sequence: organizational context and risk assessment come first, followed by control selection, regulatory mapping, gap analysis and control testing.

**New here?** Start with **[01 — Risk Assessment](GRC/01-risk-assessment-risk-register/README.md)** for methodology, **[05 — DORA Compliance Mapping](GRC/05-dora-compliance-mapping/README.md)** for regulatory reasoning, and **[06 — Control Testing](GRC/06-control-testing-evidence/README.md)** for execution and evidence.

| #  | Deliverable                                               | Framework                       | README                                                      | PDF                                                                           |
| -- | --------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 00 | Organization Context                                      | Supports ISO/IEC 27001 Clause 4 | [📄 README](GRC/00-organization-context/README.md)          | —                                                                             |
| 01 | Risk Assessment & Risk Register                           | ISO/IEC 27001 / NIST SP 800-30  | [📄 README](GRC/01-risk-assessment-risk-register/README.md) | [📕 PDF](GRC/01-risk-assessment-risk-register/VindobonaPay_Risk_Register.pdf) |
| 02 | Statement of Applicability (SoA)                          | ISO/IEC 27001                   | [📄 README](GRC/02-statement-of-applicability/README.md)    | [📕 PDF](GRC/02-statement-of-applicability/VindobonaPay_SoA.pdf)              |
| 03 | Control Mapping Matrix (ISO ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0) | Multi-framework                 | [📄 README](GRC/03-control-mapping/README.md)               | [📕 PDF](GRC/03-control-mapping/VindobonaPay_Control_Mapping.pdf)             |
| 04 | NIS2 Applicability & Gap Analysis                         | NIS2 (EU 2022/2555)             | [📄 README](GRC/04-nis2-gap-analysis/README.md)             | [📕 PDF](GRC/04-nis2-gap-analysis/VindobonaPay_NIS2_Gap_Analysis.pdf)         |
| 05 | DORA Compliance Mapping                                   | DORA (EU 2022/2554)             | [📄 README](GRC/05-dora-compliance-mapping/README.md)       | [📕 PDF](GRC/05-dora-compliance-mapping/VindobonaPay_DORA_Mapping.pdf)        |
| 06 | Control Testing & Evidence Automation                     | ISO 27001 / audit practice      | [📄 README](GRC/06-control-testing-evidence/README.md)      | [📕 PDF](GRC/06-control-testing-evidence/VindobonaPay_Control_Testing.pdf)    |

**Scope and limits.** VindobonaPay is a teaching scenario, not client work. The documents show how the frameworks are applied to a realistic fact pattern. Evidence references describe the type of evidence a real implementation would produce and should not be interpreted as evidence from a real organization.

<sub>AI tools were used for drafting, formatting and repetitive tasks. Assumptions, risk decisions, control conclusions and compliance mappings were reviewed and remain my responsibility.</sub>

---

## 🏅 Certifications

| Certification                                     | Status     | Year |
| ------------------------------------------------- | ---------- | ---- |
| CompTIA Security+                                 | ✅ Achieved | 2026 |
| ISO/IEC 27001:2022 Provisional Implementer (PECB) | ✅ Achieved | 2026 |

<sub>PECB awards the Lead Implementer credential to candidates who also meet the required professional and ISMS project-experience criteria. Provisional Implementer is the credential matching my current documented experience.</sub>

---

## 🧰 Methods & Tooling

### ⚖️ GRC Practice

Methods applied across the VindobonaPay deliverables.

| Area                     | What I applied                                                                                                    |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Risk management          | Qualitative risk assessment — inherent and residual scoring, acceptance criteria, treatment actions and ownership |
| Control selection        | Statement of Applicability across all 93 ISO/IEC 27001:2022 Annex A controls                                      |
| Cross-framework analysis | ISO/IEC 27001, NIS2, DORA and NIST CSF 2.0 mapping                                                                |
| Compliance assessment    | Applicability assessment, gap identification and remediation tracking                                             |
| Third-party ICT risk     | Supplier dependencies, contractual controls, concentration risk and exit planning                                 |
| Control testing          | Design and operating effectiveness, sampling, evidence requirements and exception management                      |
| Evidence automation      | Python-based comparison of access-control evidence and structured test outputs                                    |
| Regulatory research      | EUR-Lex · ENISA · ESA technical standards (EBA / ESMA / EIOPA) · NIST · supervisory and CERT guidance             |

### 🔧 Technical Foundation

A GRC analyst who understands how systems fail, how attacks work and what technical evidence looks like can design better controls and ask more useful questions of security and operations teams.

The labs below come from my cybersecurity training and were performed in isolated environments against intentionally vulnerable targets. They support the governance work; they are not the primary focus of this portfolio.

<sub>

| Tool            | Category               | Usage                                                        |
| --------------- | ---------------------- | ------------------------------------------------------------ |
| Python          | Scripting & Automation | Compliance checks, evidence collection, data processing      |
| Nmap            | Reconnaissance         | Port scanning, service enumeration                           |
| Wireshark       | Network Analysis       | Packet capture and traffic analysis                          |
| Splunk          | SIEM                   | Log analysis, alert monitoring                               |
| Metasploit      | Exploitation           | Vulnerability exploitation framework                         |
| Meterpreter     | Post-Exploitation      | Remote shell and post-exploitation tooling                   |
| msfvenom        | Payload Generation     | Custom reverse shell payloads                                |
| Hydra           | Password Attacks       | Brute force SSH, FTP and web logins                          |
| BurpSuite       | Web Security           | HTTP interception and web application testing                |
| John the Ripper | Password Attacks       | Hash cracking                                                |
| Ettercap        | Network Attacks        | ARP poisoning and Man-in-the-Middle                          |
| Netcat          | Network Utility        | Shell connections and port testing                           |
| Telnet          | Network Utility        | Manual protocol interaction                                  |
| Gobuster        | Web Enumeration        | Directory and virtual-host enumeration                       |
| Nishang         | Post Exploitation      | PowerShell reverse shells                                    |
| GCC             | C Compiler             | Compiling vulnerable C programs for buffer-overflow analysis |

</sub>

---

## 🛡️ SOC Lab Reports (10/10)

<sub>

| #  | Title/README                                                                                | Tool                           | PDF Report                                                                         |
| -- | ------------------------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------- |
| 01 | [File Upload Exploit + BurpSuite](SOC/01-FileUpload/README.md)                              | BurpSuite                      | [📄 PDF](SOC/01-FileUpload/EXPLOIT%20FILE%20UPLOAD.pdf)                            |
| 02 | [XSS + SQL Injection](SOC/02-XSS-SQLi/README.md)                                            | DVWA                           | [📄 PDF](SOC/02-XSS-SQLi/XSS%20%2B%20SQL%20Injection.pdf)                          |
| 03 | [Password Cracking](SOC/03-PasswordCracking/README.md)                                      | John the Ripper                | [📄 PDF](SOC/03-PasswordCracking/Password%20craking%20and%20malware.pdf)           |
| 04 | [Authentication Cracking](SOC/04-AuthCracking/README.md)                                    | Hydra                          | [📄 PDF](SOC/04-AuthCracking/Authentication%20Cracking%20%28hydra%29.pdf)          |
| 05 | [ARP Poisoning & MITM Attack](SOC/ARP-Poisoning-Ettercap/README.md)                         | Ettercap, Wireshark            | [📄 PDF](SOC/ARP-Poisoning-Ettercap/Null%20session%20e%20Arp%20Poisoning.pdf)      |
| 06 | [Hacking with Metasploit – vsftpd 2.3.4](SOC/Hacking%20with%20Metasploit/README.md)         | Metasploit, Netcat             | [📄 PDF](SOC/Hacking%20with%20Metasploit/Hacking%20con%20Metasploit.pdf)           |
| 07 | [Black Box Penetration Test](SOC/Black%20Box/README.md)                                     | Nmap, Metasploit               | [📄 PDF](SOC/Black%20Box/Black%20Box.pdf)                                          |
| 08 | [MS17-010 Post-Exploitation & MySQL Misconfiguration](SOC/07-MS17010-Meterpreter/README.md) | Metasploit, Meterpreter, MySQL | [📄 PDF](SOC/07-MS17010-Meterpreter/Ms17-010%2BMeterpreter.pdf)                    |
| 09 | [Buffer Overflow in C](SOC/Buffer%20Overflow/README.md)                                     | GCC, C Language                | [📄 PDF](SOC/Buffer%20Overflow/Buffer%20Overflow.pdf)                              |
| 10 | [Incident Response & Malware Analysis](SOC/Incident-Response/README.md)                     | ANY.RUN, MITRE ATT&CK          | [📄 PDF](SOC/Incident-Response/Incident%20Response%20%26%20Malware%20Analysis.pdf) |

</sub>

---

## ⚔️ Hack The Box

<sub>15 machines completed — 8 main machines (Linux and Windows, Easy to Medium) and 7 Starting Point. Techniques include SMB and RCE exploitation, privilege escalation, web enumeration, SQL injection and service misconfiguration.</sub>

<sub>Full write-ups: **[HTB machine index →](HTB/README.md)** · [HTB profile](https://app.hackthebox.com/public/users/3050365)</sub>

---

## 🔬 Projects

| Project                                   | Description                                                                                                                                                             | README                                    |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [CyberLens](Projects/Cyberlens/README.md) | AI-powered security assistant for Even Realities G2 smart glasses. Real-time concept recognition, audio transcription and contextual definitions during study and labs. | [📖 README](Projects/Cyberlens/README.md) |


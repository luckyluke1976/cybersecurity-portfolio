# 🛡️ Cybersecurity Portfolio — Luca Danisi
> Bridging law, finance and cybersecurity — specializing in Governance, Risk & Compliance.  
> ISO/IEC 27001, DORA and NIS2 applied to a regulated EU financial entity, backed by hands-on technical labs.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luca-danisi-5a80a227)
[![Credly](https://img.shields.io/badge/Credly-FF6B00?style=flat&logo=credly&logoColor=white)](https://www.credly.com/users/luca-danisi)
[![Hack The Box](https://img.shields.io/badge/HackTheBox-9FEF00?style=flat&logo=hackthebox&logoColor=black)](https://app.hackthebox.com/public/users/3050365)

---
## ⚖️ Governance, Risk & Compliance

> Applying a legal + finance background to information security governance.  
> A connected set of GRC deliverables built around ISO/IEC 27001, NIS2 and DORA.

All deliverables use the same fictional case study — **VindobonaPay GmbH**, a Vienna-based licensed payment institution (~80 employees, Microsoft 365 + Azure, hybrid work) providing payment services to e-commerce merchants through a proprietary SaaS platform — so that scope, risks, controls, ownership and regulatory obligations all derive from one coherent context.

The deliverables follow the ISO/IEC 27001 implementation sequence: risks are assessed first, and the Statement of Applicability documents the controls selected to treat them.

**New here?** Start with **[01 — Risk Assessment](GRC/01-risk-assessment-risk-register/README.md)** for method, **[05 — DORA Compliance Mapping](GRC/05-dora-compliance-mapping/README.md)** for regulatory reasoning, and **[06 — Control Testing](GRC/06-control-testing-evidence/README.md)** for execution. The rest fills in the context.

| # | Deliverable | Framework | README | PDF |
|---|---|---|---|---|
| 00 | Organization Context (scenario) | Supports ISO/IEC 27001 Clause 4 | [📄 README](GRC/00-organization-context/README.md) | — |
| 01 | Risk Assessment & Risk Register | ISO/IEC 27001 / NIST SP 800-30 | [📄 README](GRC/01-risk-assessment-risk-register/README.md) | [📕 PDF](GRC/01-risk-assessment-risk-register/VindobonaPay_Risk_Register.pdf) |
| 02 | Statement of Applicability (SoA) | ISO/IEC 27001 | [📄 README](GRC/02-statement-of-applicability/README.md) | [📕 PDF](GRC/02-statement-of-applicability/VindobonaPay_SoA.pdf) |
| 03 | Control Mapping Matrix (ISO ↔ NIS2 ↔ DORA ↔ NIST CSF 2.0) | Multi-framework | [📄 README](GRC/03-control-mapping/README.md) | [📕 PDF](GRC/03-control-mapping/VindobonaPay_Control_Mapping.pdf) |
| 04 | NIS2 Applicability & Gap Analysis | NIS2 (EU 2022/2555) | [📄 README](GRC/04-nis2-gap-analysis/README.md) | [📕 PDF](GRC/04-nis2-gap-analysis/VindobonaPay_NIS2_Gap_Analysis.pdf) |
| 05 | DORA Compliance Mapping | DORA (EU 2022/2554) | [📄 README](GRC/05-dora-compliance-mapping/README.md) | [📕 PDF](GRC/05-dora-compliance-mapping/VindobonaPay_DORA_Mapping.pdf) |
| 06 | Control Testing & Evidence Automation | ISO 27001 / audit practice | [📄 README](GRC/06-control-testing-evidence/README.md) | [📕 PDF](GRC/06-control-testing-evidence/VindobonaPay_Control_Testing.pdf) |

**Scope and limits.** VindobonaPay is a teaching scenario, not client work. The documents show how the frameworks are applied to a realistic fact pattern; evidence references describe the type of evidence a real implementation would produce, not documents that physically exist.

<sub>AI tools were used for drafting, formatting and repetitive tasks. All assumptions, risk decisions and compliance mappings were reviewed and remain the author's responsibility.</sub>

---
## 🏅 Certifications
| Certification | Status | Year |
|---|---|---|
| CompTIA Security+ | ✅ Achieved | 2026 |
| ISO/IEC 27001:2022 Provisional Implementer (PECB) | ✅ Achieved | 2026 |

<sub>PECB awards the Lead Implementer credential only to candidates who also meet the documented ISMS project-experience requirement. Provisional Implementer is the tier that matches my current record; the higher tiers follow from project hours in a professional role.</sub>

---
## 🧰 Methods & Tooling

### ⚖️ GRC practice

Methods applied across the VindobonaPay deliverables. Working documents are produced in Markdown and Excel and published as PDF.

| Area | What I applied |
|---|---|
| Risk management | Qualitative risk assessment (Clause 6.1.2, NIST SP 800-30) — inherent and residual scoring, acceptance criteria, dual risk ownership |
| Control selection | Statement of Applicability across all 93 Annex A controls, with justification for inclusion and exclusion |
| Cross-framework analysis | Control mapping across ISO/IEC 27001, NIS2, DORA and NIST CSF 2.0, including the DORA *lex specialis* carve-out |
| Compliance assessment | Applicability determination and gap analysis with prioritised remediation actions |
| Control testing | Test design, sampling, exception logging, definition of expected evidence |
| Evidence automation | Python script reading access-control exports and producing structured test output |
| Regulatory sources | EUR-Lex · ENISA · ESA technical standards (EBA / ESMA / EIOPA) · NIST · national supervisory and CERT guidance |

### 🔧 Technical foundation

A GRC analyst who understands how an exploit works writes better controls and asks a SOC for the right evidence. The labs below come from my cybersecurity training and were run in an isolated environment against intentionally vulnerable targets — they support the governance work, they are not the focus of it.

<sub>

| Tool | Category | Usage |
|---|---|---|
| Python | Scripting & Automation | Compliance checks, evidence collection, data processing |
| Nmap | Reconnaissance | Port scanning, service enumeration |
| Wireshark | Network Analysis | Packet capture and traffic analysis |
| Splunk | SIEM | Log analysis, alert monitoring |
| Metasploit | Exploitation | Vulnerability exploitation framework |
| Meterpreter | Post-Exploitation | Remote shell and post-exploitation tooling |
| msfvenom | Payload Generation | Custom reverse shell payloads |
| Hydra | Password Attacks | Brute force SSH, FTP, web logins |
| BurpSuite | Web Security | HTTP interception, web app testing |
| John the Ripper | Password Attacks | Hash cracking |
| Ettercap | Network Attacks | ARP Poisoning, Man-in-the-Middle |
| Netcat | Network Utility | Shell connections, port testing |
| Telnet | Network Utility | Manual protocol interaction |
| Gobuster | Web Enumeration | Directory and vhost brute force |
| Nishang | Post Exploitation | PowerShell reverse shells |
| GCC | C Compiler | Compiling vulnerable C programs for buffer overflow analysis |

</sub>

---
## 🛡️ SOC Lab Reports (10/10)

<sub>

| # | Title/README | Tool | PDF Report |
|---|---|---|---|
| 01 | [File Upload Exploit + BurpSuite](SOC/01-FileUpload/README.md) | BurpSuite | [📄 PDF](SOC/01-FileUpload/EXPLOIT%20FILE%20UPLOAD.pdf) |
| 02 | [XSS + SQL Injection](SOC/02-XSS-SQLi/README.md) | DVWA | [📄 PDF](SOC/02-XSS-SQLi/XSS%20%2B%20SQL%20Injection.pdf) |
| 03 | [Password Cracking](SOC/03-PasswordCracking/README.md) | John the Ripper | [📄 PDF](SOC/03-PasswordCracking/Password%20craking%20and%20malware.pdf) |
| 04 | [Authentication Cracking](SOC/04-AuthCracking/README.md) | Hydra | [📄 PDF](SOC/04-AuthCracking/Authentication%20Cracking%20(hydra).pdf) |
| 05 | [ARP Poisoning & MITM Attack](SOC/ARP-Poisoning-Ettercap/README.md) | Ettercap, Wireshark | [📄 PDF](SOC/ARP-Poisoning-Ettercap/Null%20session%20e%20Arp%20Poisoning.pdf) |
| 06 | [Hacking with Metasploit – vsftpd 2.3.4](SOC/Hacking%20with%20Metasploit/README.md) | Metasploit, Netcat | [📄 PDF](SOC/Hacking%20with%20Metasploit/Hacking%20con%20Metasploit.pdf) |
| 07 | [Black Box Penetration Test](SOC/Black%20Box/README.md) | Nmap, Metasploit | [📄 PDF](SOC/Black%20Box/Black%20Box.pdf) |
| 08 | [MS17-010 Post-Exploitation & MySQL Misconfiguration](SOC/07-MS17010-Meterpreter/README.md) | Metasploit, Meterpreter, MySQL | [📄 PDF](SOC/07-MS17010-Meterpreter/Ms17-010%2BMeterpreter.pdf) |
| 09 | [Buffer Overflow in C](SOC/Buffer%20Overflow/README.md) | GCC, C Language | [📄 PDF](SOC/Buffer%20Overflow/Buffer%20Overflow.pdf) |
| 10 | [Incident Response & Malware Analysis](SOC/Incident-Response/README.md) | ANY.RUN, MITRE ATT&CK |[📄 PDF](SOC/Incident-Response/Incident%20Response%20%26%20Malware%20Analysis.pdf) |

</sub>

---
## ⚔️ Hack The Box

<sub>15 machines completed — 8 main machines (Linux and Windows, Easy to Medium) and 7 Starting Point. Techniques span SMB and RCE exploitation, privilege escalation, web enumeration, SQL injection and service misconfiguration.</sub>

<sub>Full write-ups: **[HTB machine index →](HTB/README.md)**  ·  [HTB profile](https://app.hackthebox.com/public/users/3050365)</sub>

---
## 🔬 Projects

| Project | Description | README |
|---|---|---|
| [CyberLens](Projects/Cyberlens/README.md) | AI-powered security assistant for Even Realities G2 smart glasses. Real-time concept recognition, audio transcription and contextual definitions during study and labs. | [📖 README](Projects/Cyberlens/README.md) |
| 07 | [Black Box Penetration Test](SOC/Black%20Box/README.md) | Nmap, Metasploit | [📄 PDF](SOC/Black%20Box/Black%20Box.pdf) |
| 08 | [MS17-010 Post-Exploitation & MySQL Misconfiguration](SOC/07-MS17010-Meterpreter/README.md) | Metasploit, Meterpreter, MySQL | [📄 PDF](SOC/07-MS17010-Meterpreter/Ms17-010%2BMeterpreter.pdf) |
| 09 | [Buffer Overflow in C](SOC/Buffer%20Overflow/README.md) | GCC, C Language | [📄 PDF](SOC/Buffer%20Overflow/Buffer%20Overflow.pdf) |
| 10 | [Incident Response & Malware Analysis](SOC/Incident-Response/README.md) | ANY.RUN, MITRE ATT&CK |[📄 PDF](SOC/Incident-Response/Incident%20Response%20%26%20Malware%20Analysis.pdf) |

</sub>

---
## ⚔️ Hack The Box

<sub>15 machines completed — 8 main machines (Linux and Windows, Easy to Medium) and 7 Starting Point. Techniques span SMB and RCE exploitation, privilege escalation, web enumeration, SQL injection and service misconfiguration.</sub>

<sub>Full write-ups: **[HTB machine index →](HTB/README.md)**  ·  [HTB profile](https://app.hackthebox.com/public/users/3050365)</sub>

---
## 🔬 Projects

| Project | Description | README |
|---|---|---|
| [CyberLens](Projects/Cyberlens/README.md) | AI-powered security assistant for Even Realities G2 smart glasses. Real-time concept recognition, audio transcription and contextual definitions during study and labs. | [📖 README](Projects/Cyberlens/README.md) |

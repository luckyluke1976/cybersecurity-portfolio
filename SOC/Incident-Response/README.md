# SOC Lab 10 – Incident Response & Malware Analysis

**Difficulty:** Intermediate  
**Status:** Completed ✅

---

## Summary

This lab covers two exercises. The first one focuses on incident response procedures applied to a compromised database server (System B), following CSIRT methodology. The second one is a malware analysis exercise using the ANY.RUN sandbox platform to analyse two suspicious files and map their behaviour to the MITRE ATT&CK framework.

---

## Tools Used

- **Firewall** — perimeter traffic blocking
- **CSIRT Procedures** — standard incident response methodology
- **ANY.RUN** — online sandbox for dynamic malware analysis
- **MITRE ATT&CK Framework** — attack technique classification

---

## Part 1 – Incident Response

### Scenario
System B (a database server) was compromised by an external attacker who breached the network perimeter via the Internet. The CSIRT team must isolate the system, remove it from the network and sanitise the disks before disposal.

### Isolation of System B
- Physically disconnected from the internal network to stop lateral movement
- Firewall rules created to block all inbound/outbound traffic from System B's IP
- System logs, active processes and RAM dump collected before any other action

### Removal of System B
- Controlled shutdown performed
- OS reinstalled from scratch on clean hardware
- Data restored from a pre-compromise backup
- Full malware scan performed before reconnecting to the network

### Data Sanitisation
| Level | Method | When to Use |
|---|---|---|
| CLEAR | Overwrite with zeros (`dd` on Linux) | Disk reused within same organisation |
| PURGE | Multiple overwrite or crypto erasure (`shred`, SSD wipe) | Disk decommissioned or transferred |
| DESTROY | Physical destruction (shredding, degaussing) | Highly sensitive data, no reuse possible |

---

## Part 2 – Malware Analysis with ANY.RUN

### Case 1 — DNS_Changer.ps1
- **Verdict:** Suspicious (65/100)
- **Type:** PowerShell script
- **Behaviour:** Executes with `-ExecutionPolicy Bypass`, reads Internet settings, attempts to create local accounts
- **MITRE ATT&CK:**
  - T1059.001 — PowerShell execution with policy bypass
  - T1012 — Registry query for Internet settings
  - T1136.001 — Local account creation via PowerShell
- **Risk:** Likely a DNS Changer — redirects victim traffic to fake or malicious sites

### Case 2 — procexp.exe
- **Verdict:** Malicious (100/100)
- **Type:** Executable masquerading as Sysinternals Process Explorer
- **Behaviour:** Self-rewriting, installs hidden system driver, creates scheduled tasks for persistence, communicates with C&C on non-standard ports
- **MITRE ATT&CK:**
  - Execution — scheduled tasks and malicious file execution
  - Persistence — scheduled tasks survive reboot
  - Defense Evasion — masquerading, sandbox evasion, obfuscated files
  - Discovery — collects GUID, computer name, language
  - C&C — non-standard port communication with remote command server
- **Risk:** Advanced malware with full evasion, persistence and remote control capabilities

---

## What I Learned

- CSIRT incident response follows a precise sequence: isolate → preserve evidence → remove → restore → verify
- The choice between Clear, Purge and Destroy depends on data sensitivity and hardware destination
- ANY.RUN allows fast dynamic analysis of suspicious files without risking your own machine
- MITRE ATT&CK gives a common language to classify and communicate what malware actually does
- A file scoring 100/100 malicious on ANY.RUN hiding as a legitimate tool is a classic masquerading attack

---

## Disclaimer
This lab was performed in a controlled environment for educational purposes only.

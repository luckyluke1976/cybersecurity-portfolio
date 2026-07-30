# ⚔️ Hack The Box — Machine Write-ups

<sub>[← Back to portfolio](../README.md)  ·  [HTB profile](https://app.hackthebox.com/public/users/3050365)</sub>

15 machines completed. Each write-up documents enumeration, the vulnerability exploited, the exploitation path and, where applicable, privilege escalation.

All work was carried out on Hack The Box, a legal training platform providing intentionally vulnerable machines in an isolated lab environment.

---
## 🔴 Main Machines (8/8)

| # | Machine | OS | Difficulty | Technique |
|---|---|---|---|---|
| 01 | [Lame](Lame/README.md) | Linux | Easy | SMB exploitation, CVE-2007-2447 |
| 02 | [Blue](Blue/README.md) | Windows | Easy | MS17-010 EternalBlue |
| 03 | [Legacy](Legacy/README.md) | Windows | Easy | MS08-067 NetAPI |
| 04 | [Jerry](Jerry/README.md) | Windows | Easy | Tomcat default credentials, WAR upload |
| 05 | [Nibbles](Nibbles/README.md) | Linux | Easy | Web enumeration, Nibbleblog RCE, sudo misconfiguration |
| 06 | [Bounty](Bounty/README.md) | Windows | Medium | IIS web.config upload, SeImpersonatePrivilege |
| 07 | [Optimum](Optimum/README.md) | Windows | Easy | HttpFileServer RCE, MS16-032 |
| 08 | [Bastard](Bastard/README.md) | Windows | Medium | Drupal 7 Services RCE, MS15-051 |

---
## 🟢 Starting Point (7/7)

| # | Machine | OS | Difficulty | Technique |
|---|---|---|---|---|
| 01 | [Meow](Meow/README.md) | Linux | Very Easy | Telnet, anonymous login |
| 02 | [Redeemer](Redeemer/README.md) | Linux | Very Easy | Redis enumeration |
| 03 | [Appointment](Appointment/README.md) | Linux | Very Easy | SQL Injection |
| 04 | [Responder](Responder/README.md) | Windows | Very Easy | LFI, NTLMv2, WinRM |
| 05 | [Crocodile](Crocodile/README.md) | Linux | Very Easy | FTP anonymous, directory brute force |
| 06 | [Sequel](Sequel/README.md) | Linux | Very Easy | MySQL unauthenticated access |
| 07 | [Three](Three/README.md) | Linux | Very Easy | S3 bucket misconfiguration, PHP RCE |

---
## Why this sits alongside GRC work

Understanding how a control fails in practice makes for better control design and better audit questions. A vulnerability write-up shows what an attacker actually needed — an unpatched service, a default credential, an over-permissive privilege — which is the same evidence a compliance test looks for from the other direction.

<sub>[← Back to portfolio](../README.md)</sub>

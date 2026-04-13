# 🛡️ Cybersecurity Portfolio — Luca Danisi
> Practical cybersecurity portfolio targeting junior roles.  
> Includes offensive writeups (HTB) and defensive lab reports (SOC Analyst).
---
## 👤 About Me
Cybersecurity student currently pursuing **Cisco CCST Cybersecurity**, working towards **CompTIA Security+** and beyond.  
Passionate about both offensive and defensive security, with a focus on penetration testing and SOC analysis.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luca-danisi-5a80a227)
[![Credly](https://img.shields.io/badge/Credly-FF6B00?style=flat&logo=credly&logoColor=white)](https://www.credly.com/users/luca-danisi)
[![Hack The Box](https://img.shields.io/badge/HackTheBox-9FEF00?style=flat&logo=hackthebox&logoColor=black)](https://app.hackthebox.com/public/users/3050365)

---
## 🧰 Tools & Skills
| Tool | Category | Usage |
|---|---|---|
| Nmap | Reconnaissance | Port scanning, service enumeration |
| Wireshark | Network Analysis | Packet capture and traffic analysis |
| Splunk | SIEM | Log analysis, alert monitoring |
| Metasploit | Exploitation | Vulnerability exploitation framework |
| msfvenom | Payload Generation | Custom reverse shell payloads |
| Hydra | Password Attacks | Brute force SSH, FTP, web logins |
| BurpSuite | Web Security | HTTP interception, web app testing |
| John the Ripper | Password Attacks | Hash cracking |
| Ettercap | Network Attacks | ARP Poisoning, Man-in-the-Middle |
| Netcat | Network Utility | Shell connections, port testing |
| Telnet | Network Utility | Manual protocol interaction |
| Gobuster | Web Enumeration | Directory and vhost brute force |

---
## ⚔️ HTB Machines

### 🔴 Main Machines (5/8)
| # | Machine | OS | Difficulty | Technique |
|---|---|---|---|---|
| 01 | [Lame](HTB/Lame/README.md) | Linux | Easy | SMB exploitation, CVE-2007-2447 |
| 02 | [Blue](HTB/Blue/README.md) | Windows | Easy | MS17-010 EternalBlue |
| 03 | [Legacy](HTB/Legacy/README.md) | Windows | Easy | MS08-067 NetAPI |
| 04 | [Jerry](HTB/Jerry/README.md) | Windows | Easy | Tomcat default credentials, WAR upload |
| 05 | [Nibbles](HTB/Nibbles/README.md) | Linux | Easy | Web enumeration, Nibbleblog RCE, sudo misconfiguration |
| 06 | Bounty — coming soon | Windows | Medium | IIS, file upload bypass |
| 07 | Optimum — coming soon | Windows | Easy | HttpFileServer RCE |
| 08 | TBD | - | - | - |

---

### <sub>🟢 Starting Point</sub>

<sub>

| # | Machine | OS | Difficulty | Technique |
|---|---|---|---|---|
| 01 | [Meow](HTB/Meow/README.md) | Linux | Very Easy | Telnet, anonymous login |
| 02 | [Redeemer](HTB/Redeemer/README.md) | Linux | Very Easy | Redis enumeration |
| 03 | [Appointment](HTB/Appointment/README.md) | Linux | Very Easy | SQL Injection |
| 04 | [Responder](HTB/Responder/README.md) | Windows | Very Easy | LFI, NTLMv2, WinRM |
| 05 | [Crocodile](HTB/Crocodile/README.md) | Linux | Very Easy | FTP anonymous, directory brute force |
| 06 | [Sequel](HTB/Sequel/README.md) | Linux | Very Easy | MySQL unauthenticated access |
| 07 | [Three](HTB/Three/README.md) | Linux | Very Easy | S3 bucket misconfiguration, PHP RCE |

</sub>

---
## 🛡️ SOC Lab Reports (6/10)
| # | Title/README | Tool | PDF Report |
|---|---|---|---|
| 01 | [File Upload Exploit + BurpSuite](SOC/01-FileUpload/README.md) | BurpSuite | [📄 PDF](SOC/01-FileUpload/EXPLOIT%20FILE%20UPLOAD.pdf) |
| 02 | [XSS + SQL Injection](SOC/02-XSS-SQLi/README.md) | DVWA | [📄 PDF](SOC/02-XSS-SQLi/report.pdf) |
| 03 | [Password Cracking](SOC/03-PasswordCracking/README.md) | John the Ripper | [📄 PDF](SOC/03-PasswordCracking/report.pdf) |
| 04 | [Authentication Cracking](SOC/04-AuthCracking/README.md) | Hydra | [📄 PDF](SOC/04-AuthCracking/report.pdf) |
| 05 | [ARP Poisoning & MITM Attack](SOC/ARP-Poisoning-Ettercap/README.md) | Ettercap, Wireshark | [📄 PDF](SOC/ARP-Poisoning-Ettercap/report.pdf) |
| 06 | [Hacking with Metasploit – vsftpd 2.3.4](SOC/Hacking%20with%20Metasploit/README.md) | Metasploit, Netcat | [📄 PDF](SOC/Hacking%20with%20Metasploit/report.pdf) |
| 07 | Coming soon... | - | - |
| 08 | Coming soon... | - | - |
| 09 | Coming soon... | - | - |
| 10 | Coming soon... | - | - |

---
## 🏅 Certifications
| Certification | Status | Year |
|---|---|---|
| Cisco CCST Cybersecurity | 🔄 In progress | 2026 |
| CompTIA Security+ | 🗓️ Planned | 2026 |

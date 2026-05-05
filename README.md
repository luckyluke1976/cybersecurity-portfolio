# 🛡️ Cybersecurity Portfolio — Luca Danisi
> Building my path in cybersecurity, one lab at a time.  
> Hands-on projects and writeups — learning by doing, documenting everything.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luca-danisi-5a80a227)
[![Credly](https://img.shields.io/badge/Credly-FF6B00?style=flat&logo=credly&logoColor=white)](https://www.credly.com/users/luca-danisi)
[![Hack The Box](https://img.shields.io/badge/HackTheBox-9FEF00?style=flat&logo=hackthebox&logoColor=black)](https://app.hackthebox.com/public/users/3050365)

---
## 🏅 Certifications
| Certification | Status | Year |
|---|---|---|
| Cisco CCST Cybersecurity | 🔄 In progress | 2026 |
| CompTIA Security+ | 🗓️ Planned | 2026 |

---
## 🧰 Tools & Skills
| Tool | Category | Usage |
|---|---|---|
| Nmap | Reconnaissance | Port scanning, service enumeration |
| Wireshark | Network Analysis | Packet capture and traffic analysis |
| Splunk | SIEM | Log analysis, alert monitoring |
| Metasploit | Exploitation | Vulnerability exploitation framework |
| Meterpreter | Post-Exploitation | Remote shell, screenshot, keylogger, webcam |
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

---
## 🛡️ SOC Lab Reports (10/10)
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
| 10 | [Incident Response & Malware Analysis](SOC/Incident-Response/README.md) | ANY.RUN, MITRE ATT&CK | [📄 PDF](SOC/10-Incident-Response/Incident_Response_and_Malware_Analysis.pdf) |

---
## ⚔️ HTB Machines

### 🔴 Main Machines (8/8)
| # | Machine | OS | Difficulty | Technique |
|---|---|---|---|---|
| 01 | [Lame](HTB/Lame/README.md) | Linux | Easy | SMB exploitation, CVE-2007-2447 |
| 02 | [Blue](HTB/Blue/README.md) | Windows | Easy | MS17-010 EternalBlue |
| 03 | [Legacy](HTB/Legacy/README.md) | Windows | Easy | MS08-067 NetAPI |
| 04 | [Jerry](HTB/Jerry/README.md) | Windows | Easy | Tomcat default credentials, WAR upload |
| 05 | [Nibbles](HTB/Nibbles/README.md) | Linux | Easy | Web enumeration, Nibbleblog RCE, sudo misconfiguration |
| 06 | [Bounty](HTB/Bounty/README.md) | Windows | Medium | IIS web.config upload, SeImpersonatePrivilege |
| 07 | [Optimum](HTB/Optimum/README.md) | Windows | Easy | HttpFileServer RCE, MS16-032 |
| 08 | [Bastard](HTB/Bastard/README.md) | Windows | Medium | Drupal 7 Services RCE, MS15-051 |

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

## 🔬 Projects

| Project | Description | README | PDF |
|---|---|---|---|
| [CyberLens](Projects/CyberLens/README.md) | AI-powered security assistant for Even Realities G2 smart glasses. Real-time concept recognition, audio transcription and contextual definitions during study and labs. | [📖 README](Projects/CyberLens/README.md) | [📄 PDF](Projects/CyberLens/CyberLens.pdf) |

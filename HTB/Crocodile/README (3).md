# HTB - Crocodile

**Platform:** Hack The Box — Starting Point, Tier 1  
**OS:** Linux  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Crocodile is a Linux machine with an FTP server that allows anonymous login. By connecting anonymously, we download two files containing usernames and plaintext passwords. We then use Gobuster to find a hidden login page and authenticate with the recovered credentials to get the flag.

---

## Tools Used

- `nmap` — port scanning
- `ftp` — anonymous file download
- `gobuster` — directory brute force

---

## Steps

### 1. Port Scanning

```bash
nmap -sC -sV 10.129.50.80
```

Result:

```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
80/tcp open  http    Apache httpd 2.4.41 (Ubuntu)
```

Port 21 has FTP with anonymous login enabled. Port 80 is a web server.

### 2. FTP Anonymous Login

```bash
ftp 10.129.50.80
```

Logged in with username `anonymous` and no password. Found two files:

```
allowed.userlist
allowed.userlist.passwd
```

Downloaded both with `get`.

### 3. Reading the Files

```bash
cat allowed.userlist
cat allowed.userlist.passwd
```

Got a list of usernames and their passwords in plaintext, including `admin`.

### 4. Directory Brute Force

```bash
gobuster dir -u http://10.129.50.80 -w /usr/share/wordlists/dirb/common.txt
```

Found `/dashboard/` which redirects to `login.php`.

### 5. Web Login

Used credentials `admin` / `rKXM59ESxesUFHAd` on `http://10.129.50.80/dashboard/login.php`. Access granted — flag displayed on the dashboard.

---

## What I Learned

- Anonymous FTP access is a critical misconfiguration that can expose sensitive files.
- Credentials should never be stored in plaintext on publicly accessible services.
- Directory brute force can reveal hidden pages not linked from the main site.

---

## Remediation

- Disable anonymous FTP login
- Never store credentials in plaintext on accessible servers
- Implement strong authentication and account lockout on web login pages

---

## Flag

`c7110277ac44d78b6a9fff2232434d16`

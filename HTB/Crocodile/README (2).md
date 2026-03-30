# Crocodile — HackTheBox Writeup

**Difficulty:** Very Easy  
**OS:** Linux  
**Date:** 2026-03-30  

---

## Summary

Machine with FTP anonymous access enabled. Downloaded two files containing usernames and passwords in plaintext, then used them to log in to a web dashboard found via directory brute force.

---

## Tools Used

- Nmap
- FTP client
- Gobuster

---

## Steps

**1. Nmap scan**

```bash
nmap -sC -sV 10.129.50.80
```

Found two open ports:
- Port 21 — FTP vsftpd 3.0.3 (anonymous login allowed)
- Port 80 — Apache httpd 2.4.41

**2. FTP anonymous login**

```bash
ftp 10.129.50.80
```

Logged in as `anonymous` with no password. Found two files:
- `allowed.userlist`
- `allowed.userlist.passwd`

Downloaded both with `get`.

**3. Reading the files**

```bash
cat allowed.userlist
cat allowed.userlist.passwd
```

Got a list of usernames (aron, pwnmeow, egotisticalsw, admin, root) and their passwords in plaintext.

**4. Directory brute force**

```bash
gobuster dir -u http://10.129.50.80 -w /usr/share/wordlists/dirb/common.txt
```

Found `/dashboard/` which redirected to `login.php`.

**5. Web login**

Tried username `admin` with password `rKXM59ESxesUFHAd` — access granted. Flag visible on the dashboard.

---

## What I Learned

- FTP anonymous access is a critical misconfiguration — never leave it enabled in production.
- Sensitive files like userlist and passwords should never be stored on an FTP server.
- Directory brute force can reveal hidden pages not linked anywhere on the site.

---

## Remediation

- Disable anonymous FTP login
- Never store credentials in plaintext on publicly accessible services
- Implement account lockout and strong password policies on web login pages

---

## Flag

`c7110277ac44d78b6a9fff2232434d16`

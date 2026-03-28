# XSS and SQL Injection Exploitation Lab

## Overview
This lab demonstrates the successful exploitation of two common web application vulnerabilities in **DVWA (Damn Vulnerable Web Application)**:

- **Reflected XSS**
- **SQL Injection**

The goal of the exercise was to understand how insecure input handling can expose **session data** and **sensitive database information** in a vulnerable web application.

---

## Objective
To test and successfully exploit **Reflected XSS** and **SQL Injection** vulnerabilities in DVWA, showing how insecure input handling can expose session data and sensitive database information.

---

## Lab Environment
- **Attacker machine:** Kali Linux
- **Target machine:** Metasploitable 2
- **Target application:** DVWA
- **Network:** Internal lab network
- **Kali Linux IP:** `192.168.50.100`
- **Target IP:** `192.168.50.101`

---

## Tools Used
- Kali Linux
- Metasploitable 2
- DVWA
- Web Browser
- MySQL

---

## Technical Summary

### 1. Connectivity Check
A ping test confirmed that the attacker machine could communicate with the target machine inside the internal lab network.

### 2. DVWA Access and Setup
DVWA was accessed from the browser on Kali Linux using the target IP address. The application was configured with the security level set to **Low**.

### 3. Reflected XSS
A JavaScript payload was submitted in the Reflected XSS section of DVWA. The browser executed the payload and displayed an alert message, confirming the vulnerability.

### 4. Session Cookie Disclosure
A second XSS payload using `document.cookie` exposed the active session cookie in the browser, showing the risk of session hijacking.

### 5. SQL Injection
SQL Injection was tested by submitting crafted input in the **User ID** field. The application returned SQL errors, revealed backend information, and allowed the extraction of usernames and password hashes from the database.

---

## Results
The exploitation was successful for both vulnerabilities.

- **Reflected XSS** allowed JavaScript execution in the browser
- **Session cookie data** was exposed
- **SQL Injection** revealed database errors and backend details
- **Usernames and password hashes** were extracted from the database

---

## Issues Encountered
No major issues were encountered during the lab.

The main challenge was interpreting the application responses correctly and adjusting the payloads step by step during the exploitation process.

---

## Conclusion
This lab showed how **Reflected XSS** and **SQL Injection** can be exploited when user input is not properly validated or sanitized.

The exercise highlighted the importance of:

- input validation
- output sanitization
- secure query handling
- secure coding practices in web applications

---

## Screenshots
- Figure 1 – Connectivity check between Kali and Metasploitable
- Figure 2 – DVWA Login and Security Level Configuration
- Figure 3 – Reflected XSS Alert Execution
- Figure 4 – Session Cookie Disclosure via XSS
- Figure 5 – SQL Injection Error-Based Confirmation

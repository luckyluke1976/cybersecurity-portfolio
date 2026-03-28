# DVWA File Upload Exploitation Lab

This project shows how a file upload vulnerability in DVWA can be used to upload a PHP shell and execute commands on a Metasploitable2 machine.

The lab was carried out in a controlled environment using Kali Linux, DVWA, Metasploitable2, and Burp Suite.

## Objective

The goal of this exercise was to understand how an insecure file upload function can be exploited to gain remote command execution on a target machine.

## Lab Setup

- **Attacking machine:** Kali Linux
- **Target machine:** Metasploitable2
- **Web application:** DVWA
- **Tools used:** Burp Suite, Firefox, PHP shell

## What I Did

- Verified connectivity between the machines
- Accessed DVWA from Kali Linux
- Created a PHP shell file
- Uploaded the file through the DVWA upload function
- Executed commands remotely on the target machine
- Intercepted the HTTP request with Burp Suite
- Observed the transmitted data and session cookie

## Key Results

- The PHP shell was uploaded successfully
- Remote command execution was confirmed
- Basic system information was retrieved
- Sensitive file contents were accessed
- Burp Suite showed the request details in cleartext

## Files

- `EXPLOIT FILE UPLOAD.pdf` – full lab report

## Notes

This project was created for learning purposes in a local lab environment.

# Password Cracking with John the Ripper on DVWA

## Overview
This lab shows how password hashes can be extracted from a vulnerable web application through SQL Injection and then cracked offline with John the Ripper.

The test was performed in a controlled lab environment using DVWA hosted on Metasploitable 2 and Kali Linux as the attacker machine.

## Objective
To exploit a SQL Injection vulnerability in DVWA to extract user password hashes from the database and perform offline password cracking with John the Ripper in order to recover the corresponding plaintext passwords and understand the security weaknesses of unsalted MD5 hashing.

## Lab Environment
- **Attacker machine:** Kali Linux — `192.168.50.100`
- **Target machine:** Metasploitable 2 hosting DVWA — `192.168.50.101`
- **Network type:** Internal virtual network

## Tools Used
- Kali Linux
- Metasploitable 2
- DVWA
- Web Browser
- John the Ripper
- `hashes.txt` for storing extracted hashes

## Technical Walkthrough

### 1. Connectivity Check
The first step was to verify that Kali Linux could communicate with the target machine. A ping test confirmed that the two virtual machines were correctly connected through the internal lab network.

### 2. Access to DVWA
From the browser on Kali Linux, DVWA was opened using the target IP address. The application was accessed with the default credentials, and the security level was set to **Low** to allow the vulnerability to be tested in the lab.

### 3. SQL Injection to Extract Hashes
Inside the SQL Injection section of DVWA, a UNION-based payload was used to retrieve usernames and password hashes from the `users` table. This demonstrated that sensitive authentication data could be exposed through improper input validation.

### 4. Saving the Hashes
The extracted username and hash pairs were saved into a local file named `hashes.txt`. This file was then used as input for the offline cracking phase.

### 5. Password Cracking with John the Ripper
John the Ripper was executed against the hash file using the `raw-md5` format. The tool first used its default wordlist and then continued with incremental mode when needed. All five passwords were successfully recovered.

## Results
- Usernames and MD5 password hashes were extracted from DVWA
- The hashes were saved into `hashes.txt`
- John the Ripper successfully cracked all 5 passwords
- Most passwords were recovered through the default wordlist
- One password required incremental / brute-force mode
- The lab confirmed the weakness of storing passwords with unsalted MD5

## Issues Encountered During the Test
No major technical issues were encountered during the lab.

The main points that required attention were:
- setting the DVWA security level to **Low**
- saving the extracted hashes in the correct format
- identifying that one password could not be recovered through the default wordlist alone

## Security Takeaways
This lab highlights two important security issues:
- **SQL Injection** can expose sensitive backend data, including credential hashes
- **MD5 without salt** is not secure for password storage because it is fast and easy to crack offline

A secure system should use stronger password hashing algorithms such as **bcrypt** or **Argon2**, together with proper input validation to prevent SQL Injection.

## Conclusion
This lab demonstrated how a SQL Injection vulnerability can be used to extract password hashes from a web application database and how those hashes can then be cracked offline with John the Ripper. The successful recovery of all five plaintext passwords confirmed that storing credentials with unsalted MD5 is insecure and can be easily exploited.

## Screenshot Captions
- **Figure 1 – Successful connectivity test between Kali Linux and Metasploitable**
- **Figure 2 – DVWA login and security level configuration**
- **Figure 3 – SQL Injection used to extract usernames and password hashes**
- **Figure 4 – John the Ripper cracking the extracted MD5 hashes**

## Disclaimer
This project was carried out in a legal and controlled lab environment for educational purposes only.

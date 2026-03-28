# Authentication Cracking with Hydra

## Overview
This lab demonstrates how weak credentials can be recovered through brute-force and dictionary attacks against authentication services.

The test was performed in a controlled virtual environment using **Hydra** against **SSH** and **FTP** services configured on Kali Linux.

## Objective
To test the security of SSH and FTP authentication by performing controlled brute-force attacks with Hydra in a lab environment and demonstrating the risks of weak or dictionary-based passwords.

## Lab Environment
- **Lab machine:** Kali Linux — `192.168.50.100`
- **Services tested:** SSH on port `22` and FTP on port `21`
- **Network type:** Internal virtual network (`vtnet1`)
- **Test account:** `test_user`

## Tools Used
- Kali Linux
- Hydra
- OpenSSH service
- VSFTPD
- SecLists / password wordlists
- Custom short password list
- `test_user` test account

## Technical Walkthrough

### 1. Connectivity Check
The lab started with a connectivity check to confirm that the environment was working correctly. A ping test was performed to verify that the machine could communicate properly over the internal network before starting the authentication tests.

### 2. Creation of a Test Account
A dedicated user account named `test_user` was created on Kali Linux for the purpose of the exercise. This account was assigned the password `testpassword`, which was later used as the target credential during the brute-force tests.

### 3. SSH Service Setup and Validation
The SSH service was started on Kali Linux and its status was checked to confirm that it was active. After that, a manual SSH connection to `test_user@192.168.50.100` was performed to verify that the service was reachable and that authentication worked correctly before launching Hydra.

### 4. Wordlist Preparation and Hydra Execution Against SSH
Before running Hydra, password wordlists were prepared to provide candidate passwords for the attack. An initial attempt with a large password list and multiple parallel tasks caused instability, so the test was adjusted by using a shorter custom password list and limiting Hydra to a single task. Hydra was then used to brute-force the SSH service until valid credentials were found.

### 5. VSFTPD Installation and Configuration
The FTP service was prepared by installing and starting **VSFTPD** on Kali Linux. During this phase, it was necessary to account for the fact that VSFTPD was listening on IPv6 by default, so the configuration had to be adapted for the intended test setup.

### 6. Hydra Execution Against FTP
After the FTP service was active, Hydra was launched again against the FTP login interface using the same test account and the shorter password list. As with SSH, the attack was performed with one task at a time to keep the environment stable. The brute-force test successfully recovered the valid credentials for the FTP service.

## Results
- **SSH cracked successfully** — valid credentials found: `test_user:testpassword`
- **FTP cracked successfully** — valid credentials found: `test_user:testpassword`
- The lab confirmed that weak passwords are vulnerable to brute-force and dictionary attacks with Hydra

## Issues Encountered During the Test
- SSH limited multiple simultaneous connections, so Hydra had to be executed with `-t 1`
- VSFTPD was listening on IPv6 by default, so the configuration had to be adjusted for IPv4 testing
- The original password list was too large for the lab setup, so a shorter custom password list was created to reduce crashes and keep the test manageable

## Security Takeaways
This lab highlights some basic but important security lessons:
- Weak passwords can be recovered quickly with brute-force and dictionary attacks
- FTP is an insecure legacy service because it sends credentials in clear text
- SSH should be hardened by using key-based authentication instead of passwords
- Access controls and tools like **fail2ban** can reduce brute-force exposure

## Conclusion
The lab confirmed that weak credentials can be recovered through brute-force attacks against both SSH and FTP. Hydra successfully found valid credentials for the two services, showing why strong passwords and proper service hardening are essential.

## Screenshot Captions
- **Figure 1 – Successful connectivity test in the lab environment**
- **Figure 2 – SSH service started and verified on Kali Linux**
- **Figure 3 – Hydra finding valid SSH credentials**
- **Figure 4 – VSFTPD setup for FTP testing**
- **Figure 5 – Hydra finding valid FTP credentials**

## Disclaimer
This project was carried out in a legal and controlled lab environment for educational purposes only.

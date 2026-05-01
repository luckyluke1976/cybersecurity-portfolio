# Network Traffic Analysis with Wireshark

## Objective

The goal of this lab is to analyze a network traffic capture made with Wireshark
in order to identify Indicators of Compromise (IOCs) — signals that suggest
an attack is in progress or has already occurred.

Based on the IOCs found, possible attack vectors will be identified and
concrete actions will be proposed to reduce the impact of the attack.

---

## Lab Environment

| Machine | Role | IP Address | OS |
|---|---|---|---|
| 🐉 Kali Linux | Analyst | 192.168.200.100 | Kali Linux |
| 💀 Metasploitable | Target | 192.168.200.150 | Metasploitable 2 |

All VMs are connected on the same VirtualBox internal network.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Wireshark | Network traffic analysis — capture and inspect packets, protocols, IP addresses and communication content |

---

## Results

### IOC #1 — Public Service Announcement (BROWSER Protocol)
At row 1, a broadcast packet is observed sent from 192.168.200.150
to 192.168.200.255 via the BROWSER protocol. The machine publicly
identifies itself with the name METASPLOITABLE, announcing its
exposed services to the entire network.

### IOC #2 — Active Port Scan
From row 13 onwards, a very high volume of TCP packets with SYN flag
is observed, coming from 192.168.200.100 towards 192.168.200.150,
targeting different ports in very rapid sequence. This pattern is
consistent with an active port scan of the target machine.

### IOC #3 — Vulnerable Samba Service Exposed
Filtering traffic with the `smb` filter, it is observed that machine
192.168.200.150 is broadcasting its Samba version: Samba 3.0.20-Debian.
This version is known to contain critical vulnerabilities that allow
remote command execution without authentication (CVE-2007-2447).

---

## Issues Encountered During the Test

No major technical issues were encountered during this lab.

The main points that required attention were:
- Identifying the correct Wireshark filter (`smb`) to isolate the Samba
  traffic and read the version details
- Recognizing the SYN scan pattern from the raw traffic without any
  automated tool assistance

---

## Conclusion

The Wireshark traffic analysis revealed clear signs of active reconnaissance
on the network. An attacker at 192.168.200.100 mapped the services exposed
on the target machine (192.168.200.150) and identified a critical vulnerable
service: Samba 3.0.20.

Three IOCs were identified:
- A broadcast packet exposing the machine name and services
- An active SYN port scan
- Samba 3.0.20 exposed on the network, affected by CVE-2007-2447

The identified vulnerability allows full system access without authentication.
Immediate action is recommended to reduce the attack surface:
- Update Samba to a non-vulnerable version (>= 3.0.25rc3)
- Block SMB ports (139, 445) from external access
- Disable unnecessary network announcements

---

## Technical Walkthrough

### Step 1 — General Traffic Analysis
At first glance of the capture, an abnormal volume of TCP packets is
immediately visible coming from 192.168.200.100 towards 192.168.200.150.
The traffic appears very regular and mechanical, with SYN packets sent to
different ports in rapid sequence — a typical characteristic of an automated scan.

### Step 2 — SYN Traffic Analysis
Observing rows from 13 onwards, TCP packets almost all have the SYN flag
active and always come from the same source IP. This pattern is consistent
with an active port scan, where the attacker is trying to identify which
ports are open on the target machine.

### Step 3 — Broadcast Traffic Analysis
At row 1, a BROWSER protocol packet is observed sent in broadcast from
192.168.200.150 to 192.168.200.255. The machine publicly identifies itself
with the name METASPLOITABLE and announces its services to the network.

### Step 4 — SMB Filter
Applying the `smb` filter in the Wireshark search bar, it was possible to
isolate the SMB traffic and analyze the Host Announcement packet in detail.
The details panel clearly shows that the machine is running Samba 3.0.20-Debian
— a version affected by critical known vulnerabilities (CVE-2007-2447).

---

> ⚠️ **Disclaimer:** This lab was performed in a controlled environment for educational purposes only.
> All tools were used exclusively on machines owned and managed by the author.

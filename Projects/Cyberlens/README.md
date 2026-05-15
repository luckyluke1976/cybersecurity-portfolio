# CyberLens — Even Realities G2 SOC Assistant

> A wearable cybersecurity assistant for junior analysts.  
> Real-time threat lookups, IR playbooks, and OSINT — displayed on your glasses, controlled with a ring.  
> No screen. No phone. Hands-free.

---

## Table of Contents

1. [What Is CyberLens?](#1-what-is-cyberlens)
2. [Hardware Requirements](#2-hardware-requirements)
3. [Architecture Overview](#3-architecture-overview)
4. [Installation & Setup](#4-installation--setup)
5. [Display Constraints](#5-display-constraints)
6. [Ring Controller Navigation](#6-ring-controller-navigation)
7. [Home Screen & Categories](#7-home-screen--categories)
8. [Voice Commands — Complete Reference](#8-voice-commands--complete-reference)
   - [CVE Lookup](#81-cve-lookup)
   - [IOC Extractor](#82-ioc-extractor)
   - [IOC Enrichment](#83-ioc-enrichment)
   - [OSINT IP Lookup](#84-osint-ip-lookup)
   - [Hash Lookup](#85-hash-lookup)
   - [DNS Lookup](#86-dns-lookup)
   - [Subnet Calculator](#87-subnet-calculator)
   - [Port Lookup](#88-port-lookup)
   - [MITRE ATT&CK Reference](#89-mitre-attck-reference)
   - [Cheat Sheets](#810-cheat-sheets)
   - [Troubleshooting Guide](#811-troubleshooting-guide)
   - [IR Playbooks (NIST SP 800-61)](#812-ir-playbooks-nist-sp-800-61)
   - [Log Code Reference](#813-log-code-reference)
   - [Log Code by Category](#814-log-code-by-category)
   - [Encoder / Decoder](#815-encoder--decoder)
   - [Password Analyzer](#816-password-analyzer)
   - [Timeline Builder](#817-timeline-builder)
   - [Firewall / ACL Generator](#818-firewall--acl-generator)
   - [Threat Intel Live](#819-threat-intel-live)
   - [Session Log](#820-session-log)
9. [Tips Module — Live Interview Coach](#9-tips-module--live-interview-coach)
10. [Mobile Web App](#10-mobile-web-app)
11. [Privacy & Security Model](#11-privacy--security-model)
12. [Module Status](#12-module-status)
13. [Known Bugs & Limitations](#13-known-bugs--limitations)
14. [Environment Variables](#14-environment-variables)
15. [Project Structure](#15-project-structure)
16. [Development Rules](#16-development-rules)
17. [Roadmap — Next Steps](#17-roadmap--next-steps)
18. [About the Author](#18-about-the-author)

---

## 1. What Is CyberLens?

CyberLens is a wearable SOC assistant built for junior analysts.

It runs on **Even Realities G2** smart glasses and connects to a local Node.js server (port 3000) via the Even Hub SDK. You query it by voice; results appear on your glasses display in real time.

**20 active modules** cover the full SOC analyst workflow:
- Triage: CVE lookups, IP OSINT, IOC extraction and enrichment
- Investigation: subnet calc, DNS, hash lookup, log codes, MITRE ATT&CK
- Response: IR playbooks (20 NIST SP 800-61 scenarios), troubleshooting guides, timeline builder
- Reference: cheat sheets, ACL generator, encoder/decoder, password analyzer

There is also a **mobile web app** (browser-based dashboard) for use when the glasses are not available, and a **Tips module** that acts as a real-time interview coach.

**What CyberLens is NOT:**
- A cloud service — everything runs locally unless you explicitly call an OSINT module
- A SIEM or real-time IDS/IPS
- A replacement for professional threat intelligence platforms

---

## 2. Hardware Requirements

| Component | Requirement |
|---|---|
| Smart Glasses | Even Realities G2 |
| Ring Controller | Even Realities companion ring (included with G2) |
| Host Machine | Windows / macOS / Linux with Node.js 18+ |
| Network | Local only — no internet required for most modules |

The glasses connect to the host machine via the **Even Hub SDK**. The SOC server runs locally on port 3000. No data leaves your machine unless you run an OSINT or threat intel command.

---

## 3. Architecture Overview

```
[Voice Command or Ring Input]
        |
        v
[Even Hub SDK -- TypeScript / Vite]
  src/main.ts -- G2 UI, menu states, IOC nav
        |
        v
[Node.js SOC Server -- localhost:3000]
  server/index.js -- router, 25 handlers, Claude fallback
        |
        v
[G2 Display -- 56 chars/line, 10 lines max, ASCII only]
```

**Data flow:**
1. You speak a command (e.g. `ip 185.220.101.45`)
2. The TypeScript app parses the voice input and routes it to the correct server endpoint
3. The server fetches or computes the result
4. The result is formatted by the display layer (56-char wrap, ASCII sanitisation)
5. The formatted output appears on your glasses

The glasses are a **display layer only**. All logic runs on the server.

---

## 4. Installation & Setup

### Prerequisites

```bash
node --version   # 18 or higher required
npm --version    # any recent version
```

### Clone and install

```bash
git clone https://github.com/luckyluke1976/cybersecurity-portfolio.git
cd cyberlens-g2
npm install
```

### Configure environment

Create a `.env` file in the project root:

```env
# Required for all modules
VITE_SERVER_URL=http://localhost:3000

# Required for CVE lookup (Claude AI)
ANTHROPIC_API_KEY=your_key_here

# Required for OSINT IP and IOC enrichment
ABUSEIPDB_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here

# Required for Tips LIVE mode
SONIOX_API_KEY=your_key_here

# Required for Threat Intel Live
FIRECRAWL_API_KEY=your_key_here
```

All **static modules** (port lookup, cheat sheets, playbooks, log codes, MITRE, subnet calc, encoder, password analyzer, ACL generator) work without any API keys.

### Start the SOC server

```bash
npm run server
```

### Start the glasses app

```bash
npm run dev
```

Open the Even Hub app on your PC and connect your G2 glasses. The home screen will appear on the display within a few seconds.

> **Important:** After any change to `server/index.js`, always restart with `npm run restart`. Never apply partial patches -- replace the full file.

---

## 5. Display Constraints

The G2 uses a waveguide display. These are hardware constraints, not bugs.

| Constraint | Value |
|---|---|
| Characters per line | **56 max** |
| Lines per screen | **10 max** |
| Character encoding | **ASCII only** |
| Unicode rendering | Renders as `?` |

**Characters to avoid in server responses:**
- `->` is fine. `arrow` unicode is not.
- Use `-` for bullets, not `*` unicode variants
- Use straight quotes `"` and `'` only

The `display.ts` layer handles 56-char line wrapping automatically. Do not bypass it.

For results longer than ~10 lines (>672 characters), pagination is active: a `-- ring down for more --` prompt appears at the bottom of each page.

---

## 6. Ring Controller Navigation

The ring is the only physical input during operation.

| Ring Action | Result |
|---|---|
| **Scroll up** (eventType=1) | Move up through lines |
| **Scroll down** (eventType=2) | Move down through lines |
| **Single click** | Select / confirm |
| **Double-click** | Go back (context-aware: home / menu / IOC list) |

Back navigation is context-aware: double-click returns you to the most recent meaningful screen, not always home.

---

## 7. Home Screen & Categories

On launch, the home screen displays four categories:

| Category | Modules |
|---|---|
| **TRIAGE** | CVE, OSINT IP, IOC Extractor, Hash Lookup |
| **INVESTIGATE** | DNS, Subnet Calc, MITRE ATT&CK, Log Codes, Password Analyzer |
| **RESPOND** | IR Playbooks, Troubleshooting, Timeline Builder, ACL Generator |
| **REFERENCE** | Port Lookup, Cheat Sheets, Encoder/Decoder, Threat Intel Live |

You can navigate the menu with the ring, or skip it entirely and trigger any module directly by voice from any screen.

There is also an **IOC List mode**: when an IP, hash, URL, or CVE is detected in input, it is automatically parsed and added to a navigable IOC list you can scroll with the ring.

---

## 8. Voice Commands -- Complete Reference

All commands follow the pattern: **keyword + parameter**.  
Commands are case-insensitive. Speak clearly at normal pace.

---

### 8.1 CVE Lookup

**Trigger:** `cve <code>`  
**Example:** `cve CVE-2021-44228`  
**External API:** Claude Sonnet 4.6  
**API key required:** `ANTHROPIC_API_KEY`

Returns a plain-English summary of the CVE: what it is, what it affects, CVSS score, and recommended action.

```
CVE-2021-44228 (Log4Shell)
CVSS : 10.0 CRITICAL
Affects: Apache Log4j 2.0-2.14.1
Impact: RCE via JNDI injection
  in log messages
Fix: Upgrade to Log4j 2.15.0+
```

---

### 8.2 IOC Extractor

**Trigger:** `ioc <text>`  
**Example:** `ioc 192.168.1.1 connected to evil.com hash abc123`  
**External API:** None (local regex)

Automatically parses a block of text and extracts all Indicators of Compromise:
- IP addresses (IPv4 / IPv6)
- Domain names and URLs
- File hashes (MD5, SHA1, SHA256)
- CVE identifiers

Extracted IOCs are added to the navigable IOC List. Use the ring to scroll through them. Double-click any IOC to enrich it.

---

### 8.3 IOC Enrichment

**Trigger:** `enrich <text>`  
**Example:** `enrich 185.220.101.45`  
**External API:** VirusTotal + AbuseIPDB  
**API keys required:** `VIRUSTOTAL_API_KEY`, `ABUSEIPDB_API_KEY`

Enriches a given IOC (IP, domain, hash, or URL) by querying VirusTotal and AbuseIPDB. Returns a consolidated threat summary.

Capped at **3 lookups per IOC type** per session to preserve API quota.

---

### 8.4 OSINT IP Lookup

**Trigger:** `ip <address>`  
**Example:** `ip 185.220.101.45`  
**External API:** AbuseIPDB + DNS resolver  
**API key required:** `ABUSEIPDB_API_KEY`

Returns abuse confidence score, report count, and threat tags for a given IP address.

```
IP 185.220.101.45
Country  : Germany (DE)
ASN      : AS24940 Hetzner
ISP      : Hetzner Online GmbH
Abuse    : 97% confidence
Reports  : 1,243 total
Tags     : Tor exit / scanner
```

> **Known issue:** VirusTotal IP reputation and ip-api.com geolocation are not yet integrated. See [Known Bugs](#13-known-bugs--limitations).

**Privacy note:** This command sends the queried IP to external services. Only investigate IPs you are authorised to query.

---

### 8.5 Hash Lookup

**Trigger:** `hash <sha256>`  
**Example:** `hash 5d41402abc4b2a76b9719d911017c592`  
**External API:** VirusTotal v3  
**API key required:** `VIRUSTOTAL_API_KEY`

Submits the hash to VirusTotal and returns the detection ratio, malware family (if known), and verdict.

```
HASH RESULT
Hash   : 5d41402abc4b2...
VT     : 47/72 engines
Family : Mirai botnet
Verdict: MALICIOUS
```

---

### 8.6 DNS Lookup

**Trigger:** `dns <domain> [type]`  
**Example:** `dns google.com` or `dns google.com MX`  
**External API:** Google DNS (8.8.8.8) + Cloudflare (1.1.1.1)

Resolves a domain using dual DNS resolvers for cross-validation. Supported record types: A, AAAA, MX, TXT, NS, CNAME.

Defaults to A record if no type is specified.

```
DNS google.com A
Google     : 142.250.180.46
Cloudflare : 142.250.180.46
Match      : YES
TTL        : 300s
```

---

### 8.7 Subnet Calculator

**Trigger:** `subnet <ip/cidr>`  
**Example:** `subnet 192.168.1.0/24`  
**External API:** None (local bitwise calculation)

Returns full subnet breakdown.

```
SUBNET 192.168.1.0/24
Network   : 192.168.1.0
Broadcast : 192.168.1.255
First host: 192.168.1.1
Last host : 192.168.1.254
Mask      : 255.255.255.0
Hosts     : 254
```

---

### 8.8 Port Lookup

**Trigger:** `porta <number>`  
**Example:** `porta 443`  
**External API:** None (static JSON -- 47 ports)

Returns protocol, service name, and risk level for a given port number.

```
PORT 443
Protocol : TCP
Service  : HTTPS
Usage    : Encrypted web traffic
Risk     : Low (standard)
```

---

### 8.9 MITRE ATT&CK Reference

**Trigger:** `mitre <technique-id>`  
**Example:** `mitre T1059`  
**External API:** None (static JSON -- top 100 techniques)

Returns technique name, tactic, description, and detection notes for the given ATT&CK technique ID.

```
T1059 -- Command & Scripting
Tactic : Execution
Desc   : Attacker uses command
  interpreter (cmd, PS, bash)
  to run malicious commands
Detect : Monitor process creation,
  script block logging (PS)
```

The local database covers the **100 most common ATT&CK techniques**. For the full matrix, refer to attack.mitre.org.

---

### 8.10 Cheat Sheets

**Trigger:** `cheat <tool>`  
**Example:** `cheat nmap`  
**External API:** None (static JSON -- 10 tools)

Returns a compact command reference for common SOC tools.

**Available tools:**

| Keyword | Tool |
|---|---|
| `nmap` | Network scanning |
| `wireshark` | Packet analysis filters |
| `tcpdump` | CLI packet capture |
| `netstat` | Network connections |
| `grep` | Log searching |
| `iptables` | Linux firewall rules |
| `curl` | HTTP request testing |
| `dig` | DNS queries |
| `openssl` | TLS/certificate inspection |
| `volatility` | Memory forensics |

---

### 8.11 Troubleshooting Guide

**Trigger:** `trouble <scenario>`  
**Example:** `trouble no-internet`  
**External API:** None (static JSON -- 6 scenarios)

Returns a numbered step-by-step diagnostic guide.

**Available scenarios:**

| Keyword | Scenario |
|---|---|
| `no-internet` | Host has no internet connectivity |
| `dns-fail` | DNS resolution failures |
| `high-traffic` | Unusual traffic volume |
| `slow-network` | Network performance degradation |
| `auth-fail` | Authentication failures / lockouts |
| `firewall-block` | Traffic blocked by firewall |

---

### 8.12 IR Playbooks (NIST SP 800-61)

**Trigger:** `playbook <scenario>` or `playbook <scenario> <phase>`  
**Examples:**
- `playbook ransomware` -- full playbook
- `playbook ransomware containment` -- single phase only  
**External API:** None (20 scenario JSON files)

Returns an Incident Response playbook structured around the **NIST SP 800-61 Rev. 2** lifecycle:

1. Preparation
2. Detection & Analysis
3. Containment
4. Eradication
5. Recovery
6. Post-Incident

**Available scenarios (20 total):**

| Keyword | Incident Type |
|---|---|
| `ransomware` | Ransomware infection |
| `phishing` | Phishing attack |
| `ddos` | Distributed Denial of Service |
| `data-breach` | Data exfiltration / breach |
| `insider-threat` | Malicious insider |
| `malware` | Generic malware infection |
| `apt` | Advanced Persistent Threat |
| `web-defacement` | Website defacement |
| `credential-theft` | Stolen credentials |
| `supply-chain` | Supply chain compromise |
| `zero-day` | Zero-day exploit |
| `social-engineering` | Social engineering attack |
| `business-email` | Business email compromise (BEC) |
| `cryptomining` | Cryptominer infection |
| `lateral-movement` | Lateral movement detected |
| `exfiltration` | Data exfiltration in progress |
| `privilege-escalation` | Privilege escalation |
| `persistence` | Persistence mechanism found |
| `c2-beacon` | C2 beaconing detected |
| `wiper` | Wiper malware / destructive attack |

**Sample output (ransomware -- containment):**

```
RANSOMWARE -- CONTAINMENT
1. Isolate affected hosts from LAN
2. Disable shared drives immediately
3. Block C2 IPs at perimeter FW
4. Preserve memory dumps if possible
5. Do NOT reboot -- evidence loss risk
```

---

### 8.13 Log Code Reference

**Trigger:** `log? <code>`  
**Example:** `log? 4625`  
**External API:** None (static JSON)

Returns description, category, severity, and investigation notes for a specific log event code.

**Supported log sources:** Windows Event Log, Linux syslog, Firewall logs, Web server logs, Auth logs.

```
EVENT 4625
Category : Logon / Logoff
Meaning  : Failed logon attempt
Severity : Medium-High
Notes    : Multiple 4625 in short
  window = brute force indicator
  Check SubStatus for reason
  Cross-ref with 4624 (success)
```

---

### 8.14 Log Code by Category

**Trigger:** `logref <category>`  
**Example:** `logref windows`  
**External API:** None

Returns all log codes in a given category with one-line descriptions.

**Available categories:** `windows`, `linux`, `firewall`, `web`, `auth`

---

### 8.15 Encoder / Decoder

**Trigger:** `encode <format> <string>` or `decode <format> <string>`  
**Example:** `encode base64 hello world`  
**External API:** None (local)

**Supported formats:**

| Format | Encode | Decode |
|---|---|---|
| `base64` | Yes | Yes |
| `url` | Yes | Yes |
| `hex` | Yes | Yes |
| `rot13` | Yes | Yes (symmetric) |
| `html` | Yes | Yes |

```
ENCODE base64
Input  : hello world
Output : aGVsbG8gd29ybGQ=
```

---

### 8.16 Password Analyzer

**Trigger:** `pwcheck <password>`  
**Example:** `pwcheck P@ssw0rd123`  
**External API:** None (local -- entropy calc + rockyou top 1000)

Analyses a password for strength using two methods:
1. **Entropy calculation** -- based on character set and length
2. **rockyou top 1000 check** -- flags if the password appears in common breach lists

```
PWCHECK P@ssw0rd123
Length   : 11
Entropy  : 62.3 bits
Charset  : upper+lower+digit+symbol
rockyou  : NOT in top 1000
Verdict  : MODERATE
Notes    : Pattern detected (leet
  substitution). Use a passphrase.
```

---

### 8.17 Timeline Builder

**Trigger:** `timeline add <time> <event>` or `timeline show`  
**Example:** `timeline add 09:15 failed login from 10.0.0.5`  
**External API:** None (in-memory + JSON persist to `timeline.json`)

Builds a chronological incident timeline you can populate during an investigation. Entries persist to `timeline.json` and survive server restarts.

**Commands:**

| Command | Action |
|---|---|
| `timeline add <HH:MM> <description>` | Add an event |
| `timeline show` | Display the full timeline |
| `timeline clear` | Clear all entries |

```
INCIDENT TIMELINE
09:15 Failed login 10.0.0.5
09:18 Account locked out
09:22 Lateral movement detected
09:31 C2 beacon observed
09:45 IR team notified
```

---

### 8.18 Firewall / ACL Generator

**Trigger:** `acl <rule>`  
**Example:** `acl allow 10.0.0.5 -> any 445 tcp`  
**External API:** None (local)

Generates firewall rules in both **iptables** (Linux) and **PowerShell** (Windows) syntax. Supports a label system for rule documentation.

```
ACL RULE GENERATED
Action : ALLOW
Source : 10.0.0.5
Dest   : ANY
Port   : 445 (SMB)
Proto  : TCP
---
iptables:
iptables -A INPUT -s 10.0.0.5
  -p tcp --dport 445 -j ACCEPT
---
PowerShell:
New-NetFirewallRule -Direction
  Inbound -LocalPort 445
  -Protocol TCP -Action Allow
  -RemoteAddress 10.0.0.5
```

---

### 8.19 Threat Intel Live

**Trigger:** `threat <keyword>`  
**Example:** `threat log4j`  
**External API:** Firecrawl (feodotracker, NVD, Google Security Advisory)  
**API key required:** `FIRECRAWL_API_KEY`

Performs a live threat intelligence query across multiple sources and returns a consolidated summary of current activity, known indicators, and advisories.

> **Note:** Subject to Firecrawl timeout (10s). If the query fails, retry once. Retry logic not yet implemented -- see [Known Bugs](#13-known-bugs--limitations).

---

### 8.20 Session Log

**Trigger:** `log` or `log delete <id>`  
**External API:** None (in-memory, TTL 24h)

Displays a log of all queries made in the current session, with timestamps and response summaries. Entries are automatically cleared after 24 hours. Nothing is written to disk by default.

```
SESSION LOG
[09:15] ip 185.220.101.45 -> MALICIOUS
[09:22] cve CVE-2021-44228 -> CRITICAL
[09:30] playbook ransomware -> displayed
[09:44] timeline add 09:15 ...
```

---

## 9. Tips Module -- Live Interview Coach

> Status: Active -- `SONIOX_API_KEY` required for LIVE mode.

The Tips module turns CyberLens into a real-time interview assistant. It listens to the conversation around you and displays relevant IT/security concept definitions on your glasses as terms come up -- no phone, no googling, no breaking eye contact.

### Operating Modes

**LIVE mode** -- G2 microphone
- Uses the G2 microphone + **Soniox API** with speaker diarization
- Your voice is enrolled and filtered out -- only the interviewer's speech is transcribed
- Concepts are extracted and matched to a local definition database in real time
- **Requires:** `SONIOX_API_KEY`, active internet connection

**REMOTE mode** -- PC audio loopback
- Captures system audio output (e.g., during a video interview)
- Runs **Faster-Whisper tiny int8** -- fully local, zero external calls
- Slightly higher latency but completely private
- **Requires:** Nothing -- runs offline

### Commands

```
/tips start       -- start listening (auto-selects mode)
/tips live        -- force LIVE mode (Soniox)
/tips toggle      -- toggle on/off
/tips stop        -- stop listening
```

### Display Behaviour

- Concepts stack newest-first on the display
- Ring scrolls through the concept list
- Duplicates are ignored automatically
- Auto-reset every 24 hours

---

## 10. Mobile Web App

CyberLens includes a browser-based dashboard for use when the glasses are not available.

| File | Purpose |
|---|---|
| `cyberlens-mobile.html` | Full mobile dashboard -- all modules |
| `tips-mobile.html` | Tips system UI for mobile |
| `page-guide.html` | Onboarding reference guide |
| `page-cheat.html` | Interactive cheat sheet navigator |
| `page-trouble.html` | Troubleshooting flowchart |
| `page-playbook.html` | IR playbook step navigator |

To use: start the SOC server (`npm run server`), then open any HTML file in a browser on the same local network.

---

## 11. Privacy & Security Model

CyberLens is built local-first. The CIA Triad is the design foundation for every module decision.

| Module | External Calls | Data Sent |
|---|---|---|
| Port Lookup | None | Nothing |
| Subnet Calculator | None | Nothing |
| Cheat Sheets | None | Nothing |
| Troubleshooting | None | Nothing |
| IR Playbooks (20 scenarios) | None | Nothing |
| Log Code Reference | None | Nothing |
| MITRE ATT&CK | None | Nothing |
| Encoder / Decoder | None | Nothing |
| Password Analyzer | None | Nothing |
| Timeline Builder | None | Nothing |
| ACL Generator | None | Nothing |
| CVE Lookup | Claude AI API | CVE code only |
| OSINT IP Lookup | AbuseIPDB, DNS resolver | IP address |
| Hash Lookup | VirusTotal v3 | Hash value |
| IOC Enrichment | VirusTotal, AbuseIPDB | IOC value (max 3/type) |
| DNS Lookup | Google 8.8.8.8, Cloudflare 1.1.1.1 | Domain name |
| Threat Intel Live | Firecrawl, NVD, feodotracker | Search keyword |
| Tips (LIVE mode) | Soniox API | Audio stream |
| Tips (REMOTE mode) | None | Nothing |
| Session Log | None | Nothing |

**Session data:**
- Stored in RAM only
- 24-hour TTL -- cleared automatically
- Nothing written to disk by default
- Exception: `timeline.json` is persisted to disk if you use the Timeline Builder

---

## 12. Module Status

| Module | Status |
|---|---|
| Home screen + ring navigation | Working |
| IOC List mode (auto-parse + ring nav) | Working |
| CVE Lookup | Working |
| IOC Extractor | Working |
| IOC Enrichment | Working |
| OSINT IP Lookup | Working (partial -- see Known Bugs) |
| Hash Lookup | Working |
| DNS Lookup | Working |
| Subnet Calculator | Working |
| Port Lookup | Working |
| MITRE ATT&CK Reference | Working |
| Cheat Sheets | Working |
| Troubleshooting Guide | Working |
| IR Playbooks (20 scenarios) | Working |
| Log Code Reference | Working |
| Log Code by Category | Working |
| Encoder / Decoder | Working |
| Password Analyzer | Working |
| Timeline Builder | Working |
| Firewall / ACL Generator | Working |
| Threat Intel Live | Working (no retry on timeout) |
| Session Log | Working |
| Tips LIVE mode | Active -- SONIOX_API_KEY required |
| Tips REMOTE mode | Active |
| Wake word "Veronica" | Planned |
| iPhone / LAN test page | Planned |

---

## 13. Known Bugs & Limitations

| Priority | Module | Issue |
|---|---|---|
| CRITICAL | OSINT IP | Missing VirusTotal IP reputation and ip-api.com geolocation. Currently AbuseIPDB + DNS only. Full spec requires: threat score, ASN, anonymisation detection (Tor/VPN/proxy), geolocation, service identification. |
| HIGH | Tips (LIVE) | `/tips/start/live` fails silently without `SONIOX_API_KEY`. No user-facing error message displayed. |
| HIGH | Display | Some CVE and Threat Intel responses may exceed 10-line / 672-char limit. Pagination prompt not consistently triggered on all overflow paths. |
| MEDIUM | Threat Intel Live | Firecrawl queries fail with no retry on 10s timeout. Single point of failure with no fallback. |

---

## 14. Environment Variables

| Variable | Required For | Notes |
|---|---|---|
| `VITE_SERVER_URL` | All modules | Default: `http://localhost:3000` |
| `ANTHROPIC_API_KEY` | CVE Lookup | Claude Sonnet 4.6 |
| `ABUSEIPDB_API_KEY` | OSINT IP, IOC Enrichment | Free tier: 1,000 req/day |
| `VIRUSTOTAL_API_KEY` | Hash Lookup, IOC Enrichment | Free tier: 4 req/min |
| `SONIOX_API_KEY` | Tips LIVE mode | Paid API |
| `FIRECRAWL_API_KEY` | Threat Intel Live | Paid API |

Never commit `.env` to version control. Use `.env.example` to document required variables without values.

---

## 15. Project Structure

```
cyberlens-g2/
|
|-- server/
|   |-- index.js                    # Main router -- 25 handlers, Claude fallback
|   |-- tips-router.js              # /tips endpoints, Soniox WebSocket
|   |-- data/
|       |-- ports.json              # 47 port definitions
|       |-- cheatsheets.json        # 10 tool cheat sheets
|       |-- mitre.json              # 100 MITRE ATT&CK techniques
|       |-- rockyou_top1000.json    # Common password list
|       |-- troubleshooting.json    # 6 troubleshooting scenarios
|       |-- logcodes/               # Windows, Linux, FW, Web, Auth
|   |-- playbooks/                  # 20 IR playbook JSON files
|
|-- src/
|   |-- main.ts                     # G2 UI, 4 menu states, IOC nav
|   |-- display.ts                  # 56-char formatter, ASCII sanitiser
|   |-- commands.ts                 # Voice command parser and router
|
|-- cyberlens-mobile.html           # Mobile dashboard
|-- tips-mobile.html                # Tips mobile UI
|-- page-guide.html                 # Onboarding reference
|-- page-cheat.html                 # Cheat sheet navigator
|-- page-trouble.html               # Troubleshooting flowchart
|-- page-playbook.html              # IR playbook navigator
|
|-- vite.config.ts
|-- package.json                    # "type": "module" (ES modules only)
|-- .env                            # API keys -- never commit
|-- .env.example                    # Template for required variables
|-- timeline.json                   # Persisted timeline entries
```

---

## 16. Development Rules

These rules are non-negotiable.

**Server:**
- Never apply surgical patches to `index.js` -- always replace the full file
- Restart the server after every change: `npm run restart`
- ES modules only -- `"type": "module"` in `package.json`
- Use `fileURLToPath` for `__dirname` on Windows (ES module workaround)
- Never use PowerShell here-strings for JS or JSON -- use backticks

**Security:**
- Never expose API keys in chat or commit history
- Always anonymise real IPs and names before sharing code for review
- `.env` never touches version control

**Display:**
- Every server response must pass through `display.ts` before reaching the glasses
- Test all new modules against the 56-char limit before shipping
- ASCII only -- test with Unicode input to confirm `?` sanitisation works

**Commits:**
- Message format: imperative present tense (`Add MITRE module`, `Fix OSINT timeout`)
- Link issue number where applicable
- Pre-commit hooks: linting + type check

---

## 17. Roadmap -- Next Steps

### OSINT IP Enhancement (Priority 1)
1. Integrate ip-api.com -- geolocation + ISP + ASN
2. Integrate VirusTotal IP reputation endpoint
3. Add anonymisation detection (Tor, VPN, proxy flags)
4. Merge all sources into a single `/ip` display response
5. Test against known malicious IPs
6. Update `MENU_HINTS` for the new output format

### Display & UX Polish
1. Consistent pagination for all results exceeding 672 chars
2. Fix `-- ring down for more --` prompt on all overflow paths
3. Confirm iPhone access to `cyberlens-mobile.html` over LAN

### GitHub
1. Commit all current working modules
2. Push updated README to portfolio repo

---

## 18. About the Author

Built by **Luca Danisi** -- aspiring SOC Analyst, targeting Vienna.  
Finance and law background, pivoting into cybersecurity.

**Cert roadmap:** CCST -> Security+ -> CySA+ -> ISO 27001 -> CISM

Portfolio: [github.com/luckyluke1976/cybersecurity-portfolio](https://github.com/luckyluke1976/cybersecurity-portfolio)


# CyberLens — Even Realities G2 Smart Glasses App

> A wearable SOC assistant for junior analysts. Real-time cybersecurity lookups on your glasses display, controlled with a ring.

---

## What Is This?

CyberLens Glasses is the wearable interface of the CyberLens SOC Assistant project.  
It runs on **Even Realities G2** smart glasses and lets you query a local Node.js SOC server hands-free using voice commands and a ring controller — no phone, no screen required.

This is part of a larger portfolio project by a cybersecurity student targeting the SOC analyst career path.

---

## How It Works

```
[Voice Command or Ring Input]
        ↓
[Even Hub SDK — TypeScript / Vite app]
        ↓
[Local Node.js Server — localhost:3000]
        ↓
[G2 Display — 56 chars/line, 12 lines max]
```

The app connects to the G2 glasses via the **Even Realities Even Hub SDK**.  
All data stays local by default. External APIs are only called for specific threat-intel modules.

---

## Features

| Voice Trigger | Module | External API? |
|---|---|---|
| `porta <number>` | Port Lookup | No |
| `cve <code>` | CVE Details | Claude AI |
| `subnet <ip/cidr>` | Subnet Calculator | No |
| `cheat <tool>` | Cheat Sheet | No |
| `trouble <scenario>` | Troubleshooting Guide | No |
| `playbook <scenario>` | IR Playbook (NIST SP 800-61) | No |
| `playbook <scenario> <phase>` | IR Playbook — single phase | No |
| `log? <code>` | Log Code Reference | No |
| `logref <category>` | Log Code by category | No |
| `acl <rule>` | Firewall / ACL Generator | No |
| `ip <address>` | OSINT IP Lookup | ip-api.com + AbuseIPDB |

---

## Display Constraints

The G2 uses a waveguide display — not a standard screen.  
Every server response is formatted before it reaches the glasses:

- **56 characters per line** — hard limit
- **10–12 lines maximum** per screen
- **ASCII only** — Unicode symbols render as `?` on the G2 bitmap font

---

## Navigation

The app is controlled with the **companion ring device**:

| Ring Action | Result |
|---|---|
| Scroll | Move through lines |
| Single click | Select / confirm |
| Double-click | Go back / home screen |

Home screen is split into 4 categories: **TRIAGE / INVESTIGATE / RESPOND / REFERENCE**

---

## Architecture

```
cyberlens-g2/
├── src/
│   ├── main.ts          # Entry point, Even Hub SDK init
│   ├── display.ts       # G2 formatter (56 char wrap, ASCII)
│   └── commands.ts      # Voice command parser + router
├── vite.config.ts
├── package.json
└── .env                 # VITE_SERVER_URL=http://localhost:3000
```

**Stack:** TypeScript · Vite · Even Realities Even Hub SDK

The glasses app is the display layer only. All logic lives in the SOC server.

---

## Privacy & Design Philosophy

- **Local-first**: no data leaves your machine unless you explicitly run an OSINT command
- **CIA Triad as foundation**: every design decision evaluated against Confidentiality, Integrity, Availability
- Static lookups (ports, cheat sheets, subnets, playbooks, log codes) make **zero external calls**
- Claude AI is called only for CVE queries and open-ended questions
- Session logs are stored in RAM with a 24h TTL — nothing written to disk by default

---

## Module Status

| Module | Status |
|---|---|
| Home screen + ring navigation | Working |
| Port Lookup | Working |
| CVE Lookup | Working |
| Subnet Calculator | Working |
| Cheat Sheet | Working |
| Troubleshooting Guide | Working |
| IR Playbooks (x12 NIST scenarios) | Working |
| Log Code Reference | Working |
| Firewall / ACL Generator | Working |
| OSINT IP Lookup | Working |
| Hash Lookup | Working |
| Tips — live interview coach | Built, end-to-end test pending |
| Wake word "Veronica" | Planned |
| iPhone / LAN test page | Planned |

---

## Tips Module — Interview Coach

The Tips module captures spoken conversation in real time and displays relevant IT/security concept definitions directly on the G2 display.  
Designed for technical interviews and study sessions.

**LIVE mode** — G2 microphone → Soniox API with speaker diarization. Your voice is enrolled and filtered out; only the interviewer's speech is transcribed.

**REMOTE mode** — PC audio loopback → Faster-Whisper tiny int8, fully local, zero external calls.

Concepts stack newest-first, ring scrolls, auto-reset every 24h, duplicates ignored.

---

## About

Built by **Luca Danisi** — aspiring SOC Analyst, Vienna.  
Finance & law background, pivoting into cybersecurity.  
Cert roadmap: CCST -> Security+ -> CySA+ -> ISO 27001 -> CISM

Portfolio: [github.com/luckyluke1976/cybersecurity-portfolio](https://github.com/luckyluke1976/cybersecurity-portfolio)

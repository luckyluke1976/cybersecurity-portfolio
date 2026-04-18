# SOC Lab 09 – Buffer Overflow in C

## Overview
This lab demonstrates what a **Buffer Overflow (BOF)** is and how to trigger one in a small C program running on Kali Linux.

A Buffer Overflow happens when a program accepts user input without checking its length. If the input exceeds the buffer size (the "container" that should hold it), the extra characters end up in unauthorized memory areas and cause a **segmentation fault**.

## Objective
To write a deliberately vulnerable C program, trigger a Buffer Overflow by providing oversized input, and answer the question: *"Is increasing the buffer size enough to fix the vulnerability?"*

## Lab Environment
| Component | Details |
|---|---|
| Machine | Kali Linux – 192.168.50.100 |
| Network | VirtualBox Internal Network |
| Language | C |

## Tools Used
| Tool | Purpose |
|---|---|
| Terminal (Bash/Zsh) | Entire lab performed from the command line |
| GCC | C compiler — translates `.c` source code into an executable |
| Nano | Text editor for writing and modifying the C source code |
| C Language | Ideal for studying BOF because it performs no automatic bounds checking on buffers |

## Results

### ✅ Test 1 — Buffer of 10 chars, short input
Compiled `BOF.c` with `gcc -g BOF.c -o BOF` and ran it with input `esercizio` (9 characters).
**Result:** the program printed the username correctly and exited without errors.

### ❌ Test 2 — Buffer of 10 chars, long input
Re-ran the program with `eserciziomoooltopiùlungo` (24 characters).
**Result:**
```
zsh: segmentation fault ./BOF
```
Classic Buffer Overflow: the extra characters overwrote unauthorized memory areas and the OS terminated the process.

### ✅ Test 3 — Buffer of 30 chars, short input
Modified the source changing `char buffer [10];` to `char buffer [30];`, recompiled, and ran it with `esercizio` again.
**Result:** program worked fine without errors.

### ❌ Test 4 — Buffer of 30 chars, long input
With the 30-char buffer, entered `eserciziomooooltopiulungodiquellodiprima` (~40 characters).
**Result:**
```
zsh: segmentation fault ./BOF
```
The Buffer Overflow came back — increasing the buffer size only moved the threshold, it did not solve the problem.

## Issues Encountered During the Test
No major technical issues. The main point that required attention was choosing input strings long enough to reliably trigger the segmentation fault, especially after increasing the buffer size to 30 characters.

## Security Takeaways
- **Never trust user input** — always validate length and content before processing
- **Bounds checking is the programmer's job in C** — the language will not do it for you
- Buffer overflows are the foundation of many critical CVEs (EternalBlue, Heartbleed, BlueKeep) — understanding them at this level is key to recognizing them in real-world vulnerabilities
- Modern mitigations like **ASLR**, **stack canaries**, and **DEP/NX** make exploitation harder, but the underlying bug must still be fixed at the source code level

## Conclusion
Increasing the buffer size does **not** fix the vulnerability — it only moves it. The root cause is not the buffer size, but the fact that the program reads input without any length check.

To truly eliminate the vulnerability, the input must be **validated before being written into the buffer**. Safer alternatives to `scanf("%s", buffer)` include `fgets()` with a defined size limit, or `scanf("%9s", buffer)` to enforce a hard limit at read time.

## Technical Walkthrough

### Step 1 — Move to Desktop
```bash
cd /home/kali/Desktop
```

### Step 2 — Create the source file `BOF.c`
```bash
nano BOF.c
```

Code used:
```c
#include <stdio.h>

int main () {
    char buffer [10];
    printf ("Si prega di inserire il nome utente:");
    scanf ("%s", buffer);
    printf ("Nome utente inserito: %s\n", buffer);
    return 0;
}
```

### Step 3 — Compile
```bash
gcc -g BOF.c -o BOF
```

### Step 4 — First test (buffer 10, short input)
```bash
./BOF
```
Input: `esercizio` → program works correctly.

### Step 5 — Second test (buffer 10, long input) — Buffer Overflow!
Input: `eserciziomoooltopiùlungo` (24 chars) → `zsh: segmentation fault ./BOF`.

### Step 6 — Modify the code (buffer 30)
Changed `char buffer [10];` to `char buffer [30];`.

### Step 7 — Recompile
```bash
gcc -g BOF.c -o BOF
```

### Step 8 — Third test (buffer 30, short input)
Input: `esercizio` → program works correctly.

### Step 9 — Fourth test (buffer 30, long input) — Buffer Overflow again!
Input: `eserciziomooooltopiulungodiquellodiprima` (~40 chars) → `zsh: segmentation fault ./BOF`.

## Screenshot Captions
- **Figure 1 – Vulnerable C program in nano**
- **Figure 2 – Buffer Overflow triggered: segmentation fault on long input**

## Disclaimer
This project was carried out in a legal and controlled lab environment for educational purposes only.

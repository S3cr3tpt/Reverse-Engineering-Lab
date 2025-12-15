# ToasterBirb "Flags" Analysis

**Category:** Binary Exploitation / Reverse Engineering
**Difficulty:** Easy/Medium (Bitwise Logic)
**Tools:** Ghidra, Python (pwntools)

## 1. Challenge Overview
The target is a Linux ELF binary that asks for a "flag." It does not store the password in plain text. Instead, it uses a mathematical validation loop to check the input bit-by-bit.

## 2. Technical Analysis
The core logic resides in a loop that iterates 5 times (once for each character of the input).

**The Logic:**
The program checks if a specific bit in the user's input matches a hardcoded mask (`0x40`).
```c
// Decompiled Logic
mask = 0x40; // Binary: 0100 0000
loop (counter = 5 down to 1):
    if ( (input_byte << counter) & mask == 0 ) 
        return FAIL;
```c

The Math: To pass the check, the result of the shift operation must have the 7th bit set (matching 0x40).

Byte 1 (Shift 5): Needs bit 1 set -> 0x02 (Binary ...00010)

Byte 2 (Shift 4): Needs bit 2 set -> 0x04 (Binary ...00100)

Byte 3 (Shift 3): Needs bit 3 set -> 0x08 (Binary ...01000)

Byte 4 (Shift 2): Needs bit 4 set -> 0x10 (Binary ...10000)

Byte 5 (Shift 1): Needs bit 5 set -> 0x20 (Binary ...00000)
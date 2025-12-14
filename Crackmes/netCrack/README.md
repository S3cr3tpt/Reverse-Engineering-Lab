# NetCrack Analysis (Crackme #693017b5)

**Category:** Binary Exploitation / Network Protocol  
**Difficulty:** Beginner  
**Tools:** Ghidra, Python (pwntools), Netcat, ltrace  

## 1. Challenge Overview
The target is a Linux ELF binary that initiates a TCP connection to a specific port. The goal is to act as the server, accept the connection, and provide the correct password to retrieve the success flag.

## 2. Technical Analysis

### Dynamic Analysis (ltrace)
Tracing library calls revealed the network behavior:
```bash
ltrace ./crackme
# connect(3, {sa_family=AF_INET, sin_port=htons(3125), ...})

```

The binary acts as a **Client** connecting to 127.0.0.1:3125.

Static Analysis (Ghidra)
The validation logic resides in the checkResponse function:

## 1. **Input Capture:** It uses recv() to capture data into a buffer.

## 2. **Offset Logic:** It uses an LEA instruction to calculate Buffer_Start + Length - 6.

## 3. **Comparison:** It compares the last 6 bytes of the received data against the string "Platon".
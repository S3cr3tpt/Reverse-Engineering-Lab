#!/bin/bash
# Solver for NetCrack
# Usage: ./solver.sh

echo "[*] Setting up listener on port 3125..."
echo "[*] Waiting for target to connect..."

# -n removes the newline, ensuring exactly 6 bytes are sent
echo -n 'Platon' | nc -lvp 3125

echo -e "\n[+] Payload sent. Check client for success message."

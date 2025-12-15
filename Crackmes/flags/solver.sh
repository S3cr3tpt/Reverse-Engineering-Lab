#!/bin/bash
# Proof of Concept for ToasterBirb Flags
# Exploit: Bitwise Logic Bypass

TARGET="./bin/flags"

if [ ! -f "$TARGET" ]; then
    echo "[-] Binary $TARGET not found. Did you run decrypt.py?"
    exit 1
fi

chmod +x $TARGET

echo "[*] Sending minimal valid payload..."
# Payload: Bytes 0x02, 0x04, 0x08, 0x10, 0x20
# Logic: (0x02 << 5) & 0x40 == 0x40 (True), etc.
printf "\x02\x04\x08\x10\x20" | $TARGET

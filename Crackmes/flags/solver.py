import random
from pwn import *

# Set logging level to suppress noise, show only results
context.log_level = 'error'

BINARY_PATH = "./bin/flags"

def generate_key():
    """
    Generates a valid 5-byte key.
    Constraint: (Byte << Shift) & 0x40 != 0
    """
    key = bytearray()
    
    # Loop from 5 down to 1
    for shift in [5, 4, 3, 2, 1]:
        # Calculate the bit that MUST be 1
        target_bit = 6 - shift
        mandatory_val = (1 << target_bit)
        
        # Add random noise for the other bits (Polymorphism)
        # We use OR to ensure the mandatory bit remains 1
        noise = random.randint(0, 255)
        final_byte = mandatory_val | noise
        
        key.append(final_byte)
        
    return key

def main():
    try:
        # 1. Generate the Key
        key = generate_key()
        pretty_key = "".join([f"\\x{b:02x}" for b in key])
        print(f"[*] Generated Key: {pretty_key}")

        # 2. Start the Target Process
        # We assume the binary is in the 'bin' folder as per repo structure
        if not os.path.exists(BINARY_PATH):
            print(f"[-] Error: Binary not found at {BINARY_PATH}")
            return

        p = process(BINARY_PATH)

        # 3. Send Payload
        # We use 'send' instead of 'sendline' to avoid appending a newline \n
        p.send(key) 

        # 4. Receive and Print Output
        output = p.recvall().decode(errors='ignore')
        
        if "Thanks" in output:
            print(f"[+] SUCCESS! Target responded:\n{output.strip()}")
        else:
            print(f"[-] FAILED. Output:\n{output.strip()}")

        p.close()

    except Exception as e:
        print(f"[-] Execution Error: {e}")

if __name__ == "__main__":
    main()
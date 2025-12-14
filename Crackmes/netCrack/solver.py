#!/usr/bin/env python3
from pwn import *

# Context setup
context.log_level = 'info'

# Configuration
HOST = '0.0.0.0'
PORT = 3125
PASSWORD = b"Platon"

def main():
    log.info("[-] Setting up listener for the NetCrack binary...")
    
    # 1. Start a listener
    try:
        listener = listen(PORT, bindaddr=HOST)
    except Exception as e:
        log.error(f"Could not bind to port {PORT}. Error: {e}")
        return

    # 2. Wait for connection
    log.info(f"[*] Listening on {PORT}... Run the crackme binary now!")
    
    # This waits for the connection and returns the communication tube
    conn = listener.wait_for_connection()
    
    # FIX: Use .rhost instead of .remote_ip
    log.success(f"[+] Connection received from {conn.rhost}")

    # 3. Handle the Protocol
    time.sleep(0.5)

    # 4. Send the Payload
    log.info(f"[*] Sending payload: {PASSWORD}")
    try:
        conn.send(PASSWORD)
        log.success("[+] Payload sent successfully.")
    except Exception as e:
        log.error(f"Failed to send payload: {e}")

    # 5. Receive response
    try:
        # recv() reads data. We print it to prove we got the flag/success msg
        response = conn.recv(timeout=2)
        if response:
            print("\n" + "="*30)
            print(f"OUTPUT: {response.decode(errors='ignore').strip()}")
            print("="*30 + "\n")
    except:
        pass

    conn.close()

if __name__ == "__main__":
    main()
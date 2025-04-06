# RWARE

A demonstration project showing how a client script can use AES encryption (via the `cryptography` library) to encrypt files and send the encryption key to a remote server. This project consists of two main scripts:

- **encryptor.py**: The client-side script that generates an encryption key, (optionally) encrypts files, and sends the key to a server.
- **server.py**: The server-side script that listens for incoming connections and receives the encryption key.

> **WARNING: Legal Disclaimer**  
> This project is provided for **educational and authorized testing purposes only**.  
> The encryption functionality, if enabled, can cause irreversible data loss. **Do not run these scripts on any system containing valuable or sensitive data.**  
> By using this project, you agree that the author is not responsible for any misuse, damage, or legal consequences that may arise from its use.  
> **Do not use this code for any malicious or unauthorized activities.**

## Table of Contents
- [Overview](#overview)
- [File Descriptions](#file-descriptions)
- [Usage Instructions](#usage-instructions)
- [Setup](#setup)
- [Disclaimer](#disclaimer)
- [License](#license)

## Overview

This project demonstrates a simple method for combining AES encryption with socket communication. The `encryptor.py` script (client) generates an encryption key and optionally encrypts files. It then sends the key to a remote server, represented by the `server.py` script, which listens for connections and logs the received key.

## File Descriptions

- **encryptor.py**:  
  - Generates a Fernet (AES) encryption key.
  - Contains an optional block (commented out by default) for encrypting files in a directory.
  - Connects to a remote server using TCP sockets to send the encryption key.
  - Optionally deletes itself after running.

- **server.py**:  
  - Sets up a TCP server that listens for incoming connections.
  - Receives the encryption key sent by `encryptor.py`.
  - Logs the received key and sends a simple acknowledgment to the client.

## Usage Instructions

1. **For Testing Purposes:**
   - Use a safe environment (virtual machine or isolated test system) to run these scripts.
   - **Do not** run the encryption routine on actual system drives without careful modifications.

2. **Running the Server:**
   - Open a terminal and navigate to the `RWARE` folder.
   - Run the server:
     ```bash
     python server.py
     ```
   - The server will start and listen on port `4000` for incoming connections.

3. **Running the Client:**
   - In another terminal, navigate to the `RWARE` folder.
   - Run the client:
     ```bash
     python encryptor.py
     ```
   - The client will generate an encryption key and attempt to send it to the server.
   - **Note:** The file encryption section is commented out by default to prevent accidental damage. Uncomment it only for controlled testing.

## Setup

- **Dependencies:**
  - Python 3.x
  - [cryptography](https://pypi.org/project/cryptography/)

- **Installation:**
  1. Install Python 3 if not already installed.
  2. Install the required Python package:
     ```bash
     pip install cryptography
     ```

- **Configuration:**
  - Modify the host details in `encryptor.py` if needed. The current setup uses a dynamic DNS (e.g., `ved.hopto.org`). For testing, you can use `localhost` or another dummy host.
  - The encryption code block and self-deletion command in `encryptor.py` are commented out for safety.

## Disclaimer

This project is for educational purposes only. The code is a proof-of-concept and should **not** be used in production or for any malicious activities. The author accepts no responsibility for any damage or legal issues arising from the misuse of this code.


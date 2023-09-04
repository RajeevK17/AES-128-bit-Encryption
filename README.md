# File Encryption Using Fernet in Python

![Encryption](link_to_image)

## Overview

This Python script demonstrates file encryption using the Fernet symmetric encryption algorithm. Fernet encryption is a legitimate technique for securing data, but it is essential to emphasize ethical and responsible usage.

## Key Components

1. **Library Imports**:
   - The script imports the `cryptography.fernet` library for Fernet encryption and the `os` module for directory operations.

2. **Listing Files**:
   - It identifies files in the current directory to encrypt, excluding specific files (`'malware.py'`, `'filekey.key'`, `'decrypt.py'`, and `'1.readme.txt'`).

3. **Key Generation**:
   - The script generates an encryption key using Fernet's `generate_key()` method and saves it in `'filekey.key'`. This key will be used for both encryption and decryption.

4. **File Encryption**:
   - For each identified file, the script reads the original content and encrypts it using the generated key (`Fernet(key).encrypt(content)`).
   - The encrypted content overwrites the original file.

5. **Message**:
   - The script leaves a plaintext message in `'1.readme.txt'`, stating, "All of your files have been encrypted!!!"

## Ethical Usage

It is essential to understand that this code showcases a legitimate encryption technique. However, its usage should adhere to ethical and legal standards. Encryption should only be used for lawful purposes, such as data protection and privacy assurance.

**DO NOT** use this code for any malicious or illegal activities, including creating malware, unauthorized data access, or any actions that violate ethical and legal standards. Misuse of encryption can result in severe legal consequences.

Please ensure responsible usage of this code, with explicit consent when encrypting files owned by others.

# Decryption
Kindly check decrpyt.py to decrpyt the files and makes sure you generates key everytime you encrpyt the files otherwise ypu'll lose your data forever.

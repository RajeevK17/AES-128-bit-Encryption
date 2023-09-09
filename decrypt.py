from cryptography.fernet import Fernet
import os

with open('filekey.key', 'r') as f:
   key = f.read()

files = []

for file in os.listdir():

   if file == 'encrypt.py' or file == 'filekey.key' or file == 'decrypt.py' or file == '1.readme.txt':
      continue

   else:
      files.append(file)

for file in files:

   with open(file, 'rb') as f:
      content = f.read()

   decrypted_content = Fernet(key).decrypt(content)

   # Now, write the decrypted content back to the file
   with open(file, 'wb') as f:
      f.write(decrypted_content)

# Removing our message
os.remove('1.readme.txt')

# Removing the key as it's no longer required
os.remove('filekey.key')
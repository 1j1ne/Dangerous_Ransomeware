# !usr/bin/env python3

import os

from cryptography.fernet import Fernet, InvalidToken

import tkinter as tk
from tkinter import messagebox
import base64

All_files = []

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    visible_file = [f for f in files if not f.startswith(".")]

    for thefile in visible_file:
            path = os.path.join(root,thefile)
            
            if path == "./encrypting.py" or path == "./key.key" or path == "./decrypting.py":
                continue
            All_files.append(path)



with open("key.key", "rb") as thekey:
    secretkey = thekey.read()


secretphase = "bWFybW90Cg=="

user_phase = input("Enter secret phase to decrypt the files!\n")

print(base64.b64decode(secretphase).decode("utf-8").strip())

if base64.b64decode(secretphase).decode("utf-8").strip() == user_phase:

    for file in All_files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        
        try:
            content_decrypted = Fernet(secretkey).decrypt(content)
            with open(file, "wb") as thefile:
                thefile.write(content_decrypted)
        
        except InvalidToken:
            print("wrong token")



    # root = tk.Tk()
    # root.withdraw()

    # messagebox.showinfo("Your data is decrypted!", "Good Job")

else: 
    # root = tk.Tk()
    # root.withdraw()

    # messagebox.showinfo("Your data is not decrypted!", "Not even close! contact Yunchae!")

    print("no")
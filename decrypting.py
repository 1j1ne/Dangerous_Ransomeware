# !usr/bin/env python3

import os

from cryptography.fernet import Fernet

import tkinter as tk
from tkinter import messagebox

All_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root,file)
        dirs[:] = [d for d in dirs if d != ".git"]
        
        if path == "./encrypting.py" or path == "./key.key" or path == "./decrypting.py":
            continue
        All_files.append(path)



with open("key.key", "rb") as thekey:
    secretkey = thekey.read()



secretphase = "marmot"

user_phase = input("Enter secret phase to decrypt the files!\n")

if secretphase == user_phase:



    for file in All_files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        
        content_decrypted = Fernet(secretkey).decrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_decrypted)

    # root = tk.Tk()
    # root.withdraw()

    # messagebox.showinfo("Your data is decrypted!", "Good Job")

else: 
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Your data is not decrypted!", "Not even close! contact Yunchae!")
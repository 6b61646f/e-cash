import filecmp
import os
import ed25519
import hashlib
import time
from nacl.signing import SigningKey 
from nacl.encoding import HexEncoder

n = 3
file1 = open("solicitation.txt")
file2 = open("temp3.txt", "w")
content = file1.readlines()
count = 0
for line in content:
    if count<n:
        file2.write(line)
        count+=1
file2.close()
with open("temp3.txt", "r+") as text_file:
    texts = text_file.read()
    texts = texts.replace("from =", "owner =")
with open("temp3.txt", "w") as text_file:
    text_file.write(texts)

fd=open("temp3.txt","r")
d=fd.read()
fd.close()
m=d.split("\n")
s="\n".join(m[:-1])
fd=open("temp3.txt","w+")
for i in range(len(s)):
    fd.write(s[i])
fd.close()

n = 3
file1 = open("receipt.txt")
file2 = open("temp4.txt", "w")
content = file1.readlines()
count = 0
for line in content:
    if count<n:
        file2.write(line)
        count+=1
file2.close()
fd=open("temp4.txt","r")
d=fd.read()
fd.close()
m=d.split("\n")
s="\n".join(m[:-1])
fd=open("temp4.txt","w+")
for i in range(len(s)):
    fd.write(s[i])
fd.close()

f1 = "temp3.txt"
f2 = "temp4.txt"

result = filecmp.cmp(f1, f2)
if result == True:
    fileName2 = 'receipt.txt'
    text2 = 'owner'
    fileHandle2 = open(fileName2, "r")
    lines2 = fileHandle2.readlines()
    for line2 in lines2:
        if text2 in line2:
            with open('ownertemp.txt', 'w') as temppubKey:
                print(line2.replace('owner = ', '').replace('\n', ''), file=temppubKey, end='')
        fileHandle2.close()
    with open("ownertemp.txt", mode='rb') as file2:
        fileContent3 = file2.read()    
    pubKey = ed25519.VerifyingKey(fileContent3, encoding="hex")
    fileName = 'solicitation.txt'
    text = 'signature'
    fileHandle = open(fileName, "r")
    lines = fileHandle.readlines()
    for line in lines:
        if text in line:
            with open('signtemp.txt', 'w') as tempsg:
                print(line.replace('signature = ', '').replace('\n', ''), file=tempsg, end='')
        fileHandle.close()
    with open("signtemp.txt", mode='rb') as file:
        fileContent2 = file.read()
    signature = fileContent2

    lines = []
    with open("solicitation.txt", 'r') as fp:
        lines = fp.readlines()

    with open("solicitationtemp.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [5]:
                fp.write(line)

    fd=open("solicitationtemp.txt","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("solicitationtemp.txt","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
    fHash = open("hash.txt", "w")
    print(hashlib.blake2b(open('solicitationtemp.txt','rb').read()).hexdigest(), file=fHash, end ='')
    fHash.close()
    with open("hash.txt", mode='rb') as file:
        fileContent = file.read()
    msg = fileContent

    try:
        pubKey.verify(signature, msg, encoding='hex')
        print("The signature is valid.")
        now_ms = int( time.time_ns() / 1000 )
        n = 4
        file1 = open("solicitation.txt")
        file2 = open("newreceipt.txt", "w")
        content = file1.readlines()
        count = 0
        for line in content:
            if count<n:
                file2.write(line)
                count+=1
        print("time_stamp =", now_ms, file=file2, end='')
        file2.close()
        with open("newreceipt.txt", "r+") as text_file:
            texts = text_file.read()
            texts = texts.replace("to =", "owner =")
        with open("newreceipt.txt", "w") as text_file:
            text_file.write(texts)
        with open("newreceipt.txt", "r") as input:
            with open("temp.txt", "w") as output:
                for line in input:
                    if "from" not in line.strip("\n"):
                        output.write(line)
        os.replace('temp.txt', 'newreceipt.txt')
        fHash2 = open("hash2.txt", "w")
        print(hashlib.blake2b(open('newreceipt.txt','rb').read()).hexdigest(), file=fHash2, end ='')
        fHash2.close()
        with open("hash2.txt", mode='rb') as file:
            fileContent = file.read()
            with open('master.key', mode='rb') as privKey:
                            secretKey = privKey.read()
                            key = HexEncoder.decode(secretKey)
                            signingkey = SigningKey(key)
                            signed = signingkey.sign(fileContent)
                            with open("newreceipt.txt", "a") as data2:
                                print('\nsignature =', signed[: 64].hex(), file=data2, end='')
        os.remove("hash2.txt")
        os.remove("ownertemp.txt")
    except:
        print("Invalid signature!")

    os.remove("solicitationtemp.txt")
    os.remove("hash.txt")
    os.remove("signtemp.txt")
else:
    print("Bad")

os.remove("temp3.txt")
os.remove("temp4.txt")
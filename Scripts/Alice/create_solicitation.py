from nacl.signing import SigningKey 
from nacl.encoding import HexEncoder
import hashlib
import os
import time
now_ms = int( time.time_ns() / 1000 )
n = 3
file1 = open("receipt.txt")
file2 = open("solicitation.txt", "w")
content = file1.readlines()
count = 0
for line in content:
    if count<n:
        file2.write(line)
        count+=1
with open('pub.key') as pubKey:
    sike = pubKey.read().split()[0]
    print("to =", sike, file=file2)
    with open("pub.key", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
print("time_stamp =", now_ms, file=file2, end='')
file2.close()
with open("solicitation.txt", "r+") as text_file:
    texts = text_file.read()
    texts = texts.replace("owner =", "from =")
with open("solicitation.txt", "w") as text_file:
    text_file.write(texts)

# Open solicitation, hashed in blake2b and saved in a temp file called hash.txt
fHash = open("hash.txt", "w")
print(hashlib.blake2b(open('solicitation.txt','rb').read()).hexdigest(), file=fHash, end ='')
fHash.close()
with open("hash.txt", mode='rb') as file:
    fileContent = file.read()
   # From the solicitation file take the pubKey from the line "from" and search in the used.key the privKey that correspond
    fileName = 'solicitation.txt'
    text = 'from'
    fileHandle = open(fileName, "r")
    lines = fileHandle.readlines()
    for line in lines:
        if text in line:
            with open('temppk.txt', 'w') as temppk:
                print(line.replace('from = ', '').replace('\n', ''), file=temppk, end='')
        fileHandle.close()
    fileName2 = 'used.key'
    with open("temppk.txt", mode='r') as file1:
        fileContent2 = file1.read()
    fileHandle2 = open(fileName2, "r")
    lines2 = fileHandle2.readlines()
    for line2 in lines2:
        if fileContent2 in line2:
            with open('tempsk.txt', 'w') as tempsk:
                print(line2.replace(fileContent2, '').replace(' | ', '').replace('\n', ''), file=tempsk, end='')
                tempsk.close()
                # Sign the file with the privKey founded in used.key and the hash previously created
                with open('tempsk.txt', mode='rb') as privKey:
                    secretKey = privKey.read()
                    key = HexEncoder.decode(secretKey)
                    signingkey = SigningKey(key)
                    signed = signingkey.sign(fileContent)
                    with open("solicitation.txt", "a") as data2:
                        print('\nsignature =', signed[: 64].hex(), file=data2, end='')
    fileHandle2.close()
os.remove("hash.txt")
os.remove("tempsk.txt")
os.remove("temppk.txt")
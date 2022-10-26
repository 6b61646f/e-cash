with open('new.key') as pubKey:
    with open("pub.key", "a") as pubkey:
        print(pubKey.read().split()[0], file=pubkey)

printline = 1
lineCounter = 0
with open('new.key','r') as f:
    with open("used.key", "a") as usedkey:
        for line in f:
            lineCounter += 1
            if lineCounter == printline:
                print(line, file=usedkey, end='')
                with open("new.key", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != line:
                            f.write(i)
                    f.truncate()

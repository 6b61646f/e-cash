from nacl.signing import SigningKey
from nacl.encoding import HexEncoder
sk = SigningKey.generate()
vk = sk.verify_key
with open('new.key', 'a') as f:
    print(vk.encode(HexEncoder()).decode(),'|', sk.encode(HexEncoder()).decode(), file=f)
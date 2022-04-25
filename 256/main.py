from hashlib import sha256
flag = open("flag.txt", "rb").read()
for byte in flag:
    print(sha256(bytes([byte])).hexdigest())
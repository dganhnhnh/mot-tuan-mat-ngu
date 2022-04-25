from Crypto.Util.number import long_to_bytes

##### encryption #####
A = 0x0000000000000000000001000000000000000000000000000000000000000163
S = 0xdd268dbcaac550362d98c384c4e576ccc8b1536847b6bbb31023b4c8caee0535 
n = 256
def encrypt_block(block: bytes):
    enc_block = S
    for byte in block:
        enc_block = ((A*enc_block) ^ byte) & ((1<<n) - 1)
    return long_to_bytes(enc_block, n//8)

BLOCKSIZE = n//9
def encrypt(data: bytes):
    enc = b''
    for i in range(0, len(data), BLOCKSIZE):
        enc += encrypt_block(data[i:i+BLOCKSIZE])
    return enc

##### challenge #####
print(encrypt(open("flag.txt", "rb").read()).hex())
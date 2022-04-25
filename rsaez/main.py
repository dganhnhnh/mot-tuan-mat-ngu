from sage.all           import *
from Crypto.Util.number import *

p = getPrime(1024)
q = getPrime(1024)
N = p*q
e = 5

flag = open("flag.txt", "rb").read()
msg=bytes_to_long(flag)

# c=pow(msg, e, N)
c=pow(msg,e)

print(f'e = {e}')
print(f'N = {N}')
print(f'l = {len(flag)}')
print(f'c = {c}')


phi=(p-1)*(q-1)

d=pow(e,-1,phi)
msg=pow(c,d,N)

from Crypto.Util.number import *

def mix(data):
    b = len(data)*8
    m = bytes_to_long(data)
    c = 0
    for _ in range(b//2):       #get division of floating point values
        if (m >> _) & 1:
            c ^= m >> (b//2) << _
    return c



# flag = open("flag.txt", "rb").read()
# a1=b'a'
a2=b'abcs'

# print(f'{str(a2)}: {bytes_to_long(a2)}')
# print('little: ',int.from_bytes(a2,byteorder='little'))        
# print('big: ',int.from_bytes(a2,byteorder='big'))        

# print(mix(a1))
print(mix(a2))


# c=6942898839970185178260073539872686823033540616179568772534193638792863984577319801408327713407779249828819087800803420064518242859606213564691040797518
# print(long_to_bytes(c))
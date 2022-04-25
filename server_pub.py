from Crypto.Util import number

flag = b'# CENSOR #'
# 1 bytes 
sbox = [0, 182, 181, 3, 16, 166, 165, 19, 195, 117, 118, 192, 211, 101, 102, 208, 105, 223, 220, 106, 121, 207, 204, 122, 170, 28, 31, 169, 186, 12, 15, 185, 85, 227, 224, 86, 69, 243, 240, 70, 150, 32, 35, 149, 134, 48, 51, 133, 60, 138, 137, 63, 44, 154, 153, 47, 255, 73, 74, 252, 239, 89, 90, 236, 131, 53, 54, 128, 147, 37, 38, 144, 64, 246, 245, 67, 80, 230, 229, 83, 234, 92, 95, 233, 250, 76, 79, 249, 41, 159, 156, 42, 57, 143, 140, 58, 214, 96, 99, 213, 198, 112, 115, 197, 21, 163, 160, 22, 5, 179, 176, 6, 191, 9, 10, 188, 175, 25, 26, 172, 124, 202, 201, 127, 108, 218, 217, 111, 20, 162, 161, 23, 4, 178, 177, 7, 215, 97, 98, 212, 199, 113, 114, 196, 125, 203, 200, 126, 109, 219, 216, 110, 190, 8, 11, 189, 174, 24, 27, 173, 65, 247, 244, 66, 81, 231, 228, 82, 130, 52, 55, 129, 146, 36, 39, 145, 40, 158, 157, 43, 56, 142, 141, 59, 235, 93, 94, 232, 251, 77, 78, 248, 151, 33, 34, 148, 135, 49, 50, 132, 84, 226, 225, 87, 68, 242, 241, 71, 254, 72, 75, 253, 238, 88, 91, 237, 61, 139, 136, 62, 45, 155, 152, 46, 194, 116, 119, 193, 210, 100, 103, 209, 1, 183, 180, 2, 17, 167, 164, 18, 171, 29, 30, 168, 187, 13, 14, 184, 104, 222, 221, 107, 120, 206, 205, 123]
block_size = 8# bytes
pbox = [3, 5, 4, 1, 0, 7, 2, 6]

def encrypt_1_block(key,data):
	for round_ in range(4):
		# data = [sbox[c] for c in data]
		# data = [data[c] for c in pbox]
		data = [a^b for a,b in zip(data,key)]
	return bytes(data)

def generate_key_stream(key,data):
	while True:
		for c in encrypt_1_block(key,data.to_bytes(8,'big')):
			yield c
		data+=1

def encrypt_ctr(data,key,nonce=0):
	ciphertext = []
	for c,key_stream in zip(data,generate_key_stream(key,nonce)):
		ciphertext.append(c^key_stream)
	return nonce, bytes(ciphertext)

if __name__=='__main__':
	key = number.getRandomNBitInteger(64).to_bytes(8,'big')
	print("Wellcome to the encrypt-service:")
	nonce,ciphertext = encrypt_ctr(flag,key,number.getRandomNBitInteger(64))
	print("This is your ciphertext:",(nonce,ciphertext.hex()))
	while True:
		message = bytes.fromhex(input("Give me message in hex:"))
		nonce,ciphertext = encrypt_ctr(message,key,number.getRandomNBitInteger(64))
		print("This is your ciphertext:",(nonce,ciphertext.hex()))
	
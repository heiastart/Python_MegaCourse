from Crypto.Cipher import AES

obj = AES.new('this is a key123', AES.MODE_CBC, 'this is an IV456')
message = input('Type message to be encrypted: ')
ciphertext = obj.encrypt(message)
print(ciphertext)

obj2 = AES.new('this is a key123', AES.MODE_CBC, 'this is an IV456')
plaintext = obj2.decrypt(ciphertext)
print(plaintext)
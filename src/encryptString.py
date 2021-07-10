# CryptPy - Ivan Chen
# CryptPy is a series of standalone scripts for encryption and decryption of files / strings. 

from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

message = input("Message: ")
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encrypted)
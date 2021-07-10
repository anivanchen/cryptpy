# CryptPy - Ivan Chen
# CryptPy is a series of standalone scripts for encryption and decryption of files / strings. 

from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

message = input('Encrypted String: ')

f = Fernet(key)
decrypted = f.decrypt(message)

decrypted = decrypted.decode()
print(decrypted)
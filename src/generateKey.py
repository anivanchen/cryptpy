# CryptPy - Ivan Chen
# CryptPy is a series of standalone scripts for encryption and decryption of files / strings. 

from cryptography.fernet import Fernet
key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key)
file.close()
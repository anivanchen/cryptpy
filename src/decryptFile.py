# CryptPy - Ivan Chen
# CryptPy is a series of standalone scripts for encryption and decryption of files / strings. 

from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

with open('file.txt.encrypted', 'rb') as f: 
    data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)

with open('file.txt', 'wb') as f: 
    f.write(decrypted)
from Crypto.Cipher import AES
from Crypto.Util import Counter

key = b'1234567890123456'

ctr = Counter.new(128)

cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

plaintext = b'HELLOSAJID'

ciphertext = cipher.encrypt(plaintext)
print("Cipher:", ciphertext)

# Decrypt
ctr = Counter.new(128)
decipher = AES.new(key, AES.MODE_CTR, counter=ctr)

decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
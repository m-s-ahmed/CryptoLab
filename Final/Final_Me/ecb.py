from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Step 1: key define (16 byte)
key = b'1234567890123456'

# Step 2: ECB mode create
cipher = AES.new(key, AES.MODE_ECB)

# Step 3: plaintext
plaintext = b'HELLOSAJID'

# Step 4: padding (must, because block size = 16)
padded = pad(plaintext, 16)

# Step 5: encrypt
ciphertext = cipher.encrypt(padded)

print("Cipher:", ciphertext)

# 🔓 Decryption
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), 16)

print("Decrypted:", decrypted)
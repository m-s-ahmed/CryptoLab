from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Step 1: key
key = b'1234567890123456'

# Step 2: IV (random)
iv = get_random_bytes(16)

# Step 3: create cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

# Step 4: plaintext
plaintext = b'HELLOSAJID'

# Step 5: padding
padded = pad(plaintext, 16)

# Step 6: encrypt
ciphertext = cipher.encrypt(padded)

print("Cipher:", ciphertext)

#  Decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), 16)

print("Decrypted:", decrypted)
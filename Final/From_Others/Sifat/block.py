from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key must be exactly 8 bytes (64 bits)
key = b'8bytekey'

# Create DES cipher (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b'HelloDES'

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext, 8))
print("Ciphertext:", ciphertext)

# Decrypt
decrypted = unpad(cipher.decrypt(ciphertext), 8)
print("Decrypted:", decrypted)
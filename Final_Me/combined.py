
#pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter

# 🔐 function to make key 16 bytes
def make_key(user_key):
    key = user_key.encode()
    return key.ljust(16, b'0')[:16]   # fix size = 16 bytes

# 📥 User Input
user_key = input("Enter key: ")
plaintext = input("Enter plaintext: ").encode()

key = make_key(user_key)

print("\nChoose Mode:")
print("1. ECB")
print("2. CBC")
print("3. CFB")
print("4. OFB")
print("5. CTR")

choice = input("Enter choice (1-5): ")

# ================= ECB =================
if choice == '1':
    print("\n--- ECB MODE ---")
    cipher = AES.new(key, AES.MODE_ECB)

    padded = pad(plaintext, 16)
    ciphertext = cipher.encrypt(padded)
    print("Cipher:", ciphertext)

    decipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(decipher.decrypt(ciphertext), 16)
    print("Decrypted:", decrypted)

# ================= CBC =================
elif choice == '2':
    print("\n--- CBC MODE ---")
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext, 16)
    ciphertext = cipher.encrypt(padded)

    print("IV:", iv)
    print("Cipher:", ciphertext)

    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(decipher.decrypt(ciphertext), 16)
    print("Decrypted:", decrypted)

# ================= CFB =================
elif choice == '3':
    print("\n--- CFB MODE ---")
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)

    print("IV:", iv)
    print("Cipher:", ciphertext)

    decipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)

# ================= OFB =================
elif choice == '4':
    print("\n--- OFB MODE ---")
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext)

    print("IV:", iv)
    print("Cipher:", ciphertext)

    decipher = AES.new(key, AES.MODE_OFB, iv)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)

# ================= CTR =================
elif choice == '5':
    print("\n--- CTR MODE ---")

    ctr = Counter.new(128)

    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(plaintext)

    print("Cipher:", ciphertext)

    ctr = Counter.new(128)
    decipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)

else:
    print("Invalid choice!")

##M.S.AHMED
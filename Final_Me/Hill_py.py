import numpy as np

# text → number
def text_to_numbers(text):
    text = text.upper().replace(" ", "")
    return [ord(c) - 65 for c in text]

# number → text
def numbers_to_text(nums):
    return ''.join(chr(int(n) % 26 + 65) for n in nums)


# Encryption using C = P*K mod 26
def encrypt_pk(plain, key):

    n = key.shape[0]
    nums = text_to_numbers(plain)

    # padding
    while len(nums) % n != 0:
        nums.append(23)  # X padding

    nums = np.array(nums)

    cipher = []

    print("\nEncryption Block wise (C = P*K mod 26):\n")

    for i in range(0, len(nums), n):

        block = nums[i:i+n]

        plain_text_block = numbers_to_text(block)

        encrypted = np.dot(block, key) % 26

        cipher_text_block = numbers_to_text(encrypted)

        print("Plain Block Number :", block)
        print("Plain Block Text   :", plain_text_block)

        print("Cipher Block Number:", encrypted)
        print("Cipher Block Text  :", cipher_text_block)

        print()

        cipher.extend(encrypted)

    return numbers_to_text(cipher)



# Decryption using P = C*K⁻¹ mod 26
def decrypt_pk(cipher, key):

    n = key.shape[0]

    nums = np.array(text_to_numbers(cipher))

    det = int(round(np.linalg.det(key)))
    det_inv = pow(det, -1, 26)

    key_inv = det_inv * np.round(det * np.linalg.inv(key)).astype(int) % 26

    plain = []

    print("\nDecryption Block wise (P = C*K⁻¹ mod 26):\n")

    for i in range(0, len(nums), n):

        block = nums[i:i+n]

        cipher_text_block = numbers_to_text(block)

        decrypted = np.dot(block, key_inv) % 26

        plain_text_block = numbers_to_text(decrypted)

        print("Cipher Block Number:", block)
        print("Cipher Block Text  :", cipher_text_block)

        print("Plain Block Number :", decrypted)
        print("Plain Block Text   :", plain_text_block)

        print()

        plain.extend(decrypted)

    return numbers_to_text(plain)



# ===== USER INPUT =====

n = int(input("Enter matrix size: "))

print("Enter key matrix:")

key = []
for i in range(n):
    row = list(map(int, input().split()))
    key.append(row)

key = np.array(key)

plain = input("Enter Plain Text: ")


# ===== PROCESS =====

cipher = encrypt_pk(plain, key)

print("Final Cipher Text:", cipher)


decrypted = decrypt_pk(cipher, key)

print("Final Decrypted Text:", decrypted)
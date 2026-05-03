import string

def create_key_mapping(key):
    alphabet = string.ascii_lowercase
    
    if len(key) != 26 or not key.isalpha():
        print("Key must contain exactly 26 unique letters.")
        exit()
    
    key = key.lower()
    
    if len(set(key)) != 26:
        print("Key must not contain duplicate letters.")
        exit()
    
    encrypt_map = dict(zip(alphabet, key))
    decrypt_map = dict(zip(key, alphabet))
    
    return encrypt_map, decrypt_map


def encrypt(text, encrypt_map):
    result = ""
    
    for char in text:
        if char.islower():
            result += encrypt_map[char]
        elif char.isupper():
            result += encrypt_map[char.lower()].upper()
        else:
            result += char
    
    return result


def decrypt(cipher, decrypt_map):
    result = ""
    
    for char in cipher:
        if char.islower():
            result += decrypt_map[char]
        elif char.isupper():
            result += decrypt_map[char.lower()].upper()
        else:
            result += char
    
    return result


# -------- MAIN --------

key = input("Enter 26-letter key (substitution alphabet): ")
encrypt_map, decrypt_map = create_key_mapping(key)

text = input("Enter plaintext: ")

cipher = encrypt(text, encrypt_map)
print("Encrypted text:", cipher)

decrypted = decrypt(cipher, decrypt_map)
print("Decrypted text:", decrypted)
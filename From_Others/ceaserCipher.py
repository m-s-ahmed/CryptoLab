def encrypt(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char

    return result


# Example
plain_text = "Hello World"
key = 3
cipher_text = encrypt(plain_text, key)
print("Encrypted Text:", cipher_text)


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char

    return result


# Example
print("Decrypted Text:", decrypt(cipher_text, key))



def brute_force(cipher_text):
    print("Brute Force Results:\n")
    for key in range(26):
        print(f"Key {key}: {decrypt(cipher_text, key)}")


# Example
brute_force(cipher_text)

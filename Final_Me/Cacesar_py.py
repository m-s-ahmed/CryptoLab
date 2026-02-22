#define function for encryption
def encrypt(text, key):
    #empty string
    result = ""

    for char in text:
        if char.isupper():
            result =result + chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result =result + chr((ord(char) + key - 97) % 26 + 97)
        else:
            result = result+ char #special character keep as it is

    return result

#define function for decryption
def decrypt(text, key):
    #empty string
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char

    return result


def brute_force(cipher_text):
    print("\nBrute Force Results:\n")
    for key in range(26):
        print(f"Key {key}: {decrypt(cipher_text, key)}")



plain_text = input("Enter Plain Text: ")
key = int(input("Enter Key (0-25): "))

cipher_text = encrypt(plain_text, key)

print("Encrypted Text:", cipher_text)

print("Decrypted Text:", decrypt(cipher_text, key))

brute_force(cipher_text)
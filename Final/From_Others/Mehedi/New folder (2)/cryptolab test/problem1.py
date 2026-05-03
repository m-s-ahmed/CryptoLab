def caesar_encrypt(text, key):
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch

    return result


def caesar_decrypt(text, key):
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
        else:
            result += ch

    return result


def brute_force_attack(text):
    for key in range(26):
        temp = ""

        for ch in text:
            if 'A' <= ch <= 'Z':
                temp += chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
            elif 'a' <= ch <= 'z':
                temp += chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
            else:
                temp += ch

        print(f"Key {key}: {temp}")


# Main Program
text = input("Enter plain text: ")
key = input("Enter key: ")

key = ord(key.upper()) - ord('A')

cipher_text = caesar_encrypt(text, key)
print("\nEncrypted text:", cipher_text)

decrypted_text = caesar_decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)

print("\nResult for Brute Force Attack Results:")
brute_force_attack(cipher_text)
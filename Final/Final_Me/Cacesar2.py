# ---------- Caesar Cipher ----------

def encrypt(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result = result + chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result = result + chr((ord(char) + key - 97) % 26 + 97)
        else:
            result = result + char

    return result


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


def brute_force(cipher_text):
    print("\nBrute Force Results:\n")
    for key in range(26):
        print(f"Key {key}: {decrypt(cipher_text, key)}")


# ---------- USER MENU ----------

while True:
    choice = input("\nEnter EN (Encrypt) / DE (Decrypt) / BF (Brute Force) / EX (Exit): ").upper()

    if choice == "EN":
        plain_text = input("Enter Plain Text: ")
        key = int(input("Enter Key (0-25): "))

        cipher_text = encrypt(plain_text, key)
        print("Encrypted Text:", cipher_text)

    elif choice == "DE":
        cipher_text = input("Enter Cipher Text: ")
        key = int(input("Enter Key (0-25): "))

        plain_text = decrypt(cipher_text, key)
        print("Decrypted Text:", plain_text)

    elif choice == "BF":
        cipher_text = input("Enter Cipher Text: ")
        brute_force(cipher_text)

    elif choice == "EX":
        print("Program Ended.")
        break

    else:
        print("Invalid Option ❌")
def encrypt(text, key):
    result = ""
    text = text.lower()
    for char in text:
        if char.isalpha(): 
            shift = key % 26
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  
    
    return result


def decrypt(cipher, key):
    result = ""
    
    for char in cipher:
        if char.isalpha():
            shift = key % 26
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    
    return result

text = input("Enter text: ")
key = int(input("Enter key (shift value): "))

cipher = encrypt(text, key)
print("Encrypted text:", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted text:", decrypted)
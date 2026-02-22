def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text.lower():
        if char.isalpha():
            cipher_text += key[ord(char) - 97]
        else:
            cipher_text += char
    return cipher_text


key = "qwertyuiopasdfghjklzxcvbnm"  # substitution key
plain_text = "Mohiuddin Rahman Mukim"

encrypted = encrypt(plain_text, key)
print("Encrypted Text:", encrypted)



def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            plain_text += chr(key.index(char) + 97)
        else:
            plain_text += char
    return plain_text


decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)



#Frequency Analysis Program
from collections import Counter

def frequency_analysis(text):
    text = text.replace(" ", "")
    frequency = Counter(text)
    total = sum(frequency.values())

    for letter, count in frequency.most_common():
        print(f"{letter} : {count / total:.2f}")


print("\nFrequency Analysis:")
frequency_analysis(encrypted)



# Simple Breaking

def break_cipher(cipher_text):
    english_freq = "etaoinshrdlcumwfgypbvkjxqz"
    freq = Counter(cipher_text.replace(" ", ""))
    sorted_cipher = [x[0] for x in freq.most_common()]

    mapping = dict(zip(sorted_cipher, english_freq))

    result = ""
    for char in cipher_text:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    return result


print("\nBroken Text (Approx):")
print(break_cipher(encrypted))
# ---------- Helper Functions ----------

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


def power_mod(base, exp, mod):
    return pow(base, exp, mod)


def number_to_text(num):
    s = str(num)

    if len(s) % 2 != 0:
        s = "0" + s

    text = ""

    for i in range(0, len(s), 2):
        code = int(s[i:i+2])

        if 1 <= code <= 26:
            text += chr(code + 64)
        elif code == 27:
            text += " "
        else:
            text += "?"

    return text


def text_to_number(text):
    result = ""

    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            result += str(ord(ch) - 64).zfill(2)
        elif ch == " ":
            result += "27"

    return int(result)


# ---------- USER INPUT ----------

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
phi = (p - 1) * (q - 1)

print("\nCalculated n =", n)
print("Calculated phi(n) =", phi)

e = int(input("\nEnter public key e: "))

if gcd(e, phi) != 1:
    print("❌ e and phi(n) are not coprime. Choose another e.")
else:
    d = mod_inverse(e, phi)

    print("\n✅ Public Key (PU) =", (e, n))
    print("✅ Private Key (PR) =", (d, n))


    # ---------- Decryption ----------

    cipher_given = int(input("\nEnter Cipher to Decrypt: "))

    decrypted_number = power_mod(cipher_given, d, n)
    decrypted_text = number_to_text(decrypted_number)

    print("\nDecrypted Number =", decrypted_number)
    print("Decrypted Text =", decrypted_text)


    # ---------- Encryption ----------

    initials = input("\nEnter text to Encrypt (e.g., initials): ")

    message_number = text_to_number(initials)
    encrypted = power_mod(message_number, e, n)

    print("\nMessage Number =", message_number)
    print("Encrypted Number =", encrypted)
import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)

    if gcd != 1:
        return None

    return x % phi

def get_valid_e_values(phi):
    valid_e = []
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            valid_e.append(e)
    return valid_e

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def generate_keys():
    print("Enter two prime numbers:")
    p = int(input("p = "))
    q = int(input("q = "))

    if not (is_prime(p) and is_prime(q)):
        print("P & q must be prime")
        exit()

    n = p * q
    phi = (p - 1) * (q - 1)

    print("\nComputed values:")
    print("n =", n)
    print("phi(n) =", phi)

    valid_e = get_valid_e_values(phi)

    print("\nAvailable values of e (coprime with phi):")
    print(valid_e)

    e = int(input("\nChoose e from the above list: "))

    if e not in valid_e:
        print("Invalid choice of e.")
        exit()

    d = mod_inverse(e, phi)

    print("\nPublic Key (e, n):", (e, n))
    print("Private Key (d, n):", (d, n))

    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    decrypted = ''.join([chr(pow(char, d, n)) for char in cipher])
    return decrypted

public_key, private_key = generate_keys()

message = input("\nEnter message to encrypt: ")

cipher_text = encrypt(message, public_key)
print("\nEncrypted message:", cipher_text)

decrypted_message = decrypt(cipher_text, private_key)
print("\nDecrypted message:", decrypted_message)
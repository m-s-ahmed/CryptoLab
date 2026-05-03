# Elliptic Curve Cryptography (ECC)
# No external libraries used

# Curve parameters
p = 97
a = 2
b = 3

# Base Point
G = (3, 6)

# Point at infinity
O = None


# Modular Inverse using Extended Euclidean Algorithm
def mod_inverse(k, p):
    if k == 0:
        raise ZeroDivisionError("Division by zero")

    s, old_s = 0, 1
    r, old_r = p, k

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    return old_s % p


# Check if point is on curve
def is_on_curve(P):
    if P is None:
        return True

    x, y = P
    return (y*y - (x*x*x + a*x + b)) % p == 0


# Point Addition
def point_add(P, Q):

    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P) = O
    if x1 == x2 and y1 != y2:
        return None

    # Point doubling
    if P == Q:

        m = (3*x1*x1 + a) * mod_inverse(2*y1, p) % p

    else:

        m = (y2 - y1) * mod_inverse(x2 - x1, p) % p


    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p

    return (x3, y3)


# Scalar Multiplication
def scalar_mult(k, P):

    result = None
    addend = P

    while k:

        if k & 1:
            result = point_add(result, addend)

        addend = point_add(addend, addend)

        k >>= 1

    return result


# Key Generation
def generate_keys():

    private_key = 7   # choose random in practice
    public_key = scalar_mult(private_key, G)

    return private_key, public_key


# Encryption (ECC ElGamal)
def encrypt(M, public_key):

    k = 3   # random number

    C1 = scalar_mult(k, G)

    S = scalar_mult(k, public_key)

    C2 = point_add(M, S)

    return C1, C2


# Decryption
def decrypt(C1, C2, private_key):

    S = scalar_mult(private_key, C1)

    x, y = S
    S_neg = (x, (-y) % p)

    M = point_add(C2, S_neg)

    return M



# ---------------- TEST ----------------

# Message as a point on curve
M = (80, 10)

print("Message:", M)

# Generate keys
priv, pub = generate_keys()

print("Private Key:", priv)
print("Public Key:", pub)

# Encrypt
C1, C2 = encrypt(M, pub)

print("\nCipher:")
print("C1 =", C1)
print("C2 =", C2)

# Decrypt
decrypted = decrypt(C1, C2, priv)

print("\nDecrypted:", decrypted)

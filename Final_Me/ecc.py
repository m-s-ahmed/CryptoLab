# -------------------------------0
# Point Structure
# -------------------------------
class Point:
    def __init__(self, x=0, y=0, infinity=False):
        self.x = x
        self.y = y
        self.infinity = infinity

    def __str__(self):
        if self.infinity:
            return "Point at Infinity"
        return f"({self.x}, {self.y})"


# -------------------------------
# Modular arithmetic
# -------------------------------
def mod(a, p):
    return (a % p + p) % p


def mod_inverse(a, p):
    a = mod(a, p)
    for i in range(1, p):
        if mod(a * i, p) == 1:
            return i
    return -1


def infinity_point():
    return Point(0, 0, True)


# -------------------------------
# Check if point lies on curve
# -------------------------------
def is_on_curve(P, a, b, p):
    if P.infinity:
        return True
    return mod(P.y * P.y, p) == mod(P.x**3 + a * P.x + b, p)


# -------------------------------
# Point Addition
# -------------------------------
def point_add(P, Q, a, p):
    if P.infinity:
        return Q
    if Q.infinity:
        return P

    if P.x == Q.x and mod(P.y + Q.y, p) == 0:
        return infinity_point()

    if P.x == Q.x and P.y == Q.y:
        num = mod(3 * P.x * P.x + a, p)
        den = mod_inverse(2 * P.y, p)
        lam = mod(num * den, p)
    else:
        num = mod(Q.y - P.y, p)
        den = mod_inverse(Q.x - P.x, p)
        lam = mod(num * den, p)

    xr = mod(lam * lam - P.x - Q.x, p)
    yr = mod(lam * (P.x - xr) - P.y, p)

    return Point(xr, yr)


# -------------------------------
# Scalar Multiplication
# -------------------------------
def scalar_multiply(P, k, a, p):
    result = infinity_point()
    while k > 0:
        if k & 1:
            result = point_add(result, P, a, p)
        P = point_add(P, P, a, p)
        k >>= 1
    return result


# -------------------------------
# Compute Order of Generator
# -------------------------------
def compute_order(G, a, p):
    temp = G
    n = 1
    while not temp.infinity:
        temp = point_add(temp, G, a, p)
        n += 1
    return n


# -------------------------------
# Display all affine points
# -------------------------------
def display_all_affine_points(a, b, p):
    print("\n=== All Affine Points on the Curve ===")
    count = 0

    for x in range(p):
        y_squared = mod(x**3 + a*x + b, p)
        for y in range(p):
            if mod(y*y, p) == y_squared:
                print(f"({x}, {y})")
                count += 1

    print("Point at Infinity")
    print("Total Affine Points:", count + 1)


# -------------------------------
# XOR Encryption
# -------------------------------
def encrypt_decrypt(message, key):
    result = ""
    for ch in message:
        result += chr(ord(ch) ^ (key % 256))
    return result


# ===============================
# MAIN PROGRAM
# ===============================
if __name__ == "__main__":

    a = int(input("Enter curve parameter a: "))
    b = int(input("Enter curve parameter b: "))
    p = int(input("Enter prime p: "))

    # Check curve validity
    if (4 * a**3 + 27 * b**2) % p == 0:
        print("Invalid curve!")
        exit()

    display_all_affine_points(a, b, p)

    # Generator input
    while True:
        gx = int(input("Enter Generator Gx: "))
        gy = int(input("Enter Generator Gy: "))
        G = Point(gx, gy)

        if is_on_curve(G, a, b, p):
            break
        print("Point is NOT on curve. Try again.")

    n = compute_order(G, a, p)
    print("Order of Generator (n) =", n)

    # Private keys
    alpha = int(input("Enter Alice private key (1 <= alpha < n): "))
    beta = int(input("Enter Bob private key (1 <= beta < n): "))

    PA = scalar_multiply(G, alpha, a, p)
    PB = scalar_multiply(G, beta, a, p)

    print("\nAlice Public Key:", PA)
    print("Bob Public Key:", PB)

    sharedA = scalar_multiply(PB, alpha, a, p)
    sharedB = scalar_multiply(PA, beta, a, p)

    print("\nShared Secret (Alice):", sharedA)
    print("Shared Secret (Bob):  ", sharedB)

    if sharedA.x == sharedB.x and sharedA.y == sharedB.y:
        print("\nKey Exchange Successful!")
    else:
        print("\nKey Exchange Failed!")
        exit()

    symmetric_key = sharedA.x

    message = input("\nEnter Message: ")

    encrypted = encrypt_decrypt(message, symmetric_key)
    print("Encrypted:", encrypted)

    decrypted = encrypt_decrypt(encrypted, symmetric_key)
    print("Decrypted:", decrypted)
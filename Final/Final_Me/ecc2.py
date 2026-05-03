# ECC Encryption Code

# ---------- Modular Inverse ----------
def mod_inverse(a, p):
    a = a % p
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return None


# ---------- Point Addition ----------
def point_add(P, Q, a, p):
    # Point at infinity
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P) = infinity
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # P == Q : point doubling
    if P == Q:
        numerator = (3 * x1 * x1 + a) % p
        denominator = (2 * y1) % p
    else:
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

    inv_denominator = mod_inverse(denominator, p)

    if inv_denominator is None:
        return None

    lam = (numerator * inv_denominator) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


# ---------- Scalar Multiplication ----------
def scalar_multiply(k, P, a, p):
    result = None
    addend = P

    while k > 0:
        if k % 2 == 1:
            result = point_add(result, addend, a, p)

        addend = point_add(addend, addend, a, p)
        k = k // 2

    return result


# ---------- Calculate n / Order of G ----------
def calculate_n(G, a, p):
    current = G
    n = 1

    while current is not None:
        current = point_add(current, G, a, p)
        n += 1

    return n


# ---------- ECC Encryption ----------
def ecc_encrypt(Pm, G, Pb, k, a, p):
    first_part = scalar_multiply(k, G, a, p)
    kPb = scalar_multiply(k, Pb, a, p)
    second_part = point_add(Pm, kPb, a, p)

    return first_part, second_part


# ---------- USER INPUT ----------
p = int(input("Enter p: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

gx = int(input("Enter G x: "))
gy = int(input("Enter G y: "))
G = (gx, gy)

pmx = int(input("Enter PM x: "))
pmy = int(input("Enter PM y: "))
Pm = (pmx, pmy)

k = int(input("Enter k: "))

pbx = int(input("Enter PB x: "))
pby = int(input("Enter PB y: "))
Pb = (pbx, pby)


# ---------- PROCESS ----------
n = calculate_n(G, a, p)

G_plus_PM = point_add(G, Pm, a, p)

kg = scalar_multiply(k, G, a, p)

kPb = scalar_multiply(k, Pb, a, p)

cipher = ecc_encrypt(Pm, G, Pb, k, a, p)


# ---------- OUTPUT ----------
print("\n----- ECC Result -----")
print("Curve: E_" + str(p) + "(" + str(a) + "," + str(b) + ")")
print("G =", G)
print("n =", n)
print("PM =", Pm)
print("k =", k)
print("PB =", Pb)

print("\nG + PM =", G_plus_PM)
print("kG =", kg)
print("kPB =", kPb)

print("\nCipher Text PC = [", cipher[0], ",", cipher[1], "]")
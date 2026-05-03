# -------------------------------
# Point Structure
# -------------------------------
class Point:
    def __init__(self, x=0, y=0, infinity=False):
        self.x = x
        self.y = y
        self.infinity = infinity


# -------------------------------
# Modular Arithmetic
# -------------------------------
def mod(a, p):
    return (a % p + p) % p


def modInverse(a, p):
    a = mod(a, p)
    for i in range(1, p):
        if mod(a * i, p) == 1:
            return i
    return -1


# -------------------------------
# Special Point (Infinity)
# -------------------------------
def infinityPoint():
    return Point(0, 0, True)


# -------------------------------
# Check if point lies on curve
# -------------------------------
def isOnCurve(P, a, b, p):
    if P.infinity:
        return True
    return mod(P.y * P.y, p) == mod(P.x * P.x * P.x + a * P.x + b, p)


# -------------------------------
# Point Addition
# -------------------------------
def pointAdd(P, Q, a, p):

    if P.infinity:
        return Q
    if Q.infinity:
        return P

    if P.x == Q.x and mod(P.y + Q.y, p) == 0:
        return infinityPoint()

    if P.x == Q.x and P.y == Q.y:
        num = mod(3 * P.x * P.x + a, p)
        den = modInverse(2 * P.y, p)
        lam = mod(num * den, p)
    else:
        num = mod(Q.y - P.y, p)
        den = modInverse(Q.x - P.x, p)
        lam = mod(num * den, p)

    xr = mod(lam * lam - P.x - Q.x, p)
    yr = mod(lam * (P.x - xr) - P.y, p)

    return Point(xr, yr, False)


# -------------------------------
# Scalar Multiplication (kP)
# -------------------------------
def scalarMultiply(P, k, a, p):
    result = infinityPoint()

    while k > 0:
        if k & 1:
            result = pointAdd(result, P, a, p)
        P = pointAdd(P, P, a, p)
        k >>= 1

    return result


# -------------------------------
# Compute Order of Generator
# -------------------------------
def computeOrder(G, a, p):
    temp = G
    n = 1

    while not temp.infinity:
        temp = pointAdd(temp, G, a, p)
        n += 1

    return n


# -------------------------------
# Display All Affine Points
# -------------------------------
def displayAllAffinePoints(a, b, p):
    print("\n=== All Affine Points on the Curve ===")
    count = 0

    for x in range(p):
        y_squared = mod(x * x * x + a * x + b, p)

        for y in range(p):
            if mod(y * y, p) == y_squared:
                print(f"({x}, {y})")
                count += 1

    print("Point at Infinity")
    print("Total Affine Points:", count + 1)


# -------------------------------
# MAIN
# -------------------------------
def main():
    a, b, p = map(int, input("Enter curve parameters (a b p): ").split())

    if (4 * a * a * a + 27 * b * b) % p == 0:
        print("Invalid curve!")
        return

    displayAllAffinePoints(a, b, p)

    # Input Generator
    while True:
        gx, gy = map(int, input("Enter Generator Point (Gx Gy): ").split())
        G = Point(gx, gy, False)

        if isOnCurve(G, a, b, p):
            break
        print("Point is NOT on curve. Try again.")

    n = computeOrder(G, a, p)
    print("Order of Generator (n) =", n)

    alpha = int(input("Enter Alice private key (1 <= alpha < n): "))
    beta = int(input("Enter Bob private key (1 <= beta < n): "))

    PA = scalarMultiply(G, alpha, a, p)
    PB = scalarMultiply(G, beta, a, p)

    print(f"\nAlice Public Key: ({PA.x},{PA.y})")
    print(f"Bob Public Key: ({PB.x},{PB.y})")

    sharedA = scalarMultiply(PB, alpha, a, p)
    sharedB = scalarMultiply(PA, beta, a, p)

    print(f"\nShared Secret (Alice): ({sharedA.x},{sharedA.y})")
    print(f"Shared Secret (Bob):   ({sharedB.x},{sharedB.y})")

    if sharedA.x == sharedB.x and sharedA.y == sharedB.y:
        print("\nKey Exchange Successful!")
    else:
        print("\nKey Exchange Failed!")


if __name__ == "__main__":
    main()
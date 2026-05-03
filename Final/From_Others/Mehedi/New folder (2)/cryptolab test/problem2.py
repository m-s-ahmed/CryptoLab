def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


while True:
    p, q, r = map(int, input("Enter p q r: ").split())

    if p == 0 and q == 0 and r == 0:
        break

    n = p * q
    phi = (p - 1) * (q - 1)

    print("enter e:")

    for i in range(r):
        e = int(input())

        if gcd(e, phi) == 1:
            print("YES")
        else:
            print("NO")
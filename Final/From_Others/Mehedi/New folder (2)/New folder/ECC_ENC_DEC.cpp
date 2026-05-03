#include <iostream>
#include <string>
using namespace std;

struct Point {
    long long x, y;
    bool infinity;
};

long long mod(long long a, long long p) {
    return (a % p + p) % p;
}

long long modInverse(long long a, long long p) {
    a = mod(a, p);
    for (long long i = 1; i < p; i++)
        if (mod(a * i, p) == 1)
            return i;
    return -1;
}

Point infinityPoint() {
    return {0, 0, true};
}

bool isOnCurve(Point P, long long a, long long b, long long p) {
    if (P.infinity) return true;
    return mod(P.y * P.y, p) ==
           mod(P.x * P.x * P.x + a * P.x + b, p);
}

Point pointAdd(Point P, Point Q, long long a, long long p) {

    if (P.infinity) return Q;
    if (Q.infinity) return P;

    if (P.x == Q.x && mod(P.y + Q.y, p) == 0)
        return infinityPoint();

    long long lambda;

    if (P.x == Q.x && P.y == Q.y) {
        long long num = mod(3 * P.x * P.x + a, p);
        long long den = modInverse(2 * P.y, p);
        lambda = mod(num * den, p);
    } else {
        long long num = mod(Q.y - P.y, p);
        long long den = modInverse(Q.x - P.x, p);
        lambda = mod(num * den, p);
    }

    long long xr = mod(lambda * lambda - P.x - Q.x, p);
    long long yr = mod(lambda * (P.x - xr) - P.y, p);

    return {xr, yr, false};
}

Point scalarMultiply(Point P, long long k, long long a, long long p) {
    Point result = infinityPoint();
    while (k > 0) {
        if (k & 1)
            result = pointAdd(result, P, a, p);
        P = pointAdd(P, P, a, p);
        k >>= 1;
    }
    return result;
}

/* -------- Compute Order of Generator -------- */
long long computeOrder(Point G, long long a, long long p) {
    Point temp = G;
    long long n = 1;

    while (!temp.infinity) {
        temp = pointAdd(temp, G, a, p);
        n++;
    }
    return n;
}

/* -------- Find all Affine Points on Curve -------- */
void displayAllAffinePoints(long long a, long long b, long long p) {
    cout << "\n=== All Affine Points on the Curve ===\n";
    int count = 0;
    
    for (long long x = 0; x < p; x++) {
        long long y_squared = mod(x * x * x + a * x + b, p);
        
        // Try to find y such that y^2 ≡ y_squared (mod p)
        for (long long y = 0; y < p; y++) {
            if (mod(y * y, p) == y_squared) {
                cout << "(" << x << ", " << y << ")\n";
                count++;
            }
        }
    }
    
    cout << "Point at Infinity\n";
    cout << "Total Affine Points: " << count + 1 << endl;
}

int main() {

    long long a, b, p;
    cout << "Enter curve parameters (a b p): ";
    cin >> a >> b >> p;

    if ((4*a*a*a + 27*b*b) % p == 0) {
        cout << "Invalid curve!\n";
        return 0;
    }

    // Display all affine points on the curve
    displayAllAffinePoints(a, b, p);

    Point G;

    // Keep asking until valid generator is entered
    while (true) {
        cout << "Enter Generator Point (Gx Gy): ";
        cin >> G.x >> G.y;
        G.infinity = false;

        if (isOnCurve(G, a, b, p)) break;
        cout << "Point is NOT on curve. Try again.\n";
    }

    long long n = computeOrder(G, a, p);
    cout << "Order of Generator (n) = " << n << endl;

    long long alpha, beta;

    cout << "Enter Alice private key (1 <= alpha < n): ";
    cin >> alpha;

    cout << "Enter Bob private key (1 <= beta < n): ";
    cin >> beta;

    Point PA = scalarMultiply(G, alpha, a, p);
    Point PB = scalarMultiply(G, beta, a, p);

    cout << "\nAlice Public Key: (" << PA.x << "," << PA.y << ")";
    cout << "\nBob Public Key: (" << PB.x << "," << PB.y << ")\n";

    Point sharedA = scalarMultiply(PB, alpha, a, p);
    Point sharedB = scalarMultiply(PA, beta, a, p);

    cout << "\nShared Secret (Alice): (" << sharedA.x << "," << sharedA.y << ")";
    cout << "\nShared Secret (Bob):   (" << sharedB.x << "," << sharedB.y << ")\n";

    if (sharedA.x == sharedB.x && sharedA.y == sharedB.y)
        cout << "\nKey Exchange Successful!\n";
    else {
        cout << "\nKey Exchange Failed!\n";
        return 0;
    }

    return 0;
}
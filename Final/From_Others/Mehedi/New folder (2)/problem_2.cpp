#include <iostream>
#include <string>
using namespace std;

struct Point {
    long long x, y;
    bool infinity;
};

/* -------- Math Utilities -------- */
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
    return mod(P.y * P.y, p) == mod(P.x * P.x * P.x + a * P.x + b, p);
}

/* -------- Point Operations -------- */
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

Point pointSubtract(Point P, Point Q, long long a, long long p) {
    if (Q.infinity) return P;
    Point negQ = {Q.x, mod(-Q.y, p), false};
    return pointAdd(P, negQ, a, p);
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

/* -------- Curve Analysis -------- */
long long computeOrder(Point G, long long a, long long p) {
    Point temp = G;
    long long n = 1;
    while (!temp.infinity) {
        temp = pointAdd(temp, G, a, p);
        n++;
    }
    return n;
}

void displayAllAffinePoints(long long a, long long b, long long p) {
    cout << "\n=== All Affine Points on the Curve ===\n";
    int count = 0;
    for (long long x = 0; x < p; x++) {
        long long y_squared = mod(x * x * x + a * x + b, p);
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

/* -------- Main Execution -------- */
int main() {
    long long a, b, p;
    cout << "Enter curve parameters (a b p): ";
    cin >> a >> b >> p;

    if (mod(4 * a * a * a + 27 * b * b, p) == 0) {
        cout << "Invalid curve (singular)!\n";
        return 0;
    }

    displayAllAffinePoints(a, b, p);

    Point G;
    while (true) {
        cout << "\nEnter Generator Point (Gx Gy): ";
        cin >> G.x >> G.y;
        G.infinity = false;
        if (isOnCurve(G, a, b, p)) break;
        cout << "Point is NOT on curve. Try again.\n";
    }

    long long n = computeOrder(G, a, p);
    cout << "Order of Generator (n) = " << n << endl;

    long long Sa, beta,k;
    
    
    Point Pb;
    Point Pm;
    cout << "\nEnter Plaintext point Pm : ";
        cin >> Pm.x >> Pm.y;
         Pm.infinity = false;
    // if (!isOnCurve(Pm, a, b, p)) {
    //     cout << "Error: Point is not on curve!\n";
    //     return 0;
    // }    
    cout<<"Enter a random integer(k):";
    cin>>k;
    cout << "\nEnter Alice private key (SA): "; cin >> Sa;
    cout << "\nEnter Bobs public key : ";
        cin >> Pb.x >> Pb.y;
         Pb.infinity = false;
    if (!isOnCurve(Pb, a, b, p)) {
        cout << "Error: Point is not on curve!\n";
        return 0;
    }    

    Point Pd= pointAdd(G, Pm, a, p);
 
    Point C1 = scalarMultiply(G, k, a, p); 
    Point secretComponent = scalarMultiply(Pb, k, a, p);
    Point C2 = pointAdd(Pb, secretComponent, a, p);
    cout<<"G+Pm:("<<Pd.x<<","<<Pd.y<<")\n";
    cout << "Pc: [(" << C1.x << "," << C1.y << "),(" << C2.x << "," << C2.y << ")]\n";

    return 0;
}
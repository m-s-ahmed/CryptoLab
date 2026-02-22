
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

// Fast modular exponentiation
long long modPower(long long a, long long d, long long n) {
    long long result = 1;
    a %= n;
    while (d > 0) {
        if (d & 1)
            result = (result * a) % n;
        d >>= 1;
        a = (a * a) % n;
    }
    return result;
}

// Miller–Rabin helper
bool millerTest(long long d, long long n) {
    long long a = 2 + rand() % (n - 4);
    long long x = modPower(a, d, n);

    if (x == 1 || x == n - 1)
        return true;

    while (d != n - 1) {
        x = (x * x) % n;
        d *= 2;

        if (x == 1) return false;
        if (x == n - 1) return true;
    }
    return false;
}

// Primality test
bool isPrime(long long n, int k = 5) {
    if (n <= 1 || n == 4) return false;
    if (n <= 3) return true;

    long long d = n - 1;
    while (d % 2 == 0)
        d /= 2;

    for (int i = 0; i < k; i++)
        if (!millerTest(d, n))
            return false;

    return true;
}

// GCD
long long gcd(long long a, long long b) {
    return (b == 0) ? a : gcd(b, a % b);
}

// Modular inverse
long long modInverse(long long e, long long phi) {
    for (long long d = 1; d < phi; d++)
        if ((e * d) % phi == 1)
            return d;
    return -1;
}

int main() {
    srand(time(0));

    long long p, q;
    cout << "Enter p: ";
    cin >> p;
    cout << "Enter q: ";
    cin >> q;

    if (!isPrime(p) || !isPrime(q)) {
        cout << "\nEither p or q is NOT prime.\n";
        return 0;
    }

    long long n = p * q;
    long long phi = (p - 1) * (q - 1);

    // Find all possible e
    vector<long long> possibleE;
    for (long long i = 2; i < phi; i++)
        if (gcd(i, phi) == 1)
            possibleE.push_back(i);

    cout << "\nPossible values of e:\n";
    for (long long x : possibleE)
        cout << x << " ";
    cout << endl;

    // User selects e
    long long e;
    cout << "\nSelect e from above list: ";
    cin >> e;

    long long d = modInverse(e, phi);

    cout << "\nPublic Key (e, n): (" << e << ", " << n << ")";
    cout << "\nPrivate Key (d, n): (" << d << ", " << n << ")\n";

    int choice;
    cout << "\n1. Numeric Message\n2. Text Message\nChoose: ";
    cin >> choice;

    if (choice == 1) {
        // Numeric message
        long long msg;
        cout << "Enter numeric message: ";
        cin >> msg;

        long long enc = modPower(msg, e, n);
        long long dec = modPower(enc, d, n);

        cout << "Encrypted: " << enc << endl;
        cout << "Decrypted: " << dec << endl;
    }
    else {
        // Text message
        string text;
        cout << "Enter text: ";
        cin.ignore();
        getline(cin, text);

        vector<long long> encryptedText;
        cout << "\nEncrypted text (numbers): ";
        for (char c : text) {
            long long enc = modPower((int)c, e, n);
            encryptedText.push_back(enc);
            cout << enc << " ";
        }

        cout << "\nDecrypted text: ";
        for (long long x : encryptedText) {
            char dec = (char)modPower(x, d, n);
            cout << dec;
        }
        cout << endl;
    }

    return 0;
}

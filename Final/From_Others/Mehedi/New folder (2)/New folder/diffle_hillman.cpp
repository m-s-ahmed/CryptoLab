#include <iostream>
#include <vector>
#include <set>
using namespace std;

// Modular exponentiation
long long modExp(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;

    while (exp > 0) {
        if (exp % 2)
            result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Find primitive roots
vector<long long> findPrimitiveRoots(long long q) {
    vector<long long> roots;

    for (long long g = 2; g < q; g++) {
        set<long long> s;

        for (long long i = 1; i < q; i++) {
            s.insert(modExp(g, i, q));
        }

        if (s.size() == q - 1)
            roots.push_back(g);
    }
    if (roots.empty())
        cout << "No primitive roots found for q = " << q << endl;
    return roots;
}

int main() {
    long long q;
    cout << "Enter prime number (q): ";
    cin >> q;

    // Show primitive roots
    vector<long long> roots = findPrimitiveRoots(q);
    if (roots.empty()) {
        return 1;
    }
    cout << "\nPrimitive roots:\n";
    for (auto r : roots) cout << r << " ";
    cout << endl;

    long long a;
    cout << "\nChoose primitive root (a): ";
    cin >> a;

    // User A
    long long XA;
    cout << "Enter private key of A: ";
    cin >> XA;
    long long YA = modExp(a, XA, q);

    // User B
    long long XB;
    cout << "Enter private key of B: ";
    cin >> XB;
    long long YB = modExp(a, XB, q);

    cout << "\nPublic key of A: " << YA;
    cout << "\nPublic key of B: " << YB;

    // Shared key
    long long KA = modExp(YB, XA, q);
    long long KB = modExp(YA, XB, q);

    cout << "\n\nShared key (A): " << KA;
    cout << "\nShared key (B): " << KB; 
    return 0;
}
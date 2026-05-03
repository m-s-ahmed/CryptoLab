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
    return roots;
}

int main() {
    int count;
    cout << "Enter number of prime values: ";
    cin >> count;
    cout << "Enter prime numbers (q): ";
    vector<long long> q(count);
    for (int i = 0; i < count; i++) {
        cin >> q[i];
    }

    for (int i = 0; i < count; i++) {
        vector<long long> roots = findPrimitiveRoots(q[i]);
        
        for (auto r : roots) cout << r << " ";
        cout << endl;
    }

    return 0;
}
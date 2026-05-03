
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
/*
long long modPower(long long a, long long d, long long n) {
    long long result = 1;
    while (d > 0) {
        if (d % 2 == 1) {
            result = (result * a) % n;
        }
       a = (a * a) % n;

        d = d / 2;
    }
    return result;
}

bool millerTest(long long d, long long n) {

    long long a = 2 + rand() % (n - 4);   
    long long x = modPower(a, d, n);     
    if (x == 1 || x == n - 1)
        return true;
    while (d != n - 1) {
        x = (x * x) % n;   
        d = d * 2;
        if (x == 1)
            return false;

        if (x == n - 1)
            return true;
    }
    return false;
}
bool isPrime(long long n) {
    if (n <= 1)
        return false;
    if (n == 2 || n == 3)
        return true;
    if (n % 2 == 0)
        return false;
    long long d = n - 1;

    while (d % 2 == 0)
        d = d / 2;

    int k = 5;   
    for (int i = 0; i < k; i++) {
        if (millerTest(d, n) == false)
            return false;
    }
    return true;
}
    */
long long gcd(long long a, long long b) {
    return (b == 0) ? a : gcd(b, a % b);
}
int main() {
while(true){
    long long p, q,r;
    cout << "Enter p q r: ";
    cin>>p >> q>>r;
    if(p==0&&q==0&&r==0){
        break;
    }
    /*
    if (!isPrime(p) || !isPrime(q)) {
        cout << "\nEither p or q is NOT prime.\n";
        return 0;
    }
        */
     long n = p * q;
     long phi = (p - 1) * (q - 1);
    int e;
    cout<<"enter e:"<<endl;
    for (int i=0;i<r;i++){
        cin>>e;
        if(gcd(e,phi)==1)
        cout<<"YES"<<endl;
        else cout<<"NO"<<endl;

    }

}
    return 0;
}

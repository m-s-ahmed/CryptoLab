#include <iostream>
#include <string>
using namespace std;

string caesarEncrypt(string text, int key);
string caesarDecrypt(string text, int key);
void bruteForceAttack(string text);

int main() {
    string text;         // original plain text
    string cipherText;   // encrypted text
    string decryptedText;
    int key;

    cout << "Enter plain text: ";
    getline(cin, text);

    cout << "Enter key: ";
    cin >> key;

    key = key % 26;

    // Encrypt
    cipherText = caesarEncrypt(text, key);
    cout << "\nEncrypted text: " << cipherText << endl;

    // Decrypt
    decryptedText = caesarDecrypt(cipherText, key);
    cout << "Decrypted text: " << decryptedText << endl;

    cout << "\nBrute Force Attack Results:\n";
    bruteForceAttack(cipherText);

    return 0;
}

// Encryption
string caesarEncrypt(string text, int key) {
    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        if (ch >= 'A' && ch <= 'Z')
            text[i] = (ch - 'A' + key) % 26 + 'A';
        else if (ch >= 'a' && ch <= 'z')
            text[i] = (ch - 'a' + key) % 26 + 'a';
    }
    return text;
}

// Decryption
string caesarDecrypt(string text, int key) {
    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        if (ch >= 'A' && ch <= 'Z')
            text[i] = (ch - 'A' - key) % 26 + 'A';
        else if (ch >= 'a' && ch <= 'z')
            text[i] = (ch - 'a' - key) % 26 + 'a';
    }
    return text;
}

// Pure brute-force attack
void bruteForceAttack(string text) {
    for (int key = 0; key < 26; key++) {
        string temp = text;

        for (int i = 0; i < temp.length(); i++) {
            char ch = temp[i];

            if (ch >= 'A' && ch <= 'Z')
                temp[i] = (ch - 'A' - key + 26) % 26 + 'A';
            else if (ch >= 'a' && ch <= 'z')
                temp[i] = (ch - 'a' - key + 26) % 26 + 'a';
        }

        cout << "Key " << key << ": " << temp << endl;
    }
}

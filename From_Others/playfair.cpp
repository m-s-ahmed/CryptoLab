#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

char matrix5x5[5][5];

// Function to remove duplicates from key
string removeDuplicates(string key) {
    string result = "";
    for (char c : key) {
        if (result.find(c) == string::npos) {
            result += c;
        }
    }
    return result;
}

// Function to generate Playfair matrix
void generateMatrix(string key) {
    string alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // J removed
    key = removeDuplicates(key);

    string finalKey = key;
    for (char c : alphabet) {
        if (finalKey.find(c) == string::npos) {
            finalKey += c;
        }
    }

    int k = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            matrix5x5[i][j] = finalKey[k++];
        }
    }
}

// Function to find position of character
void findPosition(char c, int &row, int &col) {
    if (c == 'J') c = 'I';

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (matrix5x5[i][j] == c) {
                row = i;
                col = j;
                return;
            }
        }
    }
}

// Prepare plaintext
string prepareText(string text) {
    string result = "";

    for (int i = 0; i < text.length(); i++) {
        if (text[i] != ' ') {
            char c = toupper(text[i]);
            if (c == 'J') c = 'I';
            result += c;
        }
    }

    for (int i = 0; i < result.length(); i += 2) {
        if (i + 1 == result.length()) {
            result += 'X';
        }
        else if (result[i] == result[i + 1]) {
            result.insert(i + 1, "X");
        }
    }

    return result;
}

// Encryption
string encrypt(string text) {
    string cipher = "";
    for (int i = 0; i < text.length(); i += 2) {
        int r1, c1, r2, c2;
        findPosition(text[i], r1, c1);
        findPosition(text[i + 1], r2, c2);

        if (r1 == r2) {
            cipher += matrix5x5[r1][(c1 + 1) % 5];
            cipher += matrix5x5[r2][(c2 + 1) % 5];
        }
        else if (c1 == c2) {
            cipher += matrix5x5[(r1 + 1) % 5][c1];
            cipher += matrix5x5[(r2 + 1) % 5][c2];
        }
        else {
            cipher += matrix5x5[r1][c2];
            cipher += matrix5x5[r2][c1];
        }
    }
    return cipher;
}

// Decryption
string decrypt(string text) {
    string plain = "";
    for (int i = 0; i < text.length(); i += 2) {
        int r1, c1, r2, c2;
        findPosition(text[i], r1, c1);
        findPosition(text[i + 1], r2, c2);

        if (r1 == r2) {
            plain += matrix5x5[r1][(c1 + 4) % 5];
            plain += matrix5x5[r2][(c2 + 4) % 5];
        }
        else if (c1 == c2) {
            plain += matrix5x5[(r1 + 4) % 5][c1];
            plain += matrix5x5[(r2 + 4) % 5][c2];
        }
        else {
            plain += matrix5x5[r1][c2];
            plain += matrix5x5[r2][c1];
        }
    }
    return plain;
}

// Main function
int main() {
    string key, plaintext;

    cout << "Enter Key: ";
    cin >> key;

    transform(key.begin(), key.end(), key.begin(), ::toupper);

    generateMatrix(key);

    cout << "\nGenerated 5x5 Matrix:\n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cout << matrix5x5[i][j] << " ";
        }
        cout << endl;
    }

    cout << "\nEnter Plaintext: ";
    cin.ignore();
    getline(cin, plaintext);

    string prepared = prepareText(plaintext);

    string cipher = encrypt(prepared);
    cout << "\nCiphertext: " << cipher << endl;

    string decrypted = decrypt(cipher);
    cout << "Decrypted Text: " << decrypted << endl;

    return 0;
}

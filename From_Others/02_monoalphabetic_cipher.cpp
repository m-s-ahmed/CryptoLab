#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

// Standard English letter frequency order (most to least frequent)
const string ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ";

// Function to encrypt
string encrypt(string text, string key) {
    string cipherText = "";
    for (char c : text) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            int index = toupper(c) - 'A';
            char encryptedChar = key[index];
            cipherText += isupper(c) ? toupper(encryptedChar) : tolower(encryptedChar);
        } else {
            cipherText += c;
        }
    }
    return cipherText;
}

// Function to decrypt
string decrypt(string cipherText, string key) {
    string plainText = "";
    for (char c : cipherText) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            int index = key.find(toupper(c));
            char decryptedChar = 'A' + index;
            plainText += isupper(c) ? toupper(decryptedChar) : tolower(decryptedChar);
        } else {
            plainText += c;
        }
    }
    return plainText;
}

// Helper struct for sorting frequencies
struct CharFreq {
    char c;
    int count;
};

// Sort comparator for frequencies
bool compareFreq(CharFreq a, CharFreq b) {
    return a.count > b.count;
}

// Relative Frequency Analysis & naive breaking
void frequencyAnalysisAttack(string cipherText) {
    cout << "\n--- Frequency Analysis Attack ---" << endl;
    
    map<char, int> freqMap;
    int totalLetters = 0;
    
    for (char c : cipherText) {
        if (isalpha(c)) {
            freqMap[toupper(c)]++;
            totalLetters++;
        }
    }

    vector<CharFreq> frequencies;
    for (char c = 'A'; c <= 'Z'; c++) {
        frequencies.push_back({c, freqMap[c]});
    }

    sort(frequencies.begin(), frequencies.end(), compareFreq);

    cout << "Ciphertext Letter Frequencies:" << endl;
    for (int i = 0; i < frequencies.size(); i++) {
        if (frequencies[i].count > 0) {
            cout << frequencies[i].c << ": " << frequencies[i].count 
                 << " (" << (float)frequencies[i].count/totalLetters * 100 << "%)" << endl;
        }
    }

    // Attempt naive substitution based strictly on frequency match
    string guessedKey(26, ' ');
    for (int i = 0; i < frequencies.size() && i < ENGLISH_FREQ.length(); i++) {
        // Map the i-th most frequent cipher letter to the i-th most frequent English letter
        int originalCharIndex = ENGLISH_FREQ[i] - 'A';
        guessedKey[originalCharIndex] = frequencies[i].c; 
    }

    cout << "\nNaive Guess based on pure frequency match:" << endl;
    string crackedText = decrypt(cipherText, guessedKey);
    cout << "Guessed Key: " << guessedKey << endl;
    cout << "Partial/Guessed Decryption: " << crackedText << endl;
    cout << "(Note: Short texts will not crack perfectly with pure frequency analysis due to statistical anomalies.)" << endl;
}

int main() {
    // A standard a-z mapped to a shuffled key
    string key = "QWERTYUIOPASDFGHJKLZXCVBNM"; 
    // A longer text is better for frequency analysis
    string text = "DEFEND THE EAST WALL OF THE CASTLE AT DAWN. THE ENEMY IS APPROACHING FAST AND WE MUST HOLD THE LINE TO ENSURE OUR VICTORY.";
    
    cout << "Original Text: " << text << endl;
    cout << "Encryption Key: " << key << endl;

    string cipherText = encrypt(text, key);
    cout << "Encrypted Text: " << cipherText << endl;

    string decryptedText = decrypt(cipherText, key);
    cout << "Decrypted Text: " << decryptedText << endl;

    frequencyAnalysisAttack(cipherText);

    return 0;
}
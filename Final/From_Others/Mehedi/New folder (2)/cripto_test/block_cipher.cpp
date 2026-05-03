#include <iostream>
#include <vector>
#include <string>
using namespace std;

int BLOCK_SIZE;

vector<int> cipherFunc(vector<int> block, vector<int> key) {
    vector<int> result(BLOCK_SIZE);
    for (int i = 0; i < BLOCK_SIZE; i++)
        result[i] = block[i] ^ key[i];
    return result;
}
void pad(vector<int> &data) {
    while (data.size() % BLOCK_SIZE != 0)
        data.push_back(0);
}
vector<int> stringToAscii(const string &text) {
    vector<int> data;
    for (char ch : text)
        data.push_back(static_cast<unsigned char>(ch));
    return data;
}

string asciiToString(const vector<int> &data) {
    string text;
    for (int value : data) {
        if (value == 0) break;
        text.push_back(static_cast<char>(value));
    }
    return text;
}
vector<vector<int>> makeBlocks(vector<int> data) {
    vector<vector<int>> blocks;
    for (int i = 0; i < data.size(); i += BLOCK_SIZE) {
        vector<int> block;
        for (int j = 0; j < BLOCK_SIZE; j++)
            block.push_back(data[i + j]);
        blocks.push_back(block);
    }
    return blocks;
}
void printBlocks(vector<vector<int>> blocks) {
    for (auto b : blocks) {
        for (int x : b) cout << char(x) ;
        cout << endl;
    }
}
vector<vector<int>> CBC_enc(vector<vector<int>> pt, vector<int> key, vector<int> iv) {
    vector<vector<int>> ct;
    vector<int>prev=iv;

    for (auto b : pt) {
        vector<int> temp=cipherFunc(b, prev);
        vector<int> c = cipherFunc(temp, key);
        ct.push_back(c);
        prev = c;
    }
    return ct;
}

vector<vector<int>> CBC_dec(vector<vector<int>> ct, vector<int> key, vector<int> iv) {
    vector<vector<int>> pt;
    vector<int> prev = iv;

    for (auto c : ct) {
        vector<int> temp = cipherFunc(c, key);
        vector<int> p=cipherFunc(temp, prev);
        pt.push_back(p);
        prev = c;
    }
    return pt;
}
int main() {
    

    cin.ignore();
    string plaintext;
    string iv;
    string key;
    cout <<"Enter plaintext: ";
    getline(cin,plaintext);
    cout<<"Enter IV: ";
    getline(cin,iv);
    cout<<"Enter key: ";
    getline(cin,key);



    vector<int>data = stringToAscii(plaintext);

    pad(data);
    vector<vector<int>> blocks = makeBlocks(data);
    vector<int>iv = stringToAscii(iv);
    vector<int>key = stringToAscii(key);

    

    auto cbc = CBC_enc(blocks, key, iv);

    cout << "CBC:\n"; printBlocks(cbc);

    
    cout << "CBC Decryption:\n"; printBlocks(CBC_dec(cbc, key, iv));
    

    vector<vector<int>> decryptedBlocks =CBC_dec(cbc,key,iv);
    vector<int> recoveredData;
    for (auto block : decryptedBlocks)
        for (int value : block)
            recoveredData.push_back(value);

    cout << "\nRecovered plaintext: " << asciiToString(recoveredData) << endl;

    return 0;
}
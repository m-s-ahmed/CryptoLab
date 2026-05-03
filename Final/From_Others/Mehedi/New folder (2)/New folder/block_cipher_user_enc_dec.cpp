#include <iostream>
#include <vector>
using namespace std;

int BLOCK_SIZE;

// XOR cipher (same for encrypt/decrypt)
vector<int> cipherFunc(vector<int> block, vector<int> key) {
    vector<int> result(BLOCK_SIZE);
    for (int i = 0; i < BLOCK_SIZE; i++)
        result[i] = block[i] ^ key[i];
    return result;
}

// Padding
void pad(vector<int> &data) {
    while (data.size() % BLOCK_SIZE != 0)
        data.push_back(0);
}

// Make blocks
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

// Print blocks
void printBlocks(vector<vector<int>> blocks) {
    for (auto b : blocks) {
        for (int x : b) cout << x << " ";
        cout << endl;
    }
}

// ================= ECB =================
vector<vector<int>> ECB_enc(vector<vector<int>> pt, vector<int> key) {
    vector<vector<int>> ct;
    for (auto b : pt) ct.push_back(cipherFunc(b, key));
    return ct;
}

vector<vector<int>> ECB_dec(vector<vector<int>> ct, vector<int> key) {
    vector<vector<int>> pt;
    for (auto b : ct) pt.push_back(cipherFunc(b, key));
    return pt;
}

// ================= CBC =================
vector<vector<int>> CBC_enc(vector<vector<int>> pt, vector<int> key, vector<int> iv) {
    vector<vector<int>> ct;
    vector<int> prev = iv;

    for (auto b : pt) {
        vector<int> temp(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            temp[i] = b[i] ^ prev[i];

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

        vector<int> p(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            p[i] = temp[i] ^ prev[i];

        pt.push_back(p);
        prev = c;
    }
    return pt;
}

// ================= CFB =================
vector<vector<int>> CFB_enc(vector<vector<int>> pt, vector<int> key, vector<int> iv) {
    vector<vector<int>> ct;
    vector<int> prev = iv;

    for (auto b : pt) {
        vector<int> enc = cipherFunc(prev, key);

        vector<int> c(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            c[i] = b[i] ^ enc[i];

        ct.push_back(c);
        prev = c;
    }
    return ct;
}

vector<vector<int>> CFB_dec(vector<vector<int>> ct, vector<int> key, vector<int> iv) {
    vector<vector<int>> pt;
    vector<int> prev = iv;

    for (auto c : ct) {
        vector<int> enc = cipherFunc(prev, key);

        vector<int> p(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            p[i] = c[i] ^ enc[i];

        pt.push_back(p);
        prev = c;
    }
    return pt;
}

// ================= OFB =================
vector<vector<int>> OFB_enc(vector<vector<int>> pt, vector<int> key, vector<int> iv) {
    vector<vector<int>> ct;
    vector<int> prev = iv;

    for (auto b : pt) {
        prev = cipherFunc(prev, key);

        vector<int> c(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            c[i] = b[i] ^ prev[i];

        ct.push_back(c);
    }
    return ct;
}

vector<vector<int>> OFB_dec(vector<vector<int>> ct, vector<int> key, vector<int> iv) {
    // same as encryption
    return OFB_enc(ct, key, iv);
}

// ================= CTR =================
vector<vector<int>> CTR_enc(vector<vector<int>> pt, vector<int> key) {
    vector<vector<int>> ct;
    int counter = 1;

    for (auto b : pt) {
        vector<int> ctr(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            ctr[i] = counter + i;

        vector<int> enc = cipherFunc(ctr, key);

        vector<int> c(BLOCK_SIZE);
        for (int i = 0; i < BLOCK_SIZE; i++)
            c[i] = b[i] ^ enc[i];

        ct.push_back(c);
        counter++;
    }
    return ct;
}

vector<vector<int>> CTR_dec(vector<vector<int>> ct, vector<int> key) {
    // same as encryption
    return CTR_enc(ct, key);
}

// ================= MAIN =================
int main() {
    cout << "Enter block size: ";
    cin >> BLOCK_SIZE;

    int n;
    cout << "Enter plaintext size: ";
    cin >> n;

    vector<int> data(n);
    cout << "Enter plaintext:\n";
    for (int i = 0; i < n; i++) cin >> data[i];

    pad(data);
    vector<vector<int>> blocks = makeBlocks(data);

    // Key input
    vector<int> key(BLOCK_SIZE);
    cout << "Enter key (" << BLOCK_SIZE << " values):\n";
    for (int i = 0; i < BLOCK_SIZE; i++) cin >> key[i];

    // IV input
    vector<int> iv(BLOCK_SIZE);
    cout << "Enter IV (" << BLOCK_SIZE << " values):\n";
    for (int i = 0; i < BLOCK_SIZE; i++) cin >> iv[i];

    // Encrypt
    auto ecb = ECB_enc(blocks, key);
    auto cbc = CBC_enc(blocks, key, iv);
    auto cfb = CFB_enc(blocks, key, iv);
    auto ofb = OFB_enc(blocks, key, iv);
    auto ctr = CTR_enc(blocks, key);

    cout << "\n=== Encryption ===\n";
    cout << "ECB:\n"; printBlocks(ecb);
    cout << "CBC:\n"; printBlocks(cbc);
    cout << "CFB:\n"; printBlocks(cfb);
    cout << "OFB:\n"; printBlocks(ofb);
    cout << "CTR:\n"; printBlocks(ctr);

    // Decrypt
    cout << "\n=== Decryption ===\n";
    cout << "ECB:\n"; printBlocks(ECB_dec(ecb, key));
    cout << "CBC:\n"; printBlocks(CBC_dec(cbc, key, iv));
    cout << "CFB:\n"; printBlocks(CFB_dec(cfb, key, iv));
    cout << "OFB:\n"; printBlocks(OFB_dec(ofb, key, iv));
    cout << "CTR:\n"; printBlocks(CTR_dec(ctr, key));

    return 0;
}
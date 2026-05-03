# Global block size
BLOCK_SIZE = 0


# -------------------------------
# XOR cipher (same for enc/dec)
# -------------------------------
def cipherFunc(block, key):
    return [block[i] ^ key[i] for i in range(BLOCK_SIZE)]


# -------------------------------
# Padding
# -------------------------------
def pad(data):
    while len(data) % BLOCK_SIZE != 0:
        data.append(0)


# -------------------------------
# Make blocks
# -------------------------------
def makeBlocks(data):
    blocks = []
    for i in range(0, len(data), BLOCK_SIZE):
        blocks.append(data[i:i + BLOCK_SIZE])
    return blocks


# -------------------------------
# Print blocks
# -------------------------------
def printBlocks(blocks):
    for b in blocks:
        print(*b)


# ================= ECB =================
def ECB_enc(pt, key):
    return [cipherFunc(b, key) for b in pt]


def ECB_dec(ct, key):
    return [cipherFunc(b, key) for b in ct]


# ================= CBC =================
def CBC_enc(pt, key, iv):
    ct = []
    prev = iv[:]

    for b in pt:
        temp = [b[i] ^ prev[i] for i in range(BLOCK_SIZE)]
        c = cipherFunc(temp, key)
        ct.append(c)
        prev = c
    return ct


def CBC_dec(ct, key, iv):
    pt = []
    prev = iv[:]

    for c in ct:
        temp = cipherFunc(c, key)
        p = [temp[i] ^ prev[i] for i in range(BLOCK_SIZE)]
        pt.append(p)
        prev = c
    return pt


# ================= CFB =================
def CFB_enc(pt, key, iv):
    ct = []
    prev = iv[:]

    for b in pt:
        enc = cipherFunc(prev, key)
        c = [b[i] ^ enc[i] for i in range(BLOCK_SIZE)]
        ct.append(c)
        prev = c
    return ct


def CFB_dec(ct, key, iv):
    pt = []
    prev = iv[:]

    for c in ct:
        enc = cipherFunc(prev, key)
        p = [c[i] ^ enc[i] for i in range(BLOCK_SIZE)]
        pt.append(p)
        prev = c
    return pt


# ================= OFB =================
def OFB_enc(pt, key, iv):
    ct = []
    prev = iv[:]

    for b in pt:
        prev = cipherFunc(prev, key)
        c = [b[i] ^ prev[i] for i in range(BLOCK_SIZE)]
        ct.append(c)
    return ct


def OFB_dec(ct, key, iv):
    return OFB_enc(ct, key, iv)


# ================= CTR =================
def CTR_enc(pt, key):
    ct = []
    counter = 1

    for b in pt:
        ctr = [counter + i for i in range(BLOCK_SIZE)]
        enc = cipherFunc(ctr, key)
        c = [b[i] ^ enc[i] for i in range(BLOCK_SIZE)]
        ct.append(c)
        counter += 1
    return ct


def CTR_dec(ct, key):
    return CTR_enc(ct, key)


# ================= MAIN =================
def main():
    global BLOCK_SIZE

    BLOCK_SIZE = int(input("Enter block size: "))

    n = int(input("Enter plaintext size: "))
    data = list(map(int, input("Enter plaintext:\n").split()))

    pad(data)
    blocks = makeBlocks(data)

    key = list(map(int, input(f"Enter key ({BLOCK_SIZE} values):\n").split()))
    iv = list(map(int, input(f"Enter IV ({BLOCK_SIZE} values):\n").split()))

    # Encrypt
    ecb = ECB_enc(blocks, key)
    cbc = CBC_enc(blocks, key, iv)
    cfb = CFB_enc(blocks, key, iv)
    ofb = OFB_enc(blocks, key, iv)
    ctr = CTR_enc(blocks, key)

    print("\n=== Encryption ===")
    print("ECB:")
    printBlocks(ecb)

    print("CBC:")
    printBlocks(cbc)

    print("CFB:")
    printBlocks(cfb)

    print("OFB:")
    printBlocks(ofb)

    print("CTR:")
    printBlocks(ctr)

    # Decrypt
    print("\n=== Decryption ===")
    print("ECB:")
    printBlocks(ECB_dec(ecb, key))

    print("CBC:")
    printBlocks(CBC_dec(cbc, key, iv))

    print("CFB:")
    printBlocks(CFB_dec(cfb, key, iv))

    print("OFB:")
    printBlocks(OFB_dec(ofb, key, iv))

    print("CTR:")
    printBlocks(CTR_dec(ctr, key))


if __name__ == "__main__":
    main()
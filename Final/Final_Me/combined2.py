BLOCK_SIZE = 8

# ---------- XOR Function ----------
def xor_text(a, b):
    result = ""
    for i in range(len(a)):
        result += chr(ord(a[i]) ^ ord(b[i]))
    return result


# ---------- Padding with X ----------
def pad_text(text):
    while len(text) % BLOCK_SIZE != 0:
        text += "X"
    return text


# ---------- Remove Padding X ----------
def remove_padding(text):
    return text.rstrip("X")


# ---------- Split into Blocks ----------
def split_blocks(text):
    blocks = []
    for i in range(0, len(text), BLOCK_SIZE):
        blocks.append(text[i:i + BLOCK_SIZE])
    return blocks


# ---------- Block Encrypt/Decrypt using XOR ----------
def encrypt_block(block, key):
    return xor_text(block, key)


def decrypt_block(block, key):
    return xor_text(block, key)


# ================= ECB MODE =================
def encrypt_ecb(plaintext, key):
    plaintext = pad_text(plaintext)
    blocks = split_blocks(plaintext)

    cipher_blocks = []

    print("\n--- ECB Encryption Process ---")

    for i, block in enumerate(blocks, start=1):
        cipher = encrypt_block(block, key)
        cipher_blocks.append(cipher)

        print(f"P{i} =", block)
        print(f"C{i} =", cipher)
        print()

    return cipher_blocks


def decrypt_ecb(cipher_blocks, key):
    plain_blocks = []

    print("\n--- ECB Decryption Process ---")

    for i, cipher in enumerate(cipher_blocks, start=1):
        plain = decrypt_block(cipher, key)
        plain_blocks.append(plain)

        print(f"C{i} =", cipher)
        print(f"P{i} =", plain)
        print()

    return remove_padding("".join(plain_blocks))


# ================= CBC MODE =================
def encrypt_cbc(plaintext, iv, key):
    plaintext = pad_text(plaintext)
    blocks = split_blocks(plaintext)

    cipher_blocks = []
    previous = iv

    print("\n--- CBC Encryption Process ---")

    for i, block in enumerate(blocks, start=1):
        xored = xor_text(block, previous)
        cipher = encrypt_block(xored, key)

        cipher_blocks.append(cipher)
        previous = cipher

        print(f"P{i} =", block)
        print(f"C{i} =", cipher)
        print()

    return cipher_blocks


def decrypt_cbc(cipher_blocks, iv, key):
    plain_blocks = []
    previous = iv

    print("\n--- CBC Decryption Process ---")

    for i, cipher in enumerate(cipher_blocks, start=1):
        decrypted = decrypt_block(cipher, key)
        plain = xor_text(decrypted, previous)

        plain_blocks.append(plain)
        previous = cipher

        print(f"C{i} =", cipher)
        print(f"P{i} =", plain)
        print()

    return remove_padding("".join(plain_blocks))


# ================= CFB MODE =================
def encrypt_cfb(plaintext, iv, key):
    plaintext = pad_text(plaintext)
    blocks = split_blocks(plaintext)

    cipher_blocks = []
    previous = iv

    print("\n--- CFB Encryption Process ---")

    for i, block in enumerate(blocks, start=1):
        encrypted_previous = encrypt_block(previous, key)
        cipher = xor_text(block, encrypted_previous)

        cipher_blocks.append(cipher)
        previous = cipher

        print(f"P{i} =", block)
        print(f"C{i} =", cipher)
        print()

    return cipher_blocks


def decrypt_cfb(cipher_blocks, iv, key):
    plain_blocks = []
    previous = iv

    print("\n--- CFB Decryption Process ---")

    for i, cipher in enumerate(cipher_blocks, start=1):
        encrypted_previous = encrypt_block(previous, key)
        plain = xor_text(cipher, encrypted_previous)

        plain_blocks.append(plain)
        previous = cipher

        print(f"C{i} =", cipher)
        print(f"P{i} =", plain)
        print()

    return remove_padding("".join(plain_blocks))


# ================= OFB MODE =================
def encrypt_ofb(plaintext, iv, key):
    plaintext = pad_text(plaintext)
    blocks = split_blocks(plaintext)

    cipher_blocks = []
    output = iv

    print("\n--- OFB Encryption Process ---")

    for i, block in enumerate(blocks, start=1):
        output = encrypt_block(output, key)
        cipher = xor_text(block, output)

        cipher_blocks.append(cipher)

        print(f"P{i} =", block)
        print(f"C{i} =", cipher)
        print()

    return cipher_blocks


def decrypt_ofb(cipher_blocks, iv, key):
    plain_blocks = []
    output = iv

    print("\n--- OFB Decryption Process ---")

    for i, cipher in enumerate(cipher_blocks, start=1):
        output = encrypt_block(output, key)
        plain = xor_text(cipher, output)

        plain_blocks.append(plain)

        print(f"C{i} =", cipher)
        print(f"P{i} =", plain)
        print()

    return remove_padding("".join(plain_blocks))


# ================= CTR MODE =================
def make_counter_block(iv, count):
    count_text = str(count).zfill(BLOCK_SIZE)
    return xor_text(iv, count_text)


def encrypt_ctr(plaintext, iv, key):
    plaintext = pad_text(plaintext)
    blocks = split_blocks(plaintext)

    cipher_blocks = []

    print("\n--- CTR Encryption Process ---")

    for i, block in enumerate(blocks, start=1):
        counter_block = make_counter_block(iv, i)
        encrypted_counter = encrypt_block(counter_block, key)
        cipher = xor_text(block, encrypted_counter)

        cipher_blocks.append(cipher)

        print(f"P{i} =", block)
        print(f"C{i} =", cipher)
        print()

    return cipher_blocks


def decrypt_ctr(cipher_blocks, iv, key):
    plain_blocks = []

    print("\n--- CTR Decryption Process ---")

    for i, cipher in enumerate(cipher_blocks, start=1):
        counter_block = make_counter_block(iv, i)
        encrypted_counter = encrypt_block(counter_block, key)
        plain = xor_text(cipher, encrypted_counter)

        plain_blocks.append(plain)

        print(f"C{i} =", cipher)
        print(f"P{i} =", plain)
        print()

    return remove_padding("".join(plain_blocks))


# ---------- MAIN PROGRAM ----------
text = input("Enter Plaintext / Ciphertext: ")
iv = input("Enter IV (8 characters): ")
key = input("Enter Key (8 characters): ")

if len(iv) != BLOCK_SIZE or len(key) != BLOCK_SIZE:
    print("IV and Key must be exactly 8 characters.")
else:
    print("\nChoose Mode:")
    print("1. ECB")
    print("2. CBC")
    print("3. CFB")
    print("4. OFB")
    print("5. CTR")

    mode = input("Enter mode (1-5): ")

    choice = input("EN for Encrypt / DE for Decrypt: ").upper()

    if mode == "1":
        if choice == "EN":
            cipher_blocks = encrypt_ecb(text, key)
            print("Final Cipher Blocks:")
            for i, c in enumerate(cipher_blocks, start=1):
                print(f'C{i} = "{c}"')
        elif choice == "DE":
            cipher_blocks = split_blocks(text)
            plain = decrypt_ecb(cipher_blocks, key)
            print("Final Plaintext:", plain)

    elif mode == "2":
        if choice == "EN":
            cipher_blocks = encrypt_cbc(text, iv, key)
            print("Final Cipher Blocks:")
            for i, c in enumerate(cipher_blocks, start=1):
                print(f'C{i} = "{c}"')
        elif choice == "DE":
            cipher_blocks = split_blocks(text)
            plain = decrypt_cbc(cipher_blocks, iv, key)
            print("Final Plaintext:", plain)

    elif mode == "3":
        if choice == "EN":
            cipher_blocks = encrypt_cfb(text, iv, key)
            print("Final Cipher Blocks:")
            for i, c in enumerate(cipher_blocks, start=1):
                print(f'C{i} = "{c}"')
        elif choice == "DE":
            cipher_blocks = split_blocks(text)
            plain = decrypt_cfb(cipher_blocks, iv, key)
            print("Final Plaintext:", plain)

    elif mode == "4":
        if choice == "EN":
            cipher_blocks = encrypt_ofb(text, iv, key)
            print("Final Cipher Blocks:")
            for i, c in enumerate(cipher_blocks, start=1):
                print(f'C{i} = "{c}"')
        elif choice == "DE":
            cipher_blocks = split_blocks(text)
            plain = decrypt_ofb(cipher_blocks, iv, key)
            print("Final Plaintext:", plain)

    elif mode == "5":
        if choice == "EN":
            cipher_blocks = encrypt_ctr(text, iv, key)
            print("Final Cipher Blocks:")
            for i, c in enumerate(cipher_blocks, start=1):
                print(f'C{i} = "{c}"')
        elif choice == "DE":
            cipher_blocks = split_blocks(text)
            plain = decrypt_ctr(cipher_blocks, iv, key)
            print("Final Plaintext:", plain)

    else:
        print("Invalid mode.")
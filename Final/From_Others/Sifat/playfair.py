
def prepare_text(text):
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if i + 1 < len(text) and text[i] == text[i + 1]:
            result += 'x'
        i += 1

    if len(result) % 2 != 0:
        result += 'z'

    return result

def generate_key_table(key):
    key = key.replace('j', 'i')
    used = set()
    table = []

    for ch in key:
        if ch not in used and ch.isalpha():
            used.add(ch)
            table.append(ch)

    for ch in range(ord('a'), ord('z') + 1):
        c = chr(ch)
        if c == 'j':
            continue
        if c not in used:
            used.add(c)
            table.append(c)

    return [table[i:i + 5] for i in range(0, 25, 5)]

def display_matrix(matrix):
    print("\nPlayfair Key Matrix:")
    for row in matrix:
        print(" ".join(row))

def find_position(matrix, a, b):
    if a == 'j': a = 'i'
    if b == 'j': b = 'i'

    pos = [0, 0, 0, 0]

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == a:
                pos[0], pos[1] = i, j
            if matrix[i][j] == b:
                pos[2], pos[3] = i, j
    return pos

def encrypt(text, matrix):
    cipher = ""

    for i in range(0, len(text), 2):
        r1, c1, r2, c2 = find_position(matrix, text[i], text[i + 1])

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:  # Same column
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:  # Rectangle rule
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

def decrypt(cipher, matrix):
    plain = ""

    for i in range(0, len(cipher), 2):
        r1, c1, r2, c2 = find_position(matrix, cipher[i], cipher[i + 1])

        if r1 == r2:  # Same row
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:  # Same column
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]

        else:  # Rectangle rule
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain 

def playfair_cipher(text, key):
    key = key.lower().replace(" ", "")
    text = text.lower().replace(" ","")

    matrix = generate_key_table(key)
    display_matrix(matrix)

    prepared_text = prepare_text(text)
    cipher = encrypt(prepared_text, matrix)
    decrypted = decrypt(cipher, matrix) 

    print("\nPlaintext        :", text)
    print("Encrypted Text     :", cipher)
    if decrypted[-1] == 'z' and text[-1] != 'z':
        decrypted = decrypted[:-1]
    print("Decrypted Text     :", decrypted)

key = input("Enter the key: ")
text = input("Enter the text to encrypt: ")

playfair_cipher(text, key)

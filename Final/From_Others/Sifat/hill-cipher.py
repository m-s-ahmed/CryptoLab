import math

def mod_inverse(a, m):
    """Find modular inverse of a under modulo m"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def text_to_numbers(text):
    return [ord(c) - ord('a') for c in text]

def numbers_to_text(nums):
    return ''.join(chr(n + ord('a')) for n in nums)

def get_matrix_minor(matrix, i, j):
    """Return minor of matrix excluding row i and column j"""
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinant(matrix):
    """Recursive determinant calculation"""
    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant(
            get_matrix_minor(matrix, 0, c)
        )
    return det

def matrix_mod_inverse(matrix, mod):
    """Find modular inverse of matrix"""
    det = determinant(matrix) % mod
    det_inv = mod_inverse(det, mod)

    if det_inv is None:
        raise ValueError("Key matrix is not invertible modulo 26")

    size = len(matrix)

    # Cofactor matrix
    cofactors = []
    for r in range(size):
        cofactor_row = []
        for c in range(size):
            minor = get_matrix_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * determinant(minor))
        cofactors.append(cofactor_row)

    # Adjugate (transpose of cofactor matrix)
    adjugate = list(map(list, zip(*cofactors)))

    # Multiply adjugate with determinant inverse
    inv_matrix = []
    for row in adjugate:
        inv_matrix.append([(det_inv * elem) % mod for elem in row])

    return inv_matrix

def matrix_multiply(A, B, mod):
    """Multiply matrix A with vector B"""
    result = []
    for row in A:
        val = sum(row[i] * B[i] for i in range(len(B))) % mod
        result.append(val)
    return result
 
def hill_encrypt(plaintext, key_matrix):
    m = len(key_matrix)

    plaintext = plaintext.lower().replace(" ", "")

    # Padding with 'x'
    while len(plaintext) % m != 0:
        plaintext += 'x'

    nums = text_to_numbers(plaintext)
    cipher_nums = []

    for i in range(0, len(nums), m):
        block = nums[i:i+m]
        cipher_nums.extend(matrix_multiply(key_matrix, block, 26))

    return numbers_to_text(cipher_nums)

# ---------- Decryption ----------

def hill_decrypt(ciphertext, key_matrix):
    inv_key = matrix_mod_inverse(key_matrix, 26)

    nums = text_to_numbers(ciphertext)
    plain_nums = []

    for i in range(0, len(nums), len(inv_key)):
        block = nums[i:i+len(inv_key)]
        plain_nums.extend(matrix_multiply(inv_key, block, 26))

    return numbers_to_text(plain_nums)

# ---------- User Input ----------

M = int(input("Enter order of key matrix (M): "))

print("Enter key matrix characters row-wise (space separated):")
key_matrix = []

for i in range(M):
    row_chars = input().lower().split()   # take characters
    row_nums = text_to_numbers(row_chars) # convert to numbers
    key_matrix.append(row_nums)

print("\nKey Matrix:")
for row in key_matrix:
    print(row)

# ---------- Key Validity Check ----------

det = determinant(key_matrix) % 26
if math.gcd(det, 26) != 1:
    print("Invalid key matrix!")
    print("Determinant mod 26 =", det)
    exit()

plaintext = input("Enter plaintext: ")

# ---------- Output ----------

cipher = hill_encrypt(plaintext, key_matrix)
decrypted = hill_decrypt(cipher, key_matrix)

print("\nEncrypted Text:", cipher)
print("Decrypted Text:", decrypted)

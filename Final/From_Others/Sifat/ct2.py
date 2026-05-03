block_size = 8

def manual_pad(text):
    pad_len = block_size - (len(text) % block_size)
    return text +  bytes([ord('X')] * pad_len)

def xored(a, b):
    return bytes(i ^ j for i, j in zip(a, b))

def block_encrypt(plaintext, iv, key):

    paded_text = manual_pad(plaintext)
    ciphertext = b''
    prev = iv
    j = 1

    for i in range(0, len(plaintext), block_size):
        
        block = paded_text[i: i+block_size]
        xored_data = xored(block, prev)
        cipher = xored(key, xored_data)
        ciphertext += cipher        
        prev = cipher

        print("c",j," = ",cipher)
        j += 1

    return ciphertext

def block_decrypt(cipher, iv, key):
     plaintext = b''
     prev = iv
     
     for i in range(0, len(cipher), block_size):
        block = cipher[i: i+block_size]

        xored_data = xored(key, block)
        text = xored(xored_data, prev)
        print(text)
        plaintext += text
        prev = block

     return plaintext

plaintext = input("Plaintext = ").encode()
iv = input("IV = ").encode()
key = input("Key (K) = ").encode()

encrypted = block_encrypt(plaintext, iv, key)

decrypted = block_decrypt(encrypted, iv, key)
print("Decrypted = ", decrypted)    
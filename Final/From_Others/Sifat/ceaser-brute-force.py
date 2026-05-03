def brute_force_caesar(cipher_text):
    print("\nPossible decryptions:\n")
    
    for key in range(1, 26): 
        decrypted = ""
        
        for char in cipher_text:
            if char.isalpha():
                decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            else:
                decrypted += char
        
        print(f"Key {key:5}: {decrypted}")

cipher = input("Enter ciphertext: ")
brute_force_caesar(cipher)
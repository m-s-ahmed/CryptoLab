# Diffie-Hellman Key Exchange with User Input

# Function for modular exponentiation
def power(base, exp, mod):
    return pow(base, exp, mod)

# Take public values from user
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

# Take private keys from users
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

# Compute public keys
A = power(g, a, p)  # Alice's public key
B = power(g, b, p)  # Bob's public key

print("\n--- Public Keys ---")
print("Alice's public key (A):", A)
print("Bob's public key (B):", B)

# Compute shared secret keys
shared_key_alice = power(B, a, p)
shared_key_bob = power(A, b, p)

print("\n--- Shared Secret Keys ---")
print("Alice's shared key:", shared_key_alice)
print("Bob's shared key:", shared_key_bob)

# Verify both keys match
if shared_key_alice == shared_key_bob:
    print("\n✅ Key exchange successful!")
else:
    print("\n❌ Key exchange failed!")
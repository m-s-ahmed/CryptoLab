# Diffie-Hellman Key Exchange (User Input Version)

# Step 1: Take public inputs
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a generator (g): "))

# Step 2: Private keys input
alice_private = int(input("Enter Alice's private key: "))
bob_private = int(input("Enter Bob's private key: "))

# Step 3: Compute public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\n--- Public Keys ---")
print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

# Step 4: Compute shared secret
alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

print("\n--- Shared Secret ---")
print("Alice's Computed Secret:", alice_shared)
print("Bob's Computed Secret:", bob_shared)

# Step 5: Verification
if alice_shared == bob_shared:
    print("\n✅ Key Exchange Successful! Shared key =", alice_shared)
else:
    print("\n❌ Error! Keys do not match.")
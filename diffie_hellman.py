
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

# Generate public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)

# Compute shared secret keys
key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Shared key computed by Alice:", key1)
print("Shared key computed by Bob:", key2)

# Verify
if key1 == key2:
    print("Verification: Shared keys are identical.")
else:
    print("Verification: Shared keys are not identical.")


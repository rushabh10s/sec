from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

# Step 1: Generate keys for Alice
print("STEP 1: KEY GENERATION")

alice_key = RSA.generate(2048)
alice_private = alice_key
alice_public = alice_key.publickey()

print("Alice's public and private keys generated.")

# Step 2: Alice writes an email
print("\nSTEP 2: ALICE WRITES EMAIL")
message = input("Alice, enter your email message: ")
print("Original Message:", message)

# Step 3: Alice hashes the message
print("\nSTEP 3: HASHING")
h = SHA256.new(message.encode())
print("SHA-256 Hash:", h.hexdigest())

# Step 4: Alice signs the hash
print("\nSTEP 4: DIGITAL SIGNING")
signature = pkcs1_15.new(alice_private).sign(h)
print("Alice signs using her private key.")
print("Digital Signature:", signature.hex())

# Step 5: Send email and signature to Bob
print("\nSTEP 5: TRANSMISSION")
received_message = message
received_signature = signature
print("Alice sends the message and signature to Bob.")

# Step 6: Option to modify received message
print("\nSTEP 6: MESSAGE TAMPERING")
choice = input("Modify received message? (yes/no): ")

if choice.lower() == "yes":
    received_message = input("Enter modified message: ")

print("Message received by Bob:", received_message)

# Step 7: Bob verifies the signature
print("\nSTEP 7: SIGNATURE VERIFICATION")
received_hash = SHA256.new(received_message.encode())
print("Bob calculates SHA-256 hash:", received_hash.hexdigest())
print("Bob verifies using Alice's public key.")

try:
    pkcs1_15.new(alice_public).verify(
        received_hash, received_signature
    )
    print("\nFINAL STATUS: SIGNATURE VALID")
    print("Message integrity verified.")
except (ValueError, TypeError):
    print("\nFINAL STATUS: SIGNATURE INVALID")
    print("Message may have been modified.")


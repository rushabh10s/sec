
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1

# Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Original message
message = b"Hello World"

# Generate SHA-1 hash
h = SHA1.new(message)
print("SHA-1 Hash:", h.hexdigest())

# Sign the hash using private key
signature = pkcs1_15.new(private_key).sign(h)
print("Digital Signature:", signature.hex())

# Verify signature
try:
    pkcs1_15.new(public_key).verify(SHA1.new(message), signature)
    print("Signature valid. Message is authentic.")
except (ValueError, TypeError):
    print("Signature invalid. Message is tampered!")

# Test tampering
tampered_message = b"Hello World!"
print("\nTesting tampered message:")

try:
    pkcs1_15.new(public_key).verify(
        SHA1.new(tampered_message), signature
    )
    print("Signature valid.")
except (ValueError, TypeError):
    print("Tampering detected!")

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# Generate RSA key pair
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

# Display keys
print("Public Key:")
print(public_key.export_key().decode())

print("\nPrivate Key:")
print(private_key.export_key().decode())


# Get plaintext
text = input("\nEnter plaintext: ")

print("\nPlaintext:", text)


# Encryption using public key
cipher = PKCS1_OAEP.new(public_key)

ciphertext = cipher.encrypt(text.encode())

print("Encrypted Ciphertext (Hex):")
print(ciphertext.hex())


# Decryption using private key
cipher = PKCS1_OAEP.new(private_key)

decrypted = cipher.decrypt(ciphertext).decode()

print("\nDecrypted Plaintext:", decrypted)


# Verification
if decrypted == text:
    print("Verification: Plaintext matches.")
else:
    print("Verification: Plaintext does not match.")

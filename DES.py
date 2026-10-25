from Crypto.Cipher import DES


def encrypt(text, key):
    # Add X padding
    while len(text) % 8 != 0:
        text += "X"

    cipher = DES.new(key.encode(), DES.MODE_ECB)

    encrypted = cipher.encrypt(text.encode())

    return encrypted


def decrypt(ciphertext, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)

    decrypted = cipher.decrypt(ciphertext)

    return decrypted.decode()


# Input
text = input("Enter plaintext: ")
key = input("Enter 8-byte key: ")

# Check key length
if len(key) != 8:
    print("Key must be exactly 8 bytes.")
else:
    print("\nPlaintext:", text)
    print("Secret key:", key)
    ciphertext = encrypt(text, key)
    print("Encrypted ciphertext (Hex):", ciphertext.hex())
    decrypted = decrypt(ciphertext, key)
    print("Decrypted plaintext:", decrypted)

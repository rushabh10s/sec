from Crypto.Cipher import AES

def encrypt(text, key):
    while len(text.encode()) % 16 != 0:
        text += "X"

    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return cipher.encrypt(text.encode())


def decrypt(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).decode()
    return plaintext.rstrip("X")


text = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be exactly 16 bytes.")
else:
    ciphertext = encrypt(text, key)
    print("Encrypted ciphertext (Hex):", ciphertext.hex())

    decrypted = decrypt(ciphertext, key)
    print("Decrypted plaintext:", decrypted)

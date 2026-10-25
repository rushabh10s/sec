from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import os

# Option 1: Generate RSA keys
def generate_keys():
    key = RSA.generate(2048)

    f = open("private.pem", "wb")
    f.write(key.export_key())
    f.close()

    f = open("public.pem", "wb")
    f.write(key.publickey().export_key())
    f.close()

    print("RSA keys generated and saved successfully!")
    print("\nPrivate Key:\n", key.export_key().decode())
    print("\nPublic Key:\n", key.publickey().export_key().decode())


# Option 2: Sign a message
def sign_message():
    if not os.path.exists("private.pem"):
        print("Generate keys first!")
        return

    f = open("private.pem", "rb")
    private_key = RSA.import_key(f.read())
    f.close()

    message = input("Enter message: ")
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)

    print("Original Message:", message)
    print("SHA-256 Digest:", h.hexdigest())
    print("Digital Signature:", signature.hex())


# Option 3: Verify a signature
def verify_signature():
    if not os.path.exists("public.pem"):
        print("Generate keys first!")
        return

    f = open("public.pem", "rb")
    public_key = RSA.import_key(f.read())
    f.close()

    message = input("Enter original message: ")
    signature = input("Enter signature in hex: ")

    try:
        h = SHA256.new(message.encode())
        sig = bytes.fromhex(signature)
        pkcs1_15.new(public_key).verify(h, sig)
        print("Signature is VALID.")
        print("Message is authentic and unchanged.")
    except (ValueError, TypeError):
        print("Signature is INVALID.")
        print("Message may have been altered.")


# Option 4: Demonstrate message tampering
def tampering():
    if not os.path.exists("private.pem"):
        print("Generate keys first!")
        return

    f = open("private.pem", "rb")
    private_key = RSA.import_key(f.read())
    f.close()

    message = input("Enter message: ")

    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)

    modified = message + "X"

    print("Original Message:", message)
    print("Modified Message:", modified)

    try:
        h2 = SHA256.new(modified.encode())
        pkcs1_15.new(private_key.publickey()).verify(h2, signature)
        print("Signature is VALID.")
    except (ValueError, TypeError):
        print("Verification FAILED!")
        print("Message has been altered.")


# Main menu
while True:
    print("\n=========== DIGITAL SIGNATURE SYSTEM ===========")
    print("1. Generate RSA Public and Private Keys")
    print("2. Digitally Sign a Message")
    print("3. Verify a Digital Signature")
    print("4. Demonstrate Message Tampering")
    print("5. Exit")
    print("================================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_keys()
    elif choice == "2":
        sign_message()
    elif choice == "3":
        verify_signature()
    elif choice == "4":
        tampering()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Enter 1 to 5.")

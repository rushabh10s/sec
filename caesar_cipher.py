def encrypt(text, key):
    s = ""
    for i in text:
        if i.isalpha():
            if i.isupper():
                s += chr((ord(i) - ord('A') + key)%26 + ord('A'))
            elif i.islower():
                s += chr((ord(i) - ord('a') + key)%26 + ord('a'))
        else:
            s+=i
    return s


def decrypt(text, key):
    return encrypt(text, -key)

def brute_force(text):
    for i in range(26):
        print("key :", i , "plaintext : ", decrypt(text, i))

while True:
    print("1. encrypt\n2.decrypt\n3.brute force\n4. exit")
    ch = int(input("enter choice: "))
    if ch == 1:
        txt = input("Enter plain text: ")
        key = int(input("Enter key: "))
        print("ciphertext: ", encrypt(txt, key))
    elif ch == 2:
        txt = input("Enter cipher text: ")
        key = int(input("Enter key: "))
        print("plaintext: ", decrypt(txt, key))

    elif ch == 3:
        txt = input("Enter cipher text: ")
        brute_force(txt)
    else:
        break
        

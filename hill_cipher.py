import numpy as np
from math import gcd

key = np.array([[3, 3], [2, 5]])

def encrypt(text, key):
    text = text.upper()

    if len(text) % 2 != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):
        p = np.array([[ord(text[i]) - 65],[ord(text[i+1]) - 65]])

        c = np.dot(key, p) % 26

        result += chr(int(c[0][0]) + 65)
        result += chr(int(c[1][0]) + 65)

    return result


def inverse(key):
    a, b = key[0]
    c, d = key[1]

    det = (a*d - b*c)%26

    if gcd(det, 26) != 1:
        raise ValueError("Inverse does not exist")

    det_inv = pow(det, -1, 26)

    adj = np.array([[d, -b], [-c, a]])

    return (det_inv * adj) % 26


def decrypt(text, key):
    inv = inverse(key)
    result = ""

    for i in range(0, len(text), 2):
        c = np.array([[ord(text[i]) - 65],
                      [ord(text[i+1]) - 65]])

        p = np.dot(inv, c) % 26

        result += chr(int(p[0][0]) + 65)
        result += chr(int(p[1][0]) + 65)

    return result


text = input("Enter plaintext: ").upper()

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

print("Inverse key matrix:")
print(inverse(key))

print("Decrypted:", decrypt(encrypted, key))


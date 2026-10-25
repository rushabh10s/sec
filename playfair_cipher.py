def matrix(key):
    key = key.upper().replace("J", "I")
    alphab = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    s = ""
    for i in key + alphab:
        if i.isalpha() and i not in s:
            s += i

    mat = []
    for i in range(0, 25, 5):
        mat.append(list(s[i:i+5]))

    return mat


def find_position(mat, ch):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j


def prepare_text(txt):
    txt = txt.upper().replace("J", "I")
    result = ""
    i = 0

    while i < len(txt):
        a = txt[i]

        if i + 1 == len(txt):
            result += a + "X"
            i += 1
        else:
            b = txt[i+1]

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2

    return result


def encrypt(txt, mat):
    text = prepare_text(txt)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(mat, a)
        r2, c2 = find_position(mat, b)

        if r1 == r2:
            result += mat[r1][(c1+1) % 5]
            result += mat[r2][(c2+1) % 5]

        elif c1 == c2:
            result += mat[(r1+1) % 5][c1]
            result += mat[(r2+1) % 5][c2]

        else:
            result += mat[r1][c2]
            result += mat[r2][c1]

    return result


def decrypt(txt, mat):
    result = ""

    for i in range(0, len(txt), 2):
        a, b = txt[i], txt[i+1]
        r1, c1 = find_position(mat, a)
        r2, c2 = find_position(mat, b)

        if r1 == r2:
            result += mat[r1][(c1-1) % 5]
            result += mat[r2][(c2-1) % 5]

        elif c1 == c2:
            result += mat[(r1-1) % 5][c1]
            result += mat[(r2-1) % 5][c2]

        else:
            result += mat[r1][c2]
            result += mat[r2][c1]

    return result


key = "monarchy"
text = input("Enter plaintext: ").upper()

mat = matrix(key)

encrypted = encrypt(text, mat)
print("Encrypted text:", encrypted)

decrypted = decrypt(encrypted, mat)
print("Decrypted text:", decrypted)

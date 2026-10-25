def row_major_encrypt(text, cols):
    
    while len(text) % cols != 0:
        text += 'X'

    rows = len(text) // cols

    matrix = [['' for j in range(cols)] for i in range(rows)]

    k = 0
    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = text[k]
            k += 1

    # Read row-wise
    cipher = ""
    for i in range(rows):
        for j in range(cols):
            cipher += matrix[i][j]

    return matrix, cipher


def row_major_decrypt(cipher, cols):
    rows = len(cipher) // cols

    matrix = [['' for j in range(cols)] for i in range(rows)]

    # Fill row-wise
    k = 0
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = cipher[k]
            k += 1

    # Read column-wise
    text = ""
    for j in range(cols):
        for i in range(rows):
            text += matrix[i][j]

    return text


def column_major_encrypt(text, cols):
    # Add padding
    while len(text) % cols != 0:
        text += 'X'

    rows = len(text) // cols

    matrix = [['' for j in range(cols)] for i in range(rows)]

    # Fill row-wise
    k = 0
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = text[k]
            k += 1

    # Read column-wise
    cipher = ""
    for j in range(cols):
        for i in range(rows):
            cipher += matrix[i][j]

    return matrix, cipher


def column_major_decrypt(cipher, cols):
    rows = len(cipher) // cols

    matrix = [['' for j in range(cols)] for i in range(rows)]

    # Fill column-wise
    k = 0
    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = cipher[k]
            k += 1

    # Read row-wise
    text = ""
    for i in range(rows):
        for j in range(cols):
            text += matrix[i][j]

    return text


# Main program

text = input("Enter plaintext: ").upper()
cols = int(input("Enter number of columns: "))


# Row Major
matrix, cipher = row_major_encrypt(text, cols)

print("\nRow Major Encryption Matrix:")
for row in matrix:
    print(row)

print("Row Major Ciphertext:", cipher)

decrypted = row_major_decrypt(cipher, cols)
print("Row Major Decrypted Text:", decrypted)


# Column Major
matrix, cipher = column_major_encrypt(text, cols)

print("\nColumn Major Encryption Matrix:")
for row in matrix:
    print(row)

print("Column Major Ciphertext:", cipher)

decrypted = column_major_decrypt(cipher, cols)
print("Column Major Decrypted Text:", decrypted)

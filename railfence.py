def encrypt(text, key):
    rail = [[' ' for _ in range(len(text))] for _ in range(key)]
    row, step = 0, 1

    for col, ch in enumerate(text):
        rail[row][col] = ch

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    print("\nRail Fence Pattern:")
    for r in rail:
        print(' '.join(r))

    return ''.join(''.join(r).replace(' ', '') for r in rail)


def decrypt(text, key):
    pattern = []
    row, step = 0, 1

    for _ in text:
        pattern.append(row)
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    rail = []
    index = 0

    for r in range(key):
        count = pattern.count(r)
        rail.append(text[index:index + count])
        index += count

    result = ''
    for r in pattern:
        result += rail[r][0]
        rail[r] = rail[r][1:]

    return result


text = input("Enter plaintext: ")
key = int(input("Enter number of rails: "))

cipher = encrypt(text, key)
print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))

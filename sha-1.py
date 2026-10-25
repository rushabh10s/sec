import hashlib

while True:
    print("\n1. Generate SHA-1 Hash")
    print("2. Demonstrate Avalanche Effect")
    print("3. Compare Two Messages")
    print("4. SHA-1 Preprocessing")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter text: ")
        h = hashlib.sha1(text.encode()).hexdigest()

        print("Original Message:", text)
        print("SHA-1 Hash:", h)

    elif choice == '2':
        text = input("Enter text: ")

        if text == "":
            print("Enter a non-empty message.")
            continue

        modified = ('B' if text[0] == 'A' else 'A') + text[1:]

        h1 = hashlib.sha1(text.encode()).hexdigest()
        h2 = hashlib.sha1(modified.encode()).hexdigest()

        print("Original Message:", text)
        print("Original Hash:", h1)
        print("Modified Message:", modified)
        print("Modified Hash:", h2)

    elif choice == '3':
        text1 = input("Enter first message: ")
        text2 = input("Enter second message: ")

        h1 = hashlib.sha1(text1.encode()).hexdigest()
        h2 = hashlib.sha1(text2.encode()).hexdigest()

        print("Hash 1:", h1)
        print("Hash 2:", h2)

        if h1 == h2:
            print("Messages are identical.")
        else:
            print("Messages are different.")

    elif choice == '4':
        text = input("Enter a sentence: ")
        data = text.encode()
        length = len(data) * 8

        binary = ''

        for b in data:
            binary = binary + format(b, '08b')
        padded = binary + '1'

        while len(padded) % 512 != 448:
            padded += '0'

        padded += format(length, '064b')

        print("Original Binary:", binary)
        print("After Padding:", padded)
        print("Total Blocks:", len(padded) // 512)

        for i in range(0, len(padded), 512):
            print("Block", i // 512 + 1, ":", padded[i:i+512])

        print("SHA-1 Hash:", hashlib.sha1(data).hexdigest())

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")


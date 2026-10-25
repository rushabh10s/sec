
import hashlib
import os
import json


def md5(text):
    return hashlib.md5(text.encode()).hexdigest()


def file_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


while True:
    print("\n1. Generate MD5")
    print("2. Verify Message Integrity")
    print("3. Avalanche Effect")
    print("4. File MD5")
    print("5. Compare MD5, SHA-1 and SHA-256")
    print("6. Exit")
    print("7. File Integrity Monitoring")

    choice = input("Enter choice: ")

    if choice == '1':
        text = input("Enter text: ")
        print("MD5:", md5(text))

    elif choice == '2':
        text = input("Enter text: ")
        old_hash = input("Enter previous digest: ")

        if md5(text) == old_hash:
            print("Message Matches")
        else:
            print("Message Does Not Match")

    elif choice == '3':
        text1 = input("Enter original text: ")
        text2 = input("Enter modified text: ")

        print("Original MD5:", md5(text1))
        print("Modified MD5:", md5(text2))

    elif choice == '4':
        path = input("Enter file path: ")

        try:
            print("File MD5:", file_md5(path))
        except OSError:
            print("File not found.")

    elif choice == '5':
        text = input("Enter text: ")
        data = text.encode()

        print("MD5:", hashlib.md5(data).hexdigest())
        print("SHA-1:", hashlib.sha1(data).hexdigest())
        print("SHA-256:", hashlib.sha256(data).hexdigest())

    elif choice == '6':
        print("Exiting...")
        break

    elif choice == '7':
        folder = input("Enter folder path: ")

        if not os.path.isdir(folder):
            print("Folder not found.")
            continue

        record = "checksums.json"

        if os.path.exists(record):
            with open(record, "r") as f:
                old = json.load(f)
        else:
            old = {}

        current = {}

        for name in os.listdir(folder):
            path = os.path.join(folder, name)

            if os.path.isfile(path):
                current[name] = file_md5(path)

                if name not in old:
                    print(name, "- New File")
                elif old[name] == current[name]:
                    print(name, "- Not Modified")
                else:
                    print(name, "- Modified")

        for name in old:
            if name not in current:
                print(name, "- Missing File")

        with open(record, "w") as f:
            json.dump(current, f, indent=4)

        print("Checksum record updated.")

    else:
        print("Invalid choice.")

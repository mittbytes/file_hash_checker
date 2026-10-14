import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None


def save_hash(file_hash, hash_file="saved_hash.txt"):
    with open(hash_file, "w") as file:
        file.write(file_hash)

    print("Hash saved successfully!")


def check_file(file_path, hash_file="saved_hash.txt"):
    if not os.path.exists(hash_file):
        print("No saved hash found. Save a hash first.")
        return

    current_hash = calculate_hash(file_path)

    if current_hash is None:
        return

    with open(hash_file, "r") as file:
        original_hash = file.read().strip()

    print("\nOriginal hash:", original_hash)
    print("Current hash: ", current_hash)

    if current_hash == original_hash:
        print("\nRESULT: File unchanged. Hashes match.")
    else:
        print("\nWARNING: Hashes differ. File may have changed.")


def main():
    print("===== FILE HASH CHECKER =====")
    print("1. Calculate and save file hash")
    print("2. Check file integrity")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            path = input("Enter file path: ").strip()
            file_hash = calculate_hash(path)

            if file_hash is not None:
                print("\nSHA-256 hash:", file_hash)
                save_hash(file_hash)

        elif choice == "2":
            path = input("Enter file path: ").strip()
            check_file(path)

        elif choice == "3":
            print("Exiting File Hash Checker. Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()



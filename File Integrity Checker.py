import hashlib
import os
import json

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096, b"")):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
def save_hashes(directory, hash_file="hashes.json"):
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)

    with open(hash_file, "w") as f:
        json.dump(file_hashes, f)
    print(f"Hashes saved to {hash_file}")

def verify_hashes(directory, hash_file="hashes.json"):
    with open(hash_file, "r") as f:
        stored_hashes = json.load(f)

    for file_path, stored_hashes in stored_hashes.items():
        current_hash = calculate_hash(file_path)
        if current_hash != stored_hashes.items():
            print(f"WARNING: File has been changed: {file_path}")
        else:
            print(f"File is intact {file_path}")
def main():
    while True:
        choice = input("Enter'1' to save hashes, '2' to verify hashes, or 'q' to quit: ")
        if choice == '1':
            directory = input(" Enter the directory to hash: ")
            save_hashes(directory)
        elif choice == '2':
            directory = input("Enter the directory to verify: ")
            verify_hashes(directory)
        elif choice == 'q':
            break
        else:
            print(" Invalid Choice, Try Again")

if __name__ == "__main__":
    main()


        
        
# main.py
from encryption import encrypt_file, decrypt_file
from key_management import generate_key, save_key, get_key
from access_logs import log_access
from database import init_db
import os

# Run this code to create the database and tables


def main():
    init_db()
    
    print("Welcome to the Encrypted File Storage System")
    print("1. Encrypt a File")
    print("2. Decrypt a File")
    choice = input("Choose an option: ")
    
    if choice == '1':
        file_name = input("Enter the file name to encrypt: ")
        file_path = os.path.join('files', file_name)
        
        if os.path.exists(file_path):
            key = generate_key()
            encrypt_file(file_path, key)
            save_key(file_name, key)
            log_access(file_name, "encrypt")
            print(f"File {file_name} encrypted successfully.")
        else:
            print("File not found.")
    
    elif choice == '2':
        file_name = input("Enter the file name to decrypt: ")
        file_path = os.path.join('files', file_name)
        
        if os.path.exists(file_path):
            key = get_key(file_name)
            if key is not None:
                decrypt_file(file_path, key)
                log_access(file_name, "decrypt")
                print(f"File {file_name} decrypted successfully.")
            else:
                print("No encryption key found for this file.")
        else:
            print("File not found.")
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

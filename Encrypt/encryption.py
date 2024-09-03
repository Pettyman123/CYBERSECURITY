# encryption.py
import os



def custom_cipher_decrypt(ciphertext, key):
    decrypted = ''.join(chr((ord(char) - key) % 256) for char in ciphertext)
    return decrypted

def encrypt_file(file_path, key):
    with open(file_path, 'r') as file:
        content = file.read()
    
    encrypted_content = custom_cipher_encrypt(content, key)
    
    with open(file_path, 'w') as file:
        file.write(encrypted_content)

def decrypt_file(file_path, key):
    with open(file_path, 'r') as file:
        content = file.read()
    
    decrypted_content = custom_cipher_decrypt(content, key)
    
    with open(file_path, 'w') as file:
        file.write(decrypted_content)

def custom_cipher_encrypt(plaintext, key):
    if not plaintext:  # Check if plaintext is empty
        print("Warning: No content to encrypt")
    
    encrypted = ''.join(chr((ord(char) + key) % 256) for char in plaintext)
    return encrypted

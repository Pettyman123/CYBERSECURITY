# key_management.py
import os

def generate_key():
    return os.urandom(1)[0]

def save_key(file_name, key):
    from database import save_file_record
    save_file_record(file_name, key)

def get_key(file_name):
    from database import get_file_key
    return get_file_key(file_name)

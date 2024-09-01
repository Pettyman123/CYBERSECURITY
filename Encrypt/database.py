# database.py
import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect('db/storage.db')
    cursor = conn.cursor()
    
    # Create table for storing file information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            key INTEGER NOT NULL
        )
    ''')
    
    # Create table for access logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS access_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            action TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Save a new file record
def save_file_record(file_name, key):
    conn = sqlite3.connect('db/storage.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO files (file_name, key) VALUES (?, ?)', (file_name, key))
    
    conn.commit()
    conn.close()

# Retrieve the encryption key for a file
def get_file_key(file_name):
    conn = sqlite3.connect('db/storage.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT key FROM files WHERE file_name = ?', (file_name,))
    key = cursor.fetchone()
    
    conn.close()
    
    return key[0] if key else None

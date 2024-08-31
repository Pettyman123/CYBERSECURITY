# access_logs.py
import sqlite3

def log_access(file_name, action):
    conn = sqlite3.connect('db/storage.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO access_logs (file_name, action) VALUES (?, ?)', (file_name, action))
    
    conn.commit()
    conn.close()

import sqlite3

def insert_dummy_data():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('db/storage.db')
        cursor = conn.cursor()

        # Insert dummy data into the files table
        cursor.execute('''
            INSERT INTO files (file_name, key) 
            VALUES (?, ?)
        ''', ('testfile.txt', 123))

        # Insert dummy data into the access_logs table
        cursor.execute('''
            INSERT INTO access_logs (file_name, action) 
            VALUES (?, ?)
        ''', ('testfile.txt', 'encrypt'))

        # Commit the transaction
        conn.commit()

        print("Dummy data inserted successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == "__main__":
    insert_dummy_data()

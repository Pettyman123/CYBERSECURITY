# Encrypted File Storage System with Custom Cipher

## Overview
This project is a **secure file storage system** built using Python, featuring a **custom encryption algorithm** for file encryption and decryption. It also integrates an SQLite database for **key management** and **access logs**, ensuring a comprehensive, secure storage system for sensitive files.

## Features
- **Custom Cipher Encryption**: Uses a novel encryption method to protect file content.
- **File Encryption & Decryption**: Simple options for securely encrypting and decrypting files.
- **Key Management**: Securely stores encryption keys in an SQLite database.
- **Access Logging**: Logs file access events (encryption/decryption) with timestamps.

## File Structure
- **`main.py`**: User interface and main logic for encryption and decryption operations.
- **`encryption.py`**: Custom cipher encryption and decryption functions.
- **`database.py`**: SQLite database setup and management (keys and logs).
- **`insert_dummy_data.py`**: Script to insert sample data for testing purposes.

## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/your-username/encrypted-file-storage.git

2. Install dependencies (if required).
```
Run the main.py file to start the program:
python3 main.py
```
## Contribution
```
Fork the repository.
Create a new branch for your feature.
Submit a pull request with clear descriptions of your changes.
```
## Future Scope
Advanced encryption algorithms: Implement stronger and more secure encryption methods.
User authentication: Add user login to restrict access to files.
GUI development: Create a graphical interface for ease of use.
Feel free to contribute to the project by enhancing encryption, adding new features, or improving the existing system!

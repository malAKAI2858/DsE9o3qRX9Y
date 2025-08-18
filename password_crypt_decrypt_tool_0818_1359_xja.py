# 代码生成时间: 2025-08-18 13:59:16
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

"""
A simple password encryption and decryption tool using Python and Tkinter.
This program generates a key, encrypts, and decrypts a password provided by the user.
"""

# Generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Save the key to a file for later use
def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Load the key from a file for decryption
def load_key(filename='secret.key'):
    try:
        with open(filename, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        messagebox.showerror('Error', 'Key file not found.')
        return None

# Encrypt the password
def encrypt(password, key):
    try:
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password.decode()
    except Exception as e:
        messagebox.showerror('Error', f'Encryption error: {e}')
        return None

# Decrypt the password
def decrypt(encrypted_password, key):
    try:
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(encrypted_password.encode())
        return decrypted_password.decode()
    except Exception as e:
        messagebox.showerror('Error', f'Decryption error: {e}')
        return None

# Create the main application window
class PasswordToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Password Encryption/Decryption Tool')
        self.geometry('400x200')

        # Frame for input fields
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        # Original password and encrypted password labels
        tk.Label(input_frame, text='Original Password: ').grid(row=0, column=0, pady=5)
        tk.Label(input_frame, text='Encrypted Password: ').grid(row=1, column=0, pady=5)

        # Entry widgets for original and encrypted passwords
        self.original_password = tk.Entry(input_frame)
        self.original_password.grid(row=0, column=1)
        self.encrypted_password = tk.Entry(input_frame)
        self.encrypted_password.grid(row=1, column=1)

        # Buttons for encryption and decryption
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text='Encrypt', command=self.encrypt_password).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text='Decrypt', command=self.decrypt_password).pack(side=tk.LEFT, padx=10)

        # Load key from file on initialization
        self.key = load_key()
        if self.key is None:
            self.key = generate_key()
            save_key(self.key)

    def encrypt_password(self):
        password = self.original_password.get()
        if password:
            encrypted = encrypt(password, self.key)
            if encrypted:
                self.encrypted_password.delete(0, tk.END)
                self.encrypted_password.insert(0, encrypted)
            else:
                messagebox.showerror('Error', 'Failed to encrypt the password.')
        else:
            messagebox.showwarning('Warning', 'Please enter a password to encrypt.')

    def decrypt_password(self):
        encrypted = self.encrypted_password.get()
        if encrypted:
            decrypted = decrypt(encrypted, self.key)
            if decrypted:
                self.original_password.delete(0, tk.END)
                self.original_password.insert(0, decrypted)
            else:
                messagebox.showerror('Error', 'Failed to decrypt the password.')
        else:
            messagebox.showwarning('Warning', 'Please enter an encrypted password to decrypt.')

# Run the application
if __name__ == '__main__':
    app = PasswordToolApp()
    app.mainloop()
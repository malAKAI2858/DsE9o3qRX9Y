# 代码生成时间: 2025-08-11 06:19:36
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

"""
密码加密解密工具，使用tkinter界面与用户交互，采用cryptography库进行安全加密解密。
使用Fernet对称加密算法，需要预先生成密钥。
"""

# 密钥生成，保存在本地文件中，实际应用中应安全存储密钥
def generate_key():
    return Fernet.generate_key()

# 从文件中加载密钥
def load_key():
    try:
        with open('key.key', 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        return generate_key()

# 保存密钥到文件
def save_key(key):
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# 加密函数
def encrypt(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# 解密函数
def decrypt(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

# GUI界面
class PasswordToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Password Encryption/Decryption Tool')
        self.key = load_key()
        self.save_key_button = tk.Button(self.root, text='Save Key', command=self.save_key_action)
        self.save_key_button.pack()
        self.encrypt_button = tk.Button(self.root, text='Encrypt', command=self.encrypt_action)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(self.root, text='Decrypt', command=self.decrypt_action)
        self.decrypt_button.pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()
        self.result_label = tk.Label(self.root, text='')
        self.result_label.pack()

    def save_key_action(self):
        try:
            save_key(self.key)
            messagebox.showinfo('Success', 'Key saved successfully.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def encrypt_action(self):
        try:
            password = self.password_entry.get()
            encrypted_password = encrypt(password, self.key)
            self.result_label.config(text=f'Encrypted: {encrypted_password}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def decrypt_action(self):
        try:
            password = self.password_entry.get()
            decrypted_password = decrypt(password, self.key)
            self.result_label.config(text=f'Decrypted: {decrypted_password}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordToolApp(root)
    root.mainloop()
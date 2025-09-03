# 代码生成时间: 2025-09-04 05:01:04
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# 密码加密解密工具的主类
class PasswordCryptoTool:
    def __init__(self):
        # 初始化密钥
        self.key = None
        # 生成密钥
        self.generate_key()

    def generate_key(self):
        # 生成一个密钥并保存
        self.key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        # 从文件中加载密钥
        try:
            with open('key.key', 'rb') as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            self.generate_key()

    def encrypt(self, password):
        # 加密密码
        if not self.key:
            self.load_key()
        cipher_suite = Fernet(self.key)
        return cipher_suite.encrypt(password.encode()).decode()

    def decrypt(self, encrypted_password):
        # 解密密码
        if not self.key:
            self.load_key()
        cipher_suite = Fernet(self.key)
        try:
            return cipher_suite.decrypt(encrypted_password.encode()).decode()
        except Exception as e:
            print(e)
            return None

# 密码加密解密工具的GUI类
class PasswordCryptoToolGUI:
    def __init__(self, root):
        self.root = root
        self.crypto_tool = PasswordCryptoTool()
        self.create_widgets()

    def create_widgets(self):
        # 创建GUI组件
        self.password_label = tk.Label(self.root, text='Password:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()

        self.encrypted_label = tk.Label(self.root, text='Encrypted Password:')
        self.encrypted_label.pack()
        self.encrypted_entry = tk.Entry(self.root)
        self.encrypted_entry.pack()

        self.encrypt_button = tk.Button(self.root, text='Encrypt', command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(self.root, text='Decrypt', command=self.decrypt)
        self.decrypt_button.pack()

    def encrypt(self):
        # 加密按钮的回调函数
        password = self.password_entry.get()
        encrypted_password = self.crypto_tool.encrypt(password)
        self.encrypted_entry.delete(0, tk.END)
        self.encrypted_entry.insert(0, encrypted_password)

    def decrypt(self):
        # 解密按钮的回调函数
        encrypted_password = self.encrypted_entry.get()
        password = self.crypto_tool.decrypt(encrypted_password)
        if password:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        else:
            messagebox.showerror('Error', 'Failed to decrypt password')

# 创建主窗口并运行
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Password Crypto Tool')
    app = PasswordCryptoToolGUI(root)
    root.mainloop()
# 代码生成时间: 2025-09-09 01:03:35
import tkinter as tk
from tkinter import messagebox

# 用户身份认证类
class Authenticator:
    def __init__(self):
        """初始化用户认证系统"""
        self.users = {"admin": "password123"}  # 存储用户名和密码

    def authenticate(self, username, password):
        """验证用户名和密码是否匹配"""
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

    def register_user(self, username, password):
        """注册新用户"""
        if username in self.users:
            raise ValueError("Username already exists.")
        else:
            self.users[username] = password

# 创建主窗口
class AuthApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Authentication")
        self.authenticator = Authenticator()
        self.create_widgets()

    def create_widgets(self):
        # 标签和输入框
        tk.Label(self, text="Username: ").grid(row=0)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self, text="Password: ").grid(row=1)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        # 登录按钮
        tk.Button(self, text="Login", command=self.login).grid(row=2, column=1)

        # 注册按钮
        tk.Button(self, text="Register", command=self.register).grid(row=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            if self.authenticator.authenticate(username, password):
                messagebox.showinfo("Login", "Login successful!")
            else:
                messagebox.showerror("Login", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Login Error", str(e))

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.authenticator.register_user(username, password)
            messagebox.showinfo("Registration", "User registered successfully!")
        except ValueError as ve:
            messagebox.showerror("Registration Error", str(ve))
        except Exception as e:
            messagebox.showerror("Registration Error", str(e))

if __name__ == "__main__":
    app = AuthApp()
    app.mainloop()
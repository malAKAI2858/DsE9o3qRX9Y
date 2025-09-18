# 代码生成时间: 2025-09-18 10:47:13
import tkinter as tk
from tkinter import messagebox
from getpass import getpass

"""
访问权限控制的GUI程序，使用TKinter框架实现。
允许用户输入用户名和密码，进行验证。
"""

class AccessControlApp:
    def __init__(self, root):
        # 设置窗口标题和大小
        self.root = root
        self.root.title('Access Control')
        self.root.geometry('300x200')

        # 创建用户名和密码输入框
        self.username_label = tk.Label(root, text='Username:')
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text='Password:')
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()

        # 登录按钮
        self.login_button = tk.Button(root, text='Login', command=self.login)
        self.login_button.pack()

    def login(self):
        """
        用户登录方法。
        检查用户名和密码是否正确。
        """
        # 获取用户输入
        username = self.username_entry.get()
        password = self.password_entry.get()

        # 这里应该替换为实际的验证逻辑
        if self.validate_credentials(username, password):
            messagebox.showinfo('Success', 'Login successful!')
        else:
            messagebox.showerror('Error', 'Invalid username or password')

    def validate_credentials(self, username, password):
        """
        验证用户名和密码。
        这里使用硬编码的用户名和密码作为示例。
        """
        # 硬编码的用户名和密码
        correct_username = 'admin'
        correct_password = 'password123'

        # 验证用户名和密码
        return username == correct_username and password == correct_password

# 创建主窗口
root = tk.Tk()

# 创建应用程序实例
app = AccessControlApp(root)

# 运行主循环
root.mainloop()
# 代码生成时间: 2025-09-06 19:53:25
import tkinter as tk
from tkinter import messagebox

# 用户权限管理系统
class UserPermissionManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("User Permission Management")
        self.root.geometry("400x300")

        # 添加用户框
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        # 添加权限框
        self.permission_label = tk.Label(self.root, text="Permission Level (1-3): ")
        self.permission_label.pack()
        self.permission_entry = tk.Entry(self.root)
        self.permission_entry.pack()

        # 添加按钮
        self.add_button = tk.Button(self.root, text="Add User", command=self.add_user)
        self.add_button.pack()

        # 用户数据存储
        self.users = {}

    def add_user(self):
        "
# 代码生成时间: 2025-08-02 12:01:13
import tkinter as tk
from tkinter import messagebox

# 引入数据库连接库
import sqlite3

class SQLInjectionPreventionApp:
    """防止SQL注入的Tkinter应用程序"""
    def __init__(self, master):
        self.master = master
        self.master.title('SQL Injection Prevention')
        self.create_widgets()

    def create_widgets(self):
        # 创建输入框
        self.username_label = tk.Label(self.master, text='Username:')
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1)

        # 创建密码输入框
        self.password_label = tk.Label(self.master, text='Password:')
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.master, show='*')
        self.password_entry.grid(row=1, column=1)

        # 创建登录按钮
        self.login_button = tk.Button(self.master, text='Login', command=self.login)
        self.login_button.grid(row=2, column=1)

    def login(self):
        # 获取输入的用户名和密码
        username = self.username_entry.get()
        password = self.password_entry.get()

        # 使用参数化查询防止SQL注入
        try:
            conn = sqlite3.connect('application.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo('Success', 'Login successful')
            else:
                messagebox.showerror('Error', 'Invalid username or password')
            cursor.close()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror('Database Error', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = SQLInjectionPreventionApp(root)
    root.mainloop()
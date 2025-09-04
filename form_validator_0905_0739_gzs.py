# 代码生成时间: 2025-09-05 07:39:42
import tkinter as tk
from tkinter import messagebox

"""
表单数据验证器
"""

class FormValidator:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Validator")

        # 创建标签和输入框
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=1, column=0)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=1, column=1)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=2, column=0)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=2, column=1)

        # 创建提交按钮
        self.submit_button = tk.Button(master, text="Submit", command=self.validate)
        self.submit_button.grid(row=3, column=0, columnspan=2)

    def validate(self):
        # 验证姓名
        name = self.entry_name.get()
        if not name:
            messagebox.showerror("Error", "Name is required")
            return

        # 验证邮箱
        email = self.entry_email.get()
        if not email or not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email address")
            return

        # 验证密码
        password = self.entry_password.get()
        if not password or len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return

        # 如果所有验证通过，显示信息
        messagebox.showinfo("Success", "Form validated successfully")

    def validate_email(self, email):
        """
        验证邮箱地址是否有效
        """
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

if __name__ == "__main__":
    root = tk.Tk()
    app = FormValidator(root)
    root.mainloop()
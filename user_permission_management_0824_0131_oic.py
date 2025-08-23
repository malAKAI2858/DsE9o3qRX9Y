# 代码生成时间: 2025-08-24 01:31:27
import tkinter as tk
from tkinter import messagebox

"""
用户权限管理系统 - Python & Tkinter实现
"""

class UserPermissionManagement:
    def __init__(self, master):
        """
        初始化用户权限管理系统界面
        :param master: Tkinter的主窗口
        """
        self.master = master
        self.master.title('用户权限管理系统')
        self.master.geometry('400x300')
        
        # 创建用户列表
        self.user_list = []
        
        # 用户列表的标签和滚动条
        self.user_label = tk.Label(master, text='用户列表:')
        self.user_label.pack()
        self.user_listbox = tk.Listbox(master, height=10, width=50)
        self.user_listbox.pack()
        self.scrollbar = tk.Scrollbar(master, orient='vertical')
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.user_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.user_listbox.yview)

        # 添加用户按钮
        self.add_button = tk.Button(master, text='添加用户', command=self.add_user)
        self.add_button.pack()

        # 删除用户按钮
        self.remove_button = tk.Button(master, text='删除用户', command=self.remove_user)
        self.remove_button.pack()

        # 设置用户权限按钮
        self.set_permission_button = tk.Button(master, text='设置用户权限', command=self.set_user_permission)
        self.set_permission_button.pack()

    def add_user(self):
        """
        添加用户到用户列表
        """
        user_name = tk.simpledialog.askstring('输入', '请输入用户名:', parent=self.master)
        if user_name:
            self.user_listbox.insert(tk.END, user_name)
            self.user_list.append(user_name)
        else:
            messagebox.showerror('错误', '用户名不能为空')

    def remove_user(self):
        """
        从用户列表中删除用户
        """
        selected_index = self.user_listbox.curselection()
        if selected_index:
            self.user_listbox.delete(selected_index)
            self.user_list.pop(selected_index[0])
        else:
            messagebox.showerror('错误', '请选择一个用户')

    def set_user_permission(self):
        """
        设置用户权限
        """
        selected_index = self.user_listbox.curselection()
        if selected_index:
            user_name = self.user_listbox.get(selected_index)
            permission = tk.simpledialog.askstring('输入', '请输入用户权限:', parent=self.master)
            if permission:
                messagebox.showinfo('成功', f'用户 {user_name} 的权限已设置为 {permission}')
            else:
                messagebox.showerror('错误', '权限不能为空')
        else:
            messagebox.showerror('错误', '请选择一个用户')

def main():
    """
    程序的主入口
    """
    root = tk.Tk()
    app = UserPermissionManagement(root)
    root.mainloop()

if __name__ == '__main__':
    main()
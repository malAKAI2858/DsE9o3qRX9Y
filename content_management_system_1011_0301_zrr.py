# 代码生成时间: 2025-10-11 03:01:21
import tkinter as tk
from tkinter import messagebox

"""
内容管理系统（Content Management System）使用Tkinter框架实现。
"""

class ContentManagementSystem:
    def __init__(self, master):
        """
        初始化内容管理系统界面。
        :param master: Tkinter主窗口。
        """
        self.master = master
        self.master.title("内容管理系统")

        # 创建数据库列表
        self.database_list = []
        self.create_widgets()

    def create_widgets(self):
        """
        创建界面组件。
        """
        # 添加数据库按钮
        self.add_database_button = tk.Button(self.master, text="添加数据库", command=self.add_database)
        self.add_database_button.pack()

        # 数据库列表框
        self.database_listbox = tk.Listbox(self.master)
        self.database_listbox.pack()

        # 删除数据库按钮
        self.remove_database_button = tk.Button(self.master, text="删除数据库", command=self.remove_database)
        self.remove_database_button.pack()

    def add_database(self):
        """
        添加数据库。
        """
        database_name = simpledialog.askstring("输入", "请输入数据库名称：")
        if database_name:
            self.database_list.append(database_name)
            self.database_listbox.insert(tk.END, database_name)
        else:
            messagebox.showwarning("警告", "数据库名称不能为空！")

    def remove_database(self):
        """
        删除数据库。
        """
        selected_index = self.database_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("警告", "请选择要删除的数据库！")
        else:
            self.database_listbox.delete(selected_index)
            self.database_list.pop(selected_index[0])

# 主程序
if __name__ == "__main__":
    root = tk.Tk()
    app = ContentManagementSystem(root)
    root.mainloop()
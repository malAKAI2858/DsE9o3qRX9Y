# 代码生成时间: 2025-09-05 12:49:12
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import json

"""
这是一个使用Python和Tkinter框架创建的数据备份和恢复程序。
程序允许用户选择需要备份的文件或文件夹，并将备份保存在指定位置。
同时，用户也可以从备份文件中恢复数据。
"""

class DataBackupRestore:
    def __init__(self, root):
        """初始化程序界面"""
        self.root = root
        self.root.title('数据备份与恢复')
        self.root.geometry('400x200')

        # 创建按钮和输入框
        self.backup_button = tk.Button(root, text='备份数据', command=self.backup_data)
        self.backup_button.pack(pady=10)

        self.restore_button = tk.Button(root, text='恢复数据', command=self.restore_data)
        self.restore_button.pack(pady=10)

        self.backup_dir = tk.StringVar()
        self.restore_dir = tk.StringVar()

        # 创建输入框
        self.backup_entry = tk.Entry(root, textvariable=self.backup_dir, width=50)
        self.backup_entry.pack(pady=10)

        self.restore_entry = tk.Entry(root, textvariable=self.restore_dir, width=50)
        self.restore_entry.pack(pady=10)

        self.browse_button = tk.Button(root, text='浏览', command=self.browse_dir)
        self.browse_button.pack(pady=10)

    def backup_data(self):
        """备份数据"""
        try:
            # 获取用户选择的文件或文件夹
            file_path = filedialog.askopenfilename()
            if not file_path:
                return

            # 获取备份目录
            backup_dir = self.backup_dir.get()
            if not backup_dir:
                messagebox.showerror('错误', '请选择备份目录')
                return

            # 创建备份文件
            backup_file = os.path.join(backup_dir, os.path.basename(file_path) + '.json')
            if os.path.exists(backup_file):
                overwrite = messagebox.askyesno('覆盖备份', '备份文件已存在，是否覆盖？')
                if not overwrite:
                    return
            else:
                overwrite = True

            # 备份文件内容
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    data = f.read()
                    with open(backup_file, 'w') as f:
                        json.dump(data, f)
            elif os.path.isdir(file_path):
                with open(backup_file, 'w') as f:
                    json.dump(os.listdir(file_path), f)

            if overwrite:
                messagebox.showinfo('成功', '数据备份成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def restore_data(self):
        """恢复数据"""
        try:
            # 获取备份文件
            backup_file = filedialog.askopenfilename()
            if not backup_file:
                return

            # 获取恢复目录
            restore_dir = self.restore_dir.get()
            if not restore_dir:
                messagebox.showerror('错误', '请选择恢复目录')
                return

            # 恢复文件内容
            with open(backup_file, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    # 恢复文件夹
                    for name in data:
                        file_path = os.path.join(restore_dir, name)
                        if os.path.exists(file_path):
                            overwrite = messagebox.askyesno('覆盖文件', '文件已存在，是否覆盖？')
                            if not overwrite:
                                continue
                        shutil.copy(os.path.join(backup_file[:-4], name), file_path)
                else:
                    # 恢复文件
                    with open(os.path.join(restore_dir, os.path.basename(backup_file)[:-4]), 'w') as f:
                        f.write(data)
            messagebox.showinfo('成功', '数据恢复成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def browse_dir(self):
        """浏览目录"""
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.backup_dir.set(dir_path)
            self.restore_dir.set(dir_path)

if __name__ == '__main__':
    root = tk.Tk()
    app = DataBackupRestore(root)
    root.mainloop()
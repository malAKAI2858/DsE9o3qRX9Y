# 代码生成时间: 2025-09-22 15:27:09
import os
import tkinter as tk
from tkinter import filedialog, messagebox

"""
批量文件重命名工具
该工具使用TKINTER框架创建了一个简单的图形界面，
允许用户选择一个文件夹，然后为该文件夹中的所有文件提供一个
新的命名模式。
"""

class BatchRenameTool:
    def __init__(self, master):
        # 创建主窗口
        self.master = master
        self.master.title('批量文件重命名工具')

        # 创建文件夹选择按钮
        self.folder_btn = tk.Button(master, text='选择文件夹', command=self.select_folder)
        self.folder_btn.pack()

        # 创建命名模式输入框
        self.pattern_entry = tk.Entry(master)
        self.pattern_entry.pack()

        # 创建重命名按钮
        self.rename_btn = tk.Button(master, text='重命名文件', command=self.rename_files)
        self.rename_btn.pack()

        # 文件夹路径变量
        self.folder_path = ''

    def select_folder(self):
        # 选择文件夹
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo('信息', '文件夹选择成功')
        else:
            messagebox.showerror('错误', '未选择文件夹')

    def rename_files(self):
        # 检查是否选择了文件夹
        if not self.folder_path:
            messagebox.showerror('错误', '请先选择文件夹')
            return

        # 获取命名模式
        pattern = self.pattern_entry.get()
        if not pattern:
            messagebox.showerror('错误', '请输入命名模式')
            return

        # 重命名文件
        try:
            for i, filename in enumerate(os.listdir(self.folder_path)):
                if not filename.startswith('.'):  # 忽略隐藏文件
                    new_name = f"{pattern}_{i+1}{os.path.splitext(filename)[1]}"
                    os.rename(os.path.join(self.folder_path, filename), os.path.join(self.folder_path, new_name))
            messagebox.showinfo('信息', '文件重命名成功')
        except Exception as e:
            messagebox.showerror('错误', f'重命名失败: {e}')


# 创建主窗口并运行
if __name__ == '__main__':
    root = tk.Tk()
    app = BatchRenameTool(root)
    root.mainloop()
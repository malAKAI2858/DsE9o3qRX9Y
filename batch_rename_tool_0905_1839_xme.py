# 代码生成时间: 2025-09-05 18:39:51
import os
import tkinter as tk
from tkinter import filedialog
# 优化算法效率
from tkinter import messagebox

"""
批量文件重命名工具，使用Python和Tkinter框架创建。
"""
# TODO: 优化性能

class BatchRenameTool:
    def __init__(self, root):
# 增强安全性
        """
        初始化界面和变量。
        :param root: Tkinter主窗口。
# TODO: 优化性能
        """
        self.root = root
        self.root.title('批量文件重命名工具')
        self.root.geometry('400x200')

        self.folder_path = ''
        self.pattern = ''
        self.new_pattern = ''

        # 创建界面元素
# 改进用户体验
        self.create_widgets()

    def create_widgets(self):
        # 选择文件夹按钮
        btn_browse = tk.Button(self.root, text='选择文件夹', command=self.browse_folder)
        btn_browse.pack(pady=10)

        # 输入原始文件名模式
        label_pattern = tk.Label(self.root, text='原始文件名模式：')
        label_pattern.pack()
        self.entry_pattern = tk.Entry(self.root, width=50)
        self.entry_pattern.pack()

        # 输入新文件名模式
# 改进用户体验
        label_new_pattern = tk.Label(self.root, text='新文件名模式：')
        label_new_pattern.pack()
        self.entry_new_pattern = tk.Entry(self.root, width=50)
        self.entry_new_pattern.pack()

        # 开始重命名按钮
# FIXME: 处理边界情况
        btn_rename = tk.Button(self.root, text='开始重命名', command=self.rename_files)
        btn_rename.pack(pady=10)
# 优化算法效率

    def browse_folder(self):
        """
# 扩展功能模块
        浏览文件夹并获取路径。
        """
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo('信息', '文件夹选择成功')
        else:
            messagebox.showwarning('警告', '未选择文件夹')
# 添加错误处理

    def rename_files(self):
        """
        根据输入的模式批量重命名文件。
# 改进用户体验
        """
        if not self.folder_path:
            messagebox.showwarning('警告', '请先选择文件夹')
            return
# NOTE: 重要实现细节

        self.pattern = self.entry_pattern.get()
        self.new_pattern = self.entry_new_pattern.get()

        if not self.pattern or not self.new_pattern:
            messagebox.showwarning('警告', '请输入文件名模式')
            return

        try:
            for filename in os.listdir(self.folder_path):
# NOTE: 重要实现细节
                if filename.startswith(self.pattern):
                    # 构建新的文件名
                    new_filename = filename.replace(self.pattern, self.new_pattern)
                    # 重命名文件
                    os.rename(os.path.join(self.folder_path, filename),
                               os.path.join(self.folder_path, new_filename))
            messagebox.showinfo('信息', '文件重命名完成')
        except Exception as e:
            messagebox.showerror('错误', f'重命名失败：{str(e)}')

if __name__ == '__main__':
    root = tk.Tk()
    app = BatchRenameTool(root)
    root.mainloop()
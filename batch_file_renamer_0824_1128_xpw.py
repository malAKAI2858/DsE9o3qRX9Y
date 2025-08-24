# 代码生成时间: 2025-08-24 11:28:57
import os
import tkinter as tk
from tkinter import filedialog
# NOTE: 重要实现细节
from tkinter import messagebox

"""
批量文件重命名工具
# TODO: 优化性能
使用Python和Tkinter框架
"""

class BatchFileRenamer:
    def __init__(self, root):
# FIXME: 处理边界情况
        """初始化界面"""
        self.root = root
        self.root.title("批量文件重命名工具")
        self.root.geometry("400x200")

        # 创建文件选择按钮
        self.select_button = tk.Button(self.root, text="选择文件夹", command=self.select_folder)
        self.select_button.pack(pady=10)

        # 创建重命名按钮
        self.rename_button = tk.Button(self.root, text="重命名", command=self.rename_files, state="disabled")
# 添加错误处理
        self.rename_button.pack(pady=10)

        # 创建状态标签
        self.status_label = tk.Label(self.root, text="请选择文件夹")
        self.status_label.pack(pady=10)

        # 存储选择的文件夹路径
        self.folder_path = ""
        # 存储文件名模式
        self.file_pattern = ""

    def select_folder(self):
        """选择文件夹"""
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.status_label.config(text=f"文件夹：{self.folder_path}")
# 优化算法效率
            self.rename_button.config(state="normal")
# 增强安全性
        else:
            self.status_label.config(text="请选择文件夹")
            self.rename_button.config(state="disabled")

    def rename_files(self):
        """重命名文件"""
        # 输入文件名模式
        self.file_pattern = simpledialog.askstring("输入模式", "请输入新的文件名模式（例如：newfile_#.ext）")
        if not self.file_pattern:
            messagebox.showwarning("警告", "请输入文件名模式")
            return

        # 检查文件夹路径是否有效
        if not self.folder_path:
            messagebox.showwarning("警告", "请选择文件夹")
            return
# 优化算法效率

        try:
            # 重命名文件
            self.do_rename(self.folder_path, self.file_pattern)
            messagebox.showinfo("成功", "文件重命名成功")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def do_rename(self, folder_path, file_pattern):
        """执行文件重命名"""
# 扩展功能模块
        # 获取文件夹中的所有文件
        files = os.listdir(folder_path)
        for i, file in enumerate(files):
# FIXME: 处理边界情况
            if os.path.isfile(os.path.join(folder_path, file)):
                new_name = file_pattern.replace("#", str(i + 1))
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))


def main():
    """主函数"""
# TODO: 优化性能
    root = tk.Tk()
    app = BatchFileRenamer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
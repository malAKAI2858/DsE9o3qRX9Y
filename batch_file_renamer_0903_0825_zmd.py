# 代码生成时间: 2025-09-03 08:25:38
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
批量文件重命名工具
该工具允许用户选择一个文件夹，并为该文件夹中的所有文件提供一个统一的前缀。
"""

def rename_files(directory, prefix):
    """
    对指定目录中的所有文件进行重命名，添加给定的前缀。
    """
    try:
        files = os.listdir(directory)
        for file in files:
            if not os.path.isdir(os.path.join(directory, file)):
                old_path = os.path.join(directory, file)
                new_path = os.path.join(directory, prefix + file)
                os.rename(old_path, new_path)
        messagebox.showinfo('成功', '文件重命名完成！')
    except Exception as e:
        messagebox.showerror('错误', str(e))


def select_directory():
    "
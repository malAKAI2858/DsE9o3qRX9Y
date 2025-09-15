# 代码生成时间: 2025-09-15 12:00:18
import tkinter as tk
from tkinter import messagebox
import hashlib

"""
哈希值计算工具
使用TKINTER框架创建GUI应用，用于计算文本的哈希值。
"""

class HashCalculator:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title('哈希值计算工具')

        # 创建输入框
        self.input_label = tk.Label(root, text='输入文本：')
        self.input_label.pack()
        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        # 创建选择哈希算法的下拉菜单
        self.hash_label = tk.Label(root, text='选择哈希算法：')
        self.hash_label.pack()
        self.hash_var = tk.StringVar()
        self.hash_options = ['MD5', 'SHA1', 'SHA256', 'SHA512']
        self.hash_var.set(self.hash_options[0])  # 默认选择MD5
        self.hash_menu = tk.OptionMenu(root, self.hash_var, *self.hash_options)
        self.hash_menu.pack()

        # 创建计算按钮
        self.calculate_button = tk.Button(root, text='计算哈希值', command=self.calculate_hash)
        self.calculate_button.pack()

        # 创建显示结果的标签
        self.result_label = tk.Label(root, text='')
        self.result_label.pack()

    def calculate_hash(self):
        "
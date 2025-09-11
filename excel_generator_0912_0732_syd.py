# 代码生成时间: 2025-09-12 07:32:06
import tkinter as tk
from tkinter import filedialog
import pandas as pd

"""
Excel表格自动生成器
通过TKINTER框架实现图形界面，允许用户自定义生成Excel表格。
"""

class ExcelGenerator:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title('Excel表格自动生成器')
        self.create_widgets()

    def create_widgets(self):
        """创建界面元素"""
        self.label = tk.Label(self.root, text='Excel文件名:', font=('Arial', 12))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.filename_entry = tk.Entry(self.root, width=50)
        self.filename_entry.grid(row=0, column=1, padx=10, pady=10)

        self.button_generate = tk.Button(self.root, text='生成Excel', command=self.generate_excel)
        self.button_generate.grid(row=1, column=1, padx=10, pady=10)

    def generate_excel(self):
        """生成Excel表格"""
        filename = self.filename_entry.get()
        if not filename.endswith('.xlsx'):
            filename += '.xlsx'

        try:
            # 使用Pandas创建一个空的Excel文件
            df = pd.DataFrame()
            df.to_excel(filename, index=False)
            self.status_message('Excel文件已生成: {}'.format(filename))
        except Exception as e:
            self.status_message('生成Excel文件失败: {}'.format(str(e)))

    def status_message(self, message):
        "
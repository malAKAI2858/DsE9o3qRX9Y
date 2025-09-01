# 代码生成时间: 2025-09-01 14:35:56
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

"""
CSV文件批量处理器
"""

class CSVBatchProcessor:
    def __init__(self, root):
        """
        初始化CSV文件批量处理器
        :param root: Tkinter窗口的根
        """
        self.root = root
        self.root.title('CSV文件批量处理器')

        # 创建按钮
        self.open_button = tk.Button(root, text='打开CSV文件', command=self.open_csv)
        self.open_button.pack()

        self.process_button = tk.Button(root, text='批量处理CSV文件', command=self.process_csv)
        self.process_button.pack()

    def open_csv(self):
        """
        打开CSV文件对话框
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            messagebox.showinfo('成功', '文件打开成功')
        else:
            messagebox.showerror('错误', '文件打开失败')

    def process_csv(self):
        """
        批量处理CSV文件
        """
        if not hasattr(self, 'file_path'):
            messagebox.showerror('错误', '请先打开CSV文件')
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                # 读取标题行
                header = next(csv_reader)

                # 处理每行数据
                for row in csv_reader:
                    # 对每行数据进行处理
                    # 例如：将数据存储到列表中
                    row_data = [cell.strip() for cell in row]
                    print(row_data)
                    
                    # 可以在这里添加更多的数据处理逻辑
                    # 如：保存到数据库、进行数据清洗等

        except Exception as e:
            messagebox.showerror('错误', f'处理CSV文件时出错：{e}')

    def run(self):
        """
        运行Tkinter事件循环
        """
        self.root.mainloop()

if __name__ == '__main__':
    # 创建Tkinter窗口
    root = tk.Tk()

    # 创建CSV文件批量处理器实例
    csv_processor = CSVBatchProcessor(root)

    # 运行Tkinter事件循环
    csv_processor.run()
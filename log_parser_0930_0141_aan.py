# 代码生成时间: 2025-09-30 01:41:28
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

"""
日志文件解析工具，使用Python和Tkinter框架创建。
功能：解析日志文件，提取有用信息。
"""

class LogParser:
    def __init__(self, root):
        self.root = root
        self.root.title('日志文件解析工具')
        self.create_widgets()

    def create_widgets(self):
        # 文件选择按钮
        self.open_button = tk.Button(self.root, text='选择日志文件', command=self.open_file)
        self.open_button.pack()

        # 文本框，显示日志内容
        self.text_area = tk.Text(self.root, height=20, width=80)
        self.text_area.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(title='选择日志文件', filetypes=[('日志文件', '*.log'), ('所有文件', '*.*')])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    log_content = file.read()
                    self.parse_log(log_content)
            except Exception as e:
                messagebox.showerror('错误', f'读取文件出错：{str(e)}')

    def parse_log(self, log_content):
        # 使用正则表达式解析日志
        # 假设日志格式为：[时间戳] [日志级别] [日志信息]
        log_pattern = r'\[(.*?)\] \[(.*?)\] (.*?)(
|$)'
        pattern = re.compile(log_pattern)
        for match in pattern.finditer(log_content):
            timestamp, level, message = match.groups()
            # 处理日志信息
            print(f'{timestamp} - {level} - {message}')
            # 将解析后的日志信息显示在文本框中
            self.text_area.insert(tk.END, f'{timestamp} - {level} - {message}
')

# 主程序入口
if __name__ == '__main__':
    root = tk.Tk()
    app = LogParser(root)
    root.mainloop()
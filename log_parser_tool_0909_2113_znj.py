# 代码生成时间: 2025-09-09 21:13:40
import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os

"""
日志文件解析工具，使用Tkinter框架创建GUI。
功能：选择日志文件，解析并显示日志内容。
"""

class LogParserTool:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title('日志文件解析工具')
        self.root.geometry('600x400')

        # 文件选择按钮
        self.btn_select_file = tk.Button(root, text='选择日志文件', command=self.select_file)
        self.btn_select_file.pack(pady=10)

        # 显示文本框
        self.text_area = tk.Text(root, height=20, width=80)
        self.text_area.pack(pady=10)

    # 选择文件函数
    def select_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        try:
            self.parse_log(file_path)
        except Exception as e:
            messagebox.showerror('错误', f'解析日志文件出错：{e}')

    # 解析日志文件函数
    def parse_log(self, file_path):
        """
        解析日志文件内容，并将结果显示在文本框中。
        Args:
            file_path (str): 日志文件路径
        """
        # 检查文件是否存在
        if not os.path.exists(file_path):
            messagebox.showerror('错误', '文件不存在')
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                log_content = file.read()
                self.display_log_content(log_content)
        except UnicodeDecodeError:
            messagebox.showerror('错误', '文件编码错误，请确保文件是UTF-8编码')
        except Exception as e:
            messagebox.showerror('错误', f'读取文件出错：{e}')

    # 显示日志内容函数
    def display_log_content(self, log_content):
        """将解析后的日志内容显示在文本框中"""
        self.text_area.delete('1.0', tk.END)  # 清空文本框
        self.text_area.insert(tk.END, log_content)  # 插入日志内容

# 主函数
def main():
    """程序主入口"""
    root = tk.Tk()
    LogParserTool(root)
    root.mainloop()

if __name__ == '__main__':
    main()
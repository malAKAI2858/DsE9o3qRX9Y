# 代码生成时间: 2025-08-06 17:22:59
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

# 设置日志文件的格式
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 错误日志收集器类
class ErrorLogCollector:
    def __init__(self, master):
        self.master = master
        self.master.title('Error Log Collector')
        self.create_widgets()

    def create_widgets(self):
        # 添加按钮，点击后打开文件对话框选择日志文件
        self.browse_button = tk.Button(self.master, text='Select Log File', command=self.select_log_file)
        self.browse_button.pack(pady=10)

        # 添加按钮，点击后保存日志到文件
        self.save_button = tk.Button(self.master, text='Save Log', command=self.save_log)
        self.save_button.pack(pady=10)

        # 添加文本框显示选择的日志文件
        self.log_text = tk.Text(self.master, height=10, width=50)
        self.log_text.pack(pady=10)

    def select_log_file(self):
        # 打开文件对话框，让用户选择日志文件
        file_path = filedialog.askopenfilename()
        if file_path:
            self.log_text.delete(1.0, tk.END)
            with open(file_path, 'r') as log_file:
                self.log_text.insert(tk.END, log_file.read())
        else:
            messagebox.showinfo('Info', 'No file selected')

    def save_log(self):
        # 检查文本框是否为空
        if self.log_text.get(1.0, tk.END).strip() == '':
            messagebox.showerror('Error', 'No log content to save')
            return

        # 获取当前日期和时间作为日志文件名
        now = datetime.datetime.now()
        log_filename = now.strftime('error_log_%Y-%m-%d_%H-%M-%S.log')

        # 保存日志到文件
        try:
            with open(log_filename, 'w') as log_file:
                log_file.write(self.log_text.get(1.0, tk.END))
            messagebox.showinfo('Success', f'Log saved as {log_filename}')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save log: {e}')

# 创建主窗口并运行程序
def main():
    root = tk.Tk()
    app = ErrorLogCollector(root)
    root.mainloop()

if __name__ == '__main__':
    main()
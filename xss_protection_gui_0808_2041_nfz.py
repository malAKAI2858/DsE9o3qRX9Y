# 代码生成时间: 2025-08-08 20:41:40
import tkinter as tk
from tkinter import messagebox

# 导入 HTML 转义库
from html import escape

class XssProtectionApp:
    """XSS攻击防护GUI应用"""

    def __init__(self, master):
        """初始化GUI应用"""
        self.master = master
        self.master.title("XSS Protection")

        # 创建输入框
        self.input_label = tk.Label(master, text="Enter Text: ")
        self.input_label.pack()
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        # 创建输出框
        self.output_label = tk.Label(master, text="Escaped Text: ")
        self.output_label.pack()
        self.output_entry = tk.Entry(master)
        self.output_entry.pack()

        # 创建转换按钮
        self.convert_button = tk.Button(master, text="Escape HTML", command=self.escape_html)
        self.convert_button.pack()

    def escape_html(self):
        """转义输入框中的HTML标签"""
        try:
            # 获取输入框中的文本
            input_text = self.input_entry.get()
            # 转义HTML标签
            escaped_text = escape(input_text)
            # 将转义后的文本显示在输出框中
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, escaped_text)
        except Exception as e:
            # 错误处理
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    # 创建应用实例
    app = XssProtectionApp(root)
    # 运行主循环
    root.mainloop()
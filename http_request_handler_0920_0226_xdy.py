# 代码生成时间: 2025-09-20 02:26:14
import tkinter as tk
from tkinter import messagebox
import requests
from threading import Thread


class HttpRequestHandler:
    """HTTP请求处理器类"""

    def __init__(self, master):
        """初始化GUI界面"""
        self.master = master
        self.master.title("HTTP Request Handler")

        # 创建输入框和标签
        self.url_label = tk.Label(master, text="URL: ")
        self.url_label.grid(row=0, column=0)
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1)

        # 创建按钮
        self.send_button = tk.Button(master, text="Send Request", command=self.send_request)
        self.send_button.grid(row=1, column=0, columnspan=2)

        # 创建结果显示区域
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=2, column=0, columnspan=2)

    def send_request(self):
        """发送HTTP请求并显示结果"""
        url = self.url_entry.get()
        self.result_text.delete(1.0, tk.END)  # 清空结果显示区域
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL.")
            return

        def request_thread():
            """线程函数，用于发送HTTP请求"""
            try:
                response = requests.get(url)
                self.result_text.insert(tk.END, response.text)
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", str(e))

        # 在新线程中发送请求，避免阻塞GUI
        Thread(target=request_thread).start()

# 创建主窗口
root = tk.Tk()

# 创建HttpRequestHandler实例
app = HttpRequestHandler(root)

# 运行主事件循环
root.mainloop()
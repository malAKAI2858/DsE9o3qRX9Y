# 代码生成时间: 2025-09-12 16:26:33
import tkinter as tk
from tkinter import messagebox
import requests
import threading
import json

"""
这是一个使用Python和Tkinter框架创建的程序，用于开发RESTful API接口。
程序提供了一个简单的界面，用户可以通过输入URL和请求参数来发送HTTP请求，并显示响应结果。
"""

class RestfulApiApp:
    def __init__(self, root):
        """初始化界面"""
        self.root = root
        self.root.title("RESTful API Interface")
        self.root.geometry("600x400")
        
        # 创建输入框和标签
        self.url_label = tk.Label(root, text="URL")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()
        
        self.method_label = tk.Label(root, text="Method")
        self.method_label.pack()
        self.method_combo = tk.Combobox(root, values=["GET", "POST", "PUT", "DELETE"])
        self.method_combo.pack()
        
        self.params_label = tk.Label(root, text="Params")
        self.params_label.pack()
        self.params_entry = tk.Entry(root, width=50)
        self.params_entry.pack()
        
        # 创建发送请求的按钮
        self.send_button = tk.Button(root, text="Send", command=self.send_request)
        self.send_button.pack()
        
        # 创建显示响应结果的文本框
        self.response_text = tk.Text(root, height=10, width=50)
        self.response_text.pack()
        
    def send_request(self):
        """发送HTTP请求并显示响应结果"""
        url = self.url_entry.get()
        method = self.method_combo.get()
        params = self.params_entry.get()
        
        # 将params字符串转换为字典
        if params:
            params_dict = eval(params)  # 这里使用eval()函数需要注意安全问题
        else:
            params_dict = {}
        
        # 发送请求
        try:
            response = None
            if method == "GET":
                response = requests.get(url, params=params_dict)
            elif method == "POST":
                response = requests.post(url, json=params_dict)
            elif method == "PUT":
                response = requests.put(url, json=params_dict)
            elif method == "DELETE":
                response = requests.delete(url)
            
            # 显示响应结果
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, response.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
        
# 创建主窗口并运行程序
if __name__ == '__main__':
    root = tk.Tk()
    app = RestfulApiApp(root)
    root.mainloop()
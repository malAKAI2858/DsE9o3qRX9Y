# 代码生成时间: 2025-09-03 21:13:37
import tkinter as tk
from tkinter import messagebox
import requests
import socket
import threading

"""
网络连接状态检查器，使用Python和Tkinter框架创建。
这个程序可以检查网络连接状态，并在GUI中显示结果。
"""

class NetworkStatusChecker:
    def __init__(self, master):
        """初始化界面"""
        self.master = master
        master.title("网络连接状态检查器")
        
        self.status_label = tk.Label(master, text="检查网络连接...
        ", font=("Helvetica", 12))
        self.status_label.pack(pady=20)
        
        self.check_button = tk.Button(master, text="检查网络连接",
                                      command=self.check_network_status)
        self.check_button.pack(pady=10)
        
    def check_network_status(self):
        """检查网络连接状态"""
        threading.Thread(target=self._check_network_status).start()
        
    def _check_network_status(self):
        """实际检查网络连接状态的方法"""
        try:
            response = requests.get("http://www.google.com", timeout=5)
            if response.status_code == 200:
                self.master.after(0, self.update_status, "网络连接正常！")
            else:
                self.master.after(0, self.update_status, "网络连接失败！")
        except (requests.ConnectionError, requests.Timeout):
            self.master.after(0, self.update_status, "网络连接失败！")
        except Exception as e:
            self.master.after(0, self.update_status, f"检查网络连接时发生错误：{e}")
        
    def update_status(self, status):
        """更新界面上的网络连接状态"""
        self.status_label.config(text=status)


def main():
    root = tk.Tk()
    app = NetworkStatusChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
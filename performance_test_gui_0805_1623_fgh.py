# 代码生成时间: 2025-08-05 16:23:08
import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime
import requests

"""
性能测试脚本GUI程序
允许用户输入URL和指定测试次数，然后启动性能测试
"""

class PerformanceTestGUI:
    def __init__(self, master):
        """
        初始化界面
        :param master: tkinter主窗口
        """
        self.master = master
        master.title("性能测试脚本")

        # 创建输入框和标签
        self.url_label = tk.Label(master, text="URL:")
        self.url_label.grid(row=0, column=0)
        self.url_entry = tk.Entry(master)
        self.url_entry.grid(row=0, column=1)

        self.times_label = tk.Label(master, text="测试次数：")
        self.times_label.grid(row=1, column=0)
        self.times_entry = tk.Entry(master)
        self.times_entry.grid(row=1, column=1)

        # 创建测试按钮
        self.start_button = tk.Button(master, text="开始测试", command=self.start_test)
        self.start_button.grid(row=2, column=0, columnspan=2)

        # 创建结果展示区域
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=2)

    def start_test(self):
        """
        开始性能测试
        :param self:
        :return: None
        """
        # 获取输入的URL和测试次数
        url = self.url_entry.get()
        times = int(self.times_entry.get())

        if not url or times <= 0:
            messagebox.showerror("错误", "请输入有效的URL和测试次数")
            return

        # 启动测试线程
        test_thread = threading.Thread(target=self.run_test, args=(url, times))
        test_thread.start()

    def run_test(self, url, times):
        """
        执行性能测试
        :param url: 测试的URL
        :param times: 测试次数
        :return: None
        """
        start_time = datetime.now()
        try:
            for i in range(times):
                requests.get(url)
        except requests.RequestException as e:
            self.result_text.insert(tk.END, f"请求失败：{e}
")
            return

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        self.result_text.insert(tk.END, f"完成{times}次请求，耗时{duration}秒
")

    def mainloop(self):
        """
        GUI主循环
        :return: None
        """
        self.master.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    gui = PerformanceTestGUI(root)
    gui.mainloop()
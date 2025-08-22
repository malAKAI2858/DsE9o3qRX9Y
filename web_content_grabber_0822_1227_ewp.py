# 代码生成时间: 2025-08-22 12:27:21
import tkinter as tk
# 添加错误处理
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
# 改进用户体验

"""
网页内容抓取工具，使用Python和Tkinter框架创建。
该工具允许用户输入网址，抓取网页内容，并显示在GUI界面上。
"""

class WebContentGrabberApp:
    def __init__(self, root):
        """
        初始化GUI界面
        :param root: Tkinter窗口的根对象
        """
        self.root = root
        self.root.title("网页内容抓取工具")

        # 创建输入框
        self.url_label = tk.Label(root, text="输入网址：")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # 创建抓取按钮
        self.grab_button = tk.Button(root, text="抓取网页内容", command=self.grab_web_content)
        self.grab_button.pack()
# 增强安全性

        # 创建显示框
        self.result_text = tk.Text(root, height=20, width=80)
        self.result_text.pack()
# 优化算法效率

    def grab_web_content(self):
        """
        抓取网页内容
# 增强安全性
        """
        # 获取用户输入的网址
        url = self.url_entry.get()

        # 错误处理
# NOTE: 重要实现细节
        if not url:
            messagebox.showerror("错误", "请输入网址")
            return

        try:
            # 发送HTTP请求
# 增强安全性
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
        except requests.RequestException as e:
# 添加错误处理
            messagebox.showerror("错误", f"请求失败：{e}")
            return

        try:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')
            # 清除脚本和样式
            for script in soup(["script", "style"]):
                script.decompose()
            # 获取正文内容
            content = soup.get_text(separator="
# 增强安全性
")
            # 显示在GUI界面上
# NOTE: 重要实现细节
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("错误", f"解析失败：{e}")

if __name__ == '__main__':
    # 创建Tkinter窗口
    root = tk.Tk()
    # 创建WebContentGrabberApp实例
    app = WebContentGrabberApp(root)
    # 启动事件循环
# 添加错误处理
    root.mainloop()
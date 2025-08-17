# 代码生成时间: 2025-08-18 04:54:38
import tkinter as tk
from tkinter import messagebox
import requests
# 扩展功能模块
from bs4 import BeautifulSoup
import threading
# 增强安全性

"""
A Python script using TKINTER to create a GUI for web content scraping.
It allows users to input a URL and retrieve the HTML content of the webpage.
"""

class WebContentGrabber:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Content Grabber")
# 增强安全性
        self.root.geometry("400x200")

        # URL input label and entry
        self.url_label = tk.Label(self.root, text="Enter URL: ")
        self.url_label.pack()
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack()

        # Fetch button
        self.fetch_button = tk.Button(self.root, text="Fetch Content", command=self.fetch_content)
# TODO: 优化性能
        self.fetch_button.pack()

        # Scrollbar and text area for displaying content
# 添加错误处理
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area = tk.Text(self.root, wrap=tk.WORD, yscrollcommand=self.scrollbar.set, width=60, height=10)
        self.text_area.pack()
        self.scrollbar.config(command=self.text_area.yview)

    def fetch_content(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return

        try:
            # Start a new thread to avoid blocking the GUI thread
            threading.Thread(target=self.grab_content, args=(url,)).start()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def grab_content(self, url):
        try:
            response = requests.get(url)
# 改进用户体验
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            html_content = response.text

            # Update the text area with the HTML content in the main thread
            self.text_area.config(state=tk.NORMAL)
            self.text_area.delete(1.0, tk.END)
# TODO: 优化性能
            self.text_area.insert(tk.END, html_content)
            self.text_area.config(state=tk.DISABLED)
        except requests.exceptions.HTTPError as http_err:
            messagebox.showerror("HTTP Error", str(http_err))
        except requests.exceptions.ConnectionError as conn_err:
            messagebox.showerror("Connection Error", str(conn_err))
        except requests.exceptions.Timeout as timeout_err:
            messagebox.showerror("Timeout Error", str(timeout_err))
        except requests.exceptions.RequestException as req_err:
            messagebox.showerror("Request Exception", str(req_err))
        except Exception as e:
# FIXME: 处理边界情况
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = WebContentGrabber(root)
    root.mainloop()

if __name__ == "__main__":
    main()
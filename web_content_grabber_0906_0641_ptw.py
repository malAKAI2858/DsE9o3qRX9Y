# 代码生成时间: 2025-09-06 06:41:19
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading
"""
A simple web content grabber tool using Python and Tkinter.
It allows users to input a URL, submit it, and view the HTML content of the webpage.
"""

class WebContentGrabber:
    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.root.title("Web Content Grabber")

        # URL entry field
        self.url_label = tk.Label(root, text="Enter URL: ")
        self.url_label.grid(row=0, column=0)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_url)
        self.submit_button.grid(row=1, column=0, columnspan=2)

        #结果显示标签
        self.result_text = tk.Text(root, height=15, width=70)
        self.result_text.grid(row=2, column=0, columnspan=2)

    def submit_url(self):
        """Handle URL submission."""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        # 使用线程避免界面冻结
        threading.Thread(target=self.fetch_content, args=(url,)).start()

    def fetch_content(self, url):
        "
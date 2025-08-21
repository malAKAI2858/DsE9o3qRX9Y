# 代码生成时间: 2025-08-21 23:05:28
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading
# 改进用户体验

"""
A simple web content grabber GUI application using Python and Tkinter framework.
It allows users to input a URL and retrieve the content of the webpage.
"""

class WebContentGrabber:
    def __init__(self, master):
        """Initialize the GUI application."""
        self.master = master
        self.master.title("Web Content Grabber")
# 扩展功能模块
        self.create_widgets()

    def create_widgets(self):
        "
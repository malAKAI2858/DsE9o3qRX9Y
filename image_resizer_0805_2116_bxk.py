# 代码生成时间: 2025-08-05 21:16:40
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

"""
# TODO: 优化性能
Image Resizer Application
This application allows users to batch resize images to a specified dimension.
"""

class ImageResizer:
    def __init__(self, master):
        """Initialize the GUI application with Tkinter."""
        self.master = master
        self.master.title("Image Resizer")
        self.create_widgets()

    def create_widgets(self):
        "
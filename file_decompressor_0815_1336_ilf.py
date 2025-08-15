# 代码生成时间: 2025-08-15 13:36:48
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import tarfile
import os

"""
A simple file decompressor tool using Python and Tkinter framework.
This tool allows users to select a compressed file and extract its contents to a specified destination.
"""

class FileDecompressor:
    def __init__(self, root):
        """Initialize the FileDecompressor class."""
        self.root = root
        self.root.title('File Decompressor')

        # Create buttons
        self.open_button = tk.Button(root, text='Open Compressed File', command=self.open_file)
        self.open_button.pack(pady=10)

        self.extract_button = tk.Button(root, text='Extract Files', command=self.extract_files, state=tk.DISABLED)
        self.extract_button.pack(pady=10)

        # Store the selected file path and destination path
        self.selected_file = None
        self.destination_path = None

    def open_file(self):
        """Open a compressed file using file dialog."""
        self.selected_file = filedialog.askopenfilename(
            filetypes=[('Zip files', '*.zip'), ('Tar files', '*.tar'), ('All files', '*.*')]
        )
        if self.selected_file:
            self.extract_button.config(state=tk.NORMAL)
        else:
            self.extract_button.config(state=tk.DISABLED)

    def extract_files(self):
        "
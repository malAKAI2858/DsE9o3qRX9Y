# 代码生成时间: 2025-10-07 22:27:47
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import gzip
import bz2
import lzma

"""
A simple compression and decompression tool using Python and Tkinter.
"""

class CompressionTool:
    def __init__(self, master):
        """Initialize the CompressionTool application.
        Args:
            master (tk.Tk): The Tkinter main window.
        """
        self.master = master
        self.master.title('Compression Tool')

        # Menu
        self.menubar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.master.quit)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        self.master.config(menu=self.menubar)

        # Buttons
        self.compress_button = tk.Button(self.master, text='Compress', command=self.compress_file)
        self.compress_button.pack(pady=10)
        self.decompress_button = tk.Button(self.master, text='Decompress', command=self.decompress_file)
        self.decompress_button.pack(pady=10)

    def open_file(self):
        """Open and read a file using a file dialog."""
        self.file_path = filedialog.askopenfilename(title='Open File', filetypes=[('All files', '*.*')])
        if self.file_path:
            try:
                with open(self.file_path, 'rb') as file:
                    self.file_content = file.read()
            except Exception as e:
                messagebox.showerror('Error', f'Failed to read file: {e}')

    def compress_file(self):
        """Compress the selected file using ZIP."""
        if not hasattr(self, 'file_content'):
            messagebox.showwarning('Warning', 'No file selected. Please open a file first.')
            return

        output_path = filedialog.asksaveasfilename(title='Save Compressed File', defaultextension='.zip', filetypes=[('ZIP file', '*.zip')])
        if output_path:
            try:
                with zipfile.ZipFile(output_path, 'w') as zip_file:
                    zip_file.writestr('compressed_file', self.file_content)
                messagebox.showinfo('Success', 'File compressed successfully.')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to compress file: {e}')

    def decompress_file(self):
        """Decompress a ZIP file."""
        self.file_path = filedialog.askopenfilename(title='Open Compressed File', filetypes=[('ZIP file', '*.zip')])
        if self.file_path:
            try:
                with zipfile.ZipFile(self.file_path, 'r') as zip_file:
                    for file in zip_file.namelist():
                        zip_file.extract(file)
                messagebox.showinfo('Success', 'File decompressed successfully.')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to decompress file: {e}')

if __name__ == '__main__':
    root = tk.Tk()
    app = CompressionTool(root)
    root.mainloop()
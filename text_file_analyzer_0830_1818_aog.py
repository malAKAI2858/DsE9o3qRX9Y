# 代码生成时间: 2025-08-30 18:18:01
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

"""
Text File Analyzer using Python and Tkinter framework.
This application allows users to open a text file and analyze its content.
"""

class TextFileAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title('Text File Analyzer')

        # Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.root.quit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Text area for displaying file content
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

    def open_file(self):
        """Open a text file and display its content in the text area."""
        file_path = filedialog.askopenfilename(title='Open File', filetypes=[('Text Files', '*.txt')])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', content)
            except Exception as e:
                messagebox.showerror('Error', f'Failed to read file: {e}')

    def run(self):
        """Run the application."""
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = TextFileAnalyzer(root)
    app.run()
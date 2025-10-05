# 代码生成时间: 2025-10-05 22:30:51
import tkinter as tk
from tkinter import filedialog, Text, Menu
# TODO: 优化性能
from tkinter.colorchooser import askcolor
import pygments
# 增强安全性
from pygments.lexers import PythonLexer, guess_lexer
# FIXME: 处理边界情况
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
import webbrowser

"""
A simple Tkinter-based code highlighter using Pygments.
# FIXME: 处理边界情况
"""

class CodeHighlighter:
    def __init__(self, root):
# TODO: 优化性能
        self.root = root
        self.text_area = Text(root)
        self.text_area.pack(expand=True, fill='both')

        # Create a menu for file operations
        self.file_menu = Menu(root)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=root.quit)
# FIXME: 处理边界情况

        # Create a menu for highlight operations
        self.highlight_menu = Menu(root)
        self.highlight_menu.add_command(label='Highlight', command=self.highlight_code)
        root.config(menu=self.file_menu)

    def open_file(self):
        """Open a file and display its contents in the text area."""
        file_path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py'), ('All Files', '*.*')])
        if file_path:
# FIXME: 处理边界情况
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete('1.0', tk.END)
# FIXME: 处理边界情况
                self.text_area.insert('1.0', content)
# TODO: 优化性能

    def save_file(self):
        """Save the contents of the text area to a file."""
        file_path = filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py'), ('All Files', '*.*')])
        if file_path:
# 添加错误处理
            with open(file_path, 'w') as file:
                content = self.text_area.get('1.0', tk.END)
                file.write(content)

    def highlight_code(self):
        """Highlight the code in the text area using Pygments."""
        content = self.text_area.get('1.0', tk.END)
        try:
            lexer = PythonLexer() if content.strip().startswith('#!/usr/bin/env python') \
                else guess_lexer(content)
            formatter = HtmlFormatter(style=get_style_by_name('colorful'))
            highlighted_code = pygments.highlight(content, lexer, formatter)
            webbrowser.open('data:text/html;charset=utf-8,' + highlighted_code)
        except Exception as e:
            print(f"Error highlighting code: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Code Highlighter')
    CodeHighlighter(root)
    root.mainloop()
# 添加错误处理
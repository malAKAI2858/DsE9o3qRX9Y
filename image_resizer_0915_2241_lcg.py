# 代码生成时间: 2025-09-15 22:41:56
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
# 添加错误处理
import os

"""
Image Resizer - A Python script to resize multiple images using Tkinter GUI.
# 优化算法效率

This script allows users to select multiple images, specify a new size, and then
resize all the selected images to the specified dimensions.
"""

class ImageResizer:
    def __init__(self, root):
        self.root = root
        self.root.title('Image Resizer')
        self.root.geometry('400x200')

        # Labels
        self.label_select = tk.Label(root, text='Select images to resize:')
        self.label_select.pack(pady=10)
        self.label_size = tk.Label(root, text='Enter new size (width x height):')
        self.label_size.pack(pady=10)

        # Entries
# 改进用户体验
        self.entry_size = tk.Entry(root)
        self.entry_size.pack(pady=10)

        # Buttons
        self.btn_select = tk.Button(root, text='Select Images', command=self.select_images)
# NOTE: 重要实现细节
        self.btn_select.pack(pady=10)
        self.btn_resize = tk.Button(root, text='Resize Images', command=self.resize_images)
        self.btn_resize.pack(pady=10)

        # Listbox to show selected files
        self.listbox_files = tk.Listbox(root)
# 扩展功能模块
        self.listbox_files.pack(pady=10)
# 改进用户体验

    def select_images(self):
# 添加错误处理
        """
        Allows the user to select multiple images.
# 改进用户体验
        """
        self.files = filedialog.askopenfilenames(title='Select Images', filetypes=[('Image Files', '*.jpg *.jpeg *.png *.bmp')])
# NOTE: 重要实现细节
        for file in self.files:
            self.listbox_files.insert(tk.END, file)

    def resize_images(self):
        """
        Resizes all the selected images to the specified size.
        """
        try:
            new_size = self.entry_size.get()
            width, height = map(int, new_size.split('x'))
# FIXME: 处理边界情况
        except ValueError:
            messagebox.showerror('Error', 'Invalid size format. Please use the format: width x height.')
            return

        if not self.files:
            messagebox.showerror('Error', 'No images selected.')
            return

        for file_path in self.files:
            try:
                with Image.open(file_path) as img:
                    img = img.resize((width, height))
                    base, ext = os.path.splitext(file_path)
                    new_file_path = f"{base}_resized{ext}"
                    img.save(new_file_path)
# 增强安全性
                    print(f'Resized and saved: {new_file_path}')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to resize {file_path}. Error: {str(e)}')
# 改进用户体验

def main():
    root = tk.Tk()
    app = ImageResizer(root)
    root.mainloop()

if __name__ == '__main__':
    main()
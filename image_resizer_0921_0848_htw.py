# 代码生成时间: 2025-09-21 08:48:41
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

"""
Image Resizer Application
This application allows users to batch resize images to a specified dimension.
"""

class ImageResizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Image Resizer')
        self.geometry('400x200')
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='Enter the new image size (width x height):')
        self.label.pack()

        self.width_entry = tk.Entry(self)
        self.width_entry.pack(side='left')

        self.height_entry = tk.Entry(self)
        self.height_entry.pack(side='left')

        self.browse_button = tk.Button(self, text='Browse Folder', command=self.browse_folder)
        self.browse_button.pack()

        self.resize_button = tk.Button(self, text='Resize Images', command=self.resize_images)
        self.resize_button.pack()

        self.status_label = tk.Label(self, text='')
        self.status_label.pack()

    def browse_folder(self):
        """
        Browse for the folder containing images.
        """
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.status_label.config(text=f'Selected folder: {self.folder_path}')

    def resize_images(self):
        """
        Resize images in the selected folder.
        """
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid integer values for width and height.')
            return

        if not self.folder_path:
            messagebox.showerror('Error', 'Please select a folder first.')
            return

        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.resize_image(os.path.join(self.folder_path, filename), width, height)

        self.status_label.config(text='Resizing completed.')

    def resize_image(self, image_path, width, height):
        """
        Resize a single image.
        """
        try:
            with Image.open(image_path) as img:
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(image_path)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to resize {os.path.basename(image_path)}: {e}')

if __name__ == '__main__':
    resizer = ImageResizer()
    resizer.mainloop()
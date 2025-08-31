# 代码生成时间: 2025-09-01 01:23:27
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
Folder Structure Organizer

This program allows users to select a directory and organizes its structure by moving files
into subdirectories based on file extensions.
"""

class FolderStructureOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Structure Organizer")
        self.root.geometry("400x200")

        # Create a button to open directory selection dialog
        self.open_button = tk.Button(self.root, text="Select Directory", command=self.open_directory)
        self.open_button.pack(pady=20)

    def open_directory(self):
        """
        Open a file dialog for the user to select a directory.
        Once a directory is selected, organize the folder structure.
        """
        directory = filedialog.askdirectory()
        if not directory:
            return
        try:
            self.organize_folder_structure(directory)
            messagebox.showinfo("Success", "Folder structure organized successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def organize_folder_structure(self, directory):
        """
        Organize the folder structure by moving files into subdirectories based on file extensions.
        """
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                extension = os.path.splitext(filename)[1].lower()
                if not extension:
                    continue
                extension_dir = os.path.join(directory, extension[1:])  # Remove the dot from the extension
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)
                os.rename(filepath, os.path.join(extension_dir, filename))

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderStructureOrganizer(root)
    root.mainloop()

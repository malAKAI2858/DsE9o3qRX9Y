# 代码生成时间: 2025-08-29 22:56:11
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
from pathlib import Path
import json

"""
A simple data backup and restore program using Python and Tkinter.
This program allows users to specify a directory to backup and restore data.
"""

class DataBackupRestoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Backup and Restore")

        # Create a menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Backup", command=self.backup)
        file_menu.add_command(label="Restore", command=self.restore)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def backup(self):
        """Backup data to a specified directory."""
        try:
            # Get source directory
            source_dir = filedialog.askdirectory(title="Select source directory")
            if source_dir:
                # Get destination directory
                dest_dir = filedialog.askdirectory(title="Select destination directory")
                if dest_dir:
                    # Copy files from source to destination
                    shutil.copytree(source_dir, dest_dir + "/backup")
                    messagebox.showinfo("Backup", "Data has been successfully backed up.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def restore(self):
        """Restore data from a specified directory."""
        try:
            # Get source directory
            source_dir = filedialog.askdirectory(title="Select source directory")
            if source_dir:
                # Get destination directory
                dest_dir = filedialog.askdirectory(title="Select destination directory")
                if dest_dir:
                    # Copy files from source to destination
                    shutil.copytree(source_dir + "/backup", dest_dir)
                    messagebox.showinfo("Restore", "Data has been successfully restored.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataBackupRestoreApp(root)
    app.run()
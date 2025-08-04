# 代码生成时间: 2025-08-05 04:04:04
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import shutil
import json

"""
A simple Python and Tkinter application for data backup and restore.
"""

# Configuration
BACKUP_DIR = "backups"
CONFIG_FILENAME = "config.json"

class DataBackupRestoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Backup and Restore")

        # Create menu
        self.create_menu()

        # Create buttons
# 扩展功能模块
        self.create_buttons()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
# 优化算法效率
        file_menu.add_command(label="Backup", command=self.backup)
        file_menu.add_command(label="Restore", command=self.restore)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

    def create_buttons(self):
        # Backup button
        btn_backup = tk.Button(self.root, text="Backup", command=self.backup)
        btn_backup.pack(side=tk.LEFT, padx=10, pady=10)

        # Restore button
        btn_restore = tk.Button(self.root, text="Restore", command=self.restore)
        btn_restore.pack(side=tk.LEFT, padx=10, pady=10)

    def backup(self):
        """Backup the current data."""
        try:
            # Get the directory to backup
            dir_path = filedialog.askdirectory()
            if not dir_path:
                return

            # Create backup directory if not exists
# FIXME: 处理边界情况
            if not os.path.exists(BACKUP_DIR):
                os.makedirs(BACKUP_DIR)

            # Get the timestamp for the backup file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(BACKUP_DIR, f"backup_{timestamp}.zip")

            # Create a zip archive of the directory
            shutil.make_archive(backup_file, 'zip', dir_path)
            messagebox.showinfo("Backup", "Backup completed successfully.")
        except Exception as e:
# 添加错误处理
            messagebox.showerror("Error", f"An error occurred: {e}")

    def restore(self):
        """Restore data from a backup."""
        try:
            # Get the backup file to restore from
# 优化算法效率
            backup_file = filedialog.askopenfilename()
            if not backup_file:
                return

            # Extract the backup file
            extract_dir = filedialog.askdirectory()
            if not extract_dir:
                return

            # Extract the zip archive
            shutil.unpack_archive(backup_file, extract_dir)
            messagebox.showinfo("Restore", "Restore completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataBackupRestoreApp(root)
    root.mainloop()
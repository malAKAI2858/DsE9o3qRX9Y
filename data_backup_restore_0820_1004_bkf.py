# 代码生成时间: 2025-08-20 10:04:28
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import json

"""
A Tkinter application for data backup and restore.
It allows users to select a directory for backup and
restore the backup to the original directory or a new one.
"""

class DataBackupRestore:
    def __init__(self, master):
        self.master = master
        self.master.title('Data Backup and Restore')

        # Frame for backup button
        backup_frame = tk.Frame(self.master)
        backup_frame.pack(pady=10)

        # Button to select directory for backup
        self.backup_button = tk.Button(backup_frame, text='Backup Data', command=self.backup_data)
        self.backup_button.pack(side=tk.LEFT, padx=5)

        # Button to select directory for restore
        self.restore_button = tk.Button(backup_frame, text='Restore Data', command=self.restore_data)
        self.restore_button.pack(side=tk.LEFT, padx=5)

        # Frame for status label
        self.status_frame = tk.Frame(self.master)
        self.status_frame.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.status_frame, text='Ready', fg='green')
        self.status_label.pack(side=tk.LEFT)

    def backup_data(self):
        """
        Backs up the selected directory to a specified backup directory.
        """
        # Select source directory
        source_dir = filedialog.askdirectory()
        if not source_dir:
            self.status_label.config(text='No source directory selected', fg='red')
            return

        # Select backup directory
        backup_dir = filedialog.askdirectory()
        if not backup_dir:
            self.status_label.config(text='No backup directory selected', fg='red')
            return

        try:
            # Create backup
            shutil.copytree(source_dir, os.path.join(backup_dir, os.path.basename(source_dir)))
            self.status_label.config(text='Backup successful', fg='green')
        except Exception as e:
            messagebox.showerror('Error', f'Error backing up data: {e}')
            self.status_label.config(text='Backup failed', fg='red')

    def restore_data(self):
        """
        Restores the backup to the original directory or a new one.
        """
        # Select backup directory
        backup_dir = filedialog.askdirectory()
        if not backup_dir:
            self.status_label.config(text='No backup directory selected', fg='red')
            return

        # Select destination directory
        destination_dir = filedialog.askdirectory()
        if not destination_dir:
            self.status_label.config(text='No destination directory selected', fg='red')
            return

        try:
            # Restore backup
            shutil.copytree(os.path.join(backup_dir, os.listdir(backup_dir)[0]), destination_dir)
            self.status_label.config(text='Restore successful', fg='green')
        except Exception as e:
            messagebox.showerror('Error', f'Error restoring data: {e}')
            self.status_label.config(text='Restore failed', fg='red')

if __name__ == '__main__':
    root = tk.Tk()
    app = DataBackupRestore(root)
    root.mainloop()
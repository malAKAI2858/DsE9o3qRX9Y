# 代码生成时间: 2025-09-24 18:46:16
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
import subprocess

"""
Database Migration Tool using Python and Tkinter

This tool provides a GUI to perform database migrations.
"""

class DatabaseMigrationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Migration Tool")
        self.create_widgets()

    def create_widgets(self):
        # Input frame
        self.input_frame = tk.LabelFrame(self.root, text="Input")
        self.input_frame.pack(padx=10, pady=10)

        # Source database path label and entry
        tk.Label(self.input_frame, text="Source Database Path: ").pack(side=tk.LEFT)
        self.source_db_path_entry = tk.Entry(self.input_frame)
        self.source_db_path_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Destination database path label and entry
        tk.Label(self.input_frame, text="Destination Database Path: ").pack(side=tk.LEFT)
        self.dest_db_path_entry = tk.Entry(self.input_frame)
        self.dest_db_path_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Migration command label and entry
        tk.Label(self.input_frame, text="Migration Command: ").pack(side=tk.LEFT)
        self.migration_cmd_entry = tk.Entry(self.input_frame)
        self.migration_cmd_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        # Browse buttons
        self.browse_src_btn = tk.Button(self.button_frame, text="Browse", command=self.browse_source_db)
        self.browse_src_btn.pack(side=tk.LEFT, padx=10)
        self.browse_dest_btn = tk.Button(self.button_frame, text="Browse", command=self.browse_dest_db)
        self.browse_dest_btn.pack(side=tk.LEFT, padx=10)

        # Migration button
        self.migrate_btn = tk.Button(self.button_frame, text="Migrate", command=self.migrate_db)
        self.migrate_btn.pack(side=tk.LEFT, padx=10)

    def browse_source_db(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.source_db_path_entry.delete(0, tk.END)
            self.source_db_path_entry.insert(0, file_path)

    def browse_dest_db(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.dest_db_path_entry.delete(0, tk.END)
            self.dest_db_path_entry.insert(0, file_path)

    def migrate_db(self):
        source_path = self.source_db_path_entry.get()
        dest_path = self.dest_db_path_entry.get()
        migration_cmd = self.migration_cmd_entry.get()

        if not source_path or not dest_path or not migration_cmd:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            # Create a command to execute the migration
            command = f"{migration_cmd} {source_path} {dest_path}"

            # Run the command using subprocess
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

            # Show the result of the migration
            messagebox.showinfo("Success", "Migration completed successfully")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Migration failed: {e.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = DatabaseMigrationTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
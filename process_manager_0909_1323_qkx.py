# 代码生成时间: 2025-09-09 13:23:08
import tkinter as tk
from tkinter import messagebox
import subprocess
import psutil
import os

"""
Process Manager Application using Python and Tkinter Framework

This application allows users to view and manage system processes.

Features:
- Display list of running processes
- Kill selected processes
"""

class ProcessManager:
    def __init__(self, root):
        self.root = root
        self.root.title('Process Manager')
        self.root.geometry('600x400')
        self.processes = []
        self.load_processes()

    def load_processes(self):
        """Load running system processes"""
        try:
            self.processes = psutil.process_iter(['pid', 'name', 'status'])
            self.populate_process_list()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to load processes: {e}')

    def populate_process_list(self):
        """Populate the process list in the GUI"""
        self.process_list.delete(0, tk.END)  # Clear existing list
        for proc in self.processes:
            self.process_list.insert(tk.END, f'{proc.info[
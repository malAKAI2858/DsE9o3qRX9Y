# 代码生成时间: 2025-09-14 13:47:44
import tkinter as tk
from tkinter import ttk
import os
import psutil
import threading

"""
System Performance Monitor using Python and Tkinter.
This program provides a simple GUI to monitor system performance including CPU, Memory, and Disk usage.
"""

class SystemPerformanceMonitor:
    def __init__(self, master):
        """Initialize the GUI."""
        self.master = master
        self.master.title('System Performance Monitor')
        self.master.geometry('600x400')

        # Create frames for each monitor type
        self.cpu_frame = ttk.LabelFrame(self.master, text='CPU Usage')
        self.cpu_frame.grid(row=0, column=0, padx=10, pady=10)

        self.mem_frame = ttk.LabelFrame(self.master, text='Memory Usage')
        self.mem_frame.grid(row=0, column=1, padx=10, pady=10)

        self.disk_frame = ttk.LabelFrame(self.master, text='Disk Usage')
        self.disk_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # CPU Usage
        self.cpu_label = ttk.Label(self.cpu_frame, text='CPU Usage: 0%')
        self.cpu_label.pack(pady=10)

        # Memory Usage
        self.mem_label = ttk.Label(self.mem_frame, text='Memory Usage: 0%')
        self.mem_label.pack(pady=10)

        # Disk Usage
        self.disk_label = ttk.Label(self.disk_frame, text='Disk Usage: 0%')
        self.disk_label.pack(pady=10)

        # Start monitoring thread
        self.monitoring_thread = threading.Thread(target=self.monitor_system)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()

    def monitor_system(self):
        """Monitor system performance and update GUI."""
        while True:
            # Get CPU usage
            cpu_usage = psutil.cpu_percent()
            self.update_label(self.cpu_label, f'CPU Usage: {cpu_usage}%')

            # Get memory usage
            memory = psutil.virtual_memory()
            mem_usage = memory.percent
            self.update_label(self.mem_label, f'Memory Usage: {mem_usage}%')

            # Get disk usage
            disk_usage = psutil.disk_usage('/')
            self.update_label(self.disk_label, f'Disk Usage: {disk_usage.percent}%')

            # Update every second
            self.master.after(1000, self.monitor_system)

    def update_label(self, label, text):
        """Update the text of a label."""
        label['text'] = text

    def run(self):
        "
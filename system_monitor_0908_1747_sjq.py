# 代码生成时间: 2025-09-08 17:47:07
import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

"""
This is a simple system performance monitoring tool using Python and Tkinter framework.
It displays CPU usage, memory usage, and disk usage in real-time.
"""

class SystemMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("System Performance Monitor")
        self.cpu_label = ttk.Label(root, text="CPU Usage: 0%")
        self.cpu_label.pack(pady=10)
        self.ram_label = ttk.Label(root, text="Memory Usage: 0%")
        self.ram_label.pack(pady=10)
        self.disk_label = ttk.Label(root, text="Disk Usage: 0%\)
        self.disk_label.pack(pady=10)

        # Start the monitoring thread
        self.monitoring_thread = threading.Thread(target=self.monitor_system)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()

    def monitor_system(self):
        """
        This function monitors the system performance in real-time.
        It updates the CPU, memory, and disk usage labels.
        """
        while True:
            try:
                # Get CPU usage
                cpu_usage = psutil.cpu_percent(interval=1)
                self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")

                # Get memory usage
                memory = psutil.virtual_memory()
                memory_usage = memory.percent
                self.ram_label.config(text=f"Memory Usage: {memory_usage}%")

                # Get disk usage
                disk_usage = psutil.disk_usage('/')
                disk_usage_percent = disk_usage.percent
                self.disk_label.config(text=f"Disk Usage: {disk_usage_percent}%")

                # Sleep for 1 second before updating again
                time.sleep(1)
            except Exception as e:
                # Handle any exceptions that occur during monitoring
                print(f"Error monitoring system: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    monitor = SystemMonitor(root)
    monitor.run()
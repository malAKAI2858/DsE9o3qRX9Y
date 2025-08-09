# 代码生成时间: 2025-08-10 04:32:07
import tkinter as tk
from tkinter import ttk
import psutil
import os

"""
Memory Usage Analyzer using Python and Tkinter.
This program analyzes the memory usage of the system and displays it in a graphical user interface.
"""

class MemoryUsageAnalyzer:
    def __init__(self, root):
        """Initialize the MemoryUsageAnalyzer class."""
        self.root = root
        self.root.title("Memory Usage Analyzer")
        self.root.geometry("400x300")

        # Create a frame for the chart
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        # Create a canvas for the chart
        self.canvas = tk.Canvas(self.frame, width=380, height=250)
        self.canvas.pack()

        # Draw the chart
        self.draw_chart()

    def draw_chart(self):
        """Draw the memory usage chart."""
        try:
            # Get the memory usage data
            total_memory = psutil.virtual_memory().total
            used_memory = psutil.virtual_memory().used
            free_memory = psutil.virtual_memory().free
            memory_usage = used_memory / total_memory * 100

            # Draw the chart
            self.canvas.create_rectangle(10, 130, 370, 250, fill="light gray")
            self.canvas.create_rectangle(10, 250 - int(memory_usage / 100 * 120), 370, 250, fill="dark gray")

            # Add labels
            self.canvas.create_text(190, 10, text=f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
            self.canvas.create_text(190, 30, text=f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
            self.canvas.create_text(190, 50, text=f"Free Memory: {free_memory / (1024 ** 3):.2f} GB")
            self.canvas.create_text(190, 70, text=f"Memory Usage: {memory_usage:.2f}%")

        except Exception as e:
            print(f"Error: {e}")
            self.canvas.create_text(190, 100, text=f"Error: {e}")

    def run(self):
        """Start the GUI loop."""
        self.root.mainloop()

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the MemoryUsageAnalyzer class
    analyzer = MemoryUsageAnalyzer(root)

    # Start the GUI loop
    analyzer.run()
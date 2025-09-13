# 代码生成时间: 2025-09-14 00:32:10
import tkinter as tk
from tkinter import filedialog, messagebox
import os

"""
Test Report Generator using Python and Tkinter.
This script allows the user to select a directory and generates a test report.
"""

class TestReportGenerator:
    def __init__(self, master):
        """Initialize the GUI application."""
        self.master = master
        master.title('Test Report Generator')
        master.geometry('400x300')

        # Create a frame for buttons
        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        # Create a button to select the directory
        self.select_dir_button = tk.Button(self.frame, text='Select Directory', command=self.select_directory)
        self.select_dir_button.pack(side=tk.LEFT, padx=5)

        # Create a button to generate the report
        self.generate_report_button = tk.Button(self.frame, text='Generate Report', command=self.generate_report, state=tk.DISABLED)
        self.generate_report_button.pack(side=tk.LEFT, padx=5)

        # Create a label to display the selected directory
        self.dir_label = tk.Label(master, text='')
        self.dir_label.pack()

    def select_directory(self):
        "
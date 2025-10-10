# 代码生成时间: 2025-10-10 21:14:00
import tkinter as tk
from tkinter import messagebox
import random
import subprocess
import sys

"""
A simple Chaos Engineering tool implemented using Python and Tkinter.
This program simulates chaos by randomly killing system processes.
"""

class ChaosEngineeringTool:
    def __init__(self, master):
        """Initialize the GUI components."""
        self.master = master
        master.title("Chaos Engineering Tool")

        # Create a label
        self.label = tk.Label(master, text="Chaos Engineering Tool")
        self.label.pack()

        # Create a button to start the chaos
        self.start_button = tk.Button(master, text="Start Chaos", command=self.start_chaos)
        self.start_button.pack()

    def start_chaos(self):
        """Simulate chaos by randomly killing system processes."""
        try:
            # Get a list of system processes
            processes = subprocess.check_output(["ps", "aux"]).decode().splitlines()

            # Randomly select a process to kill
            process = random.choice(processes)
            process_id = process.split()[1]

            # Kill the process
            subprocess.run(["kill", process_id])
            messagebox.showinfo("Chaos Started", f"Killed process with ID: {process_id}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window and pass it to the ChaosEngineeringTool class
root = tk.Tk()
app = ChaosEngineeringTool(root)

# Start the GUI event loop
root.mainloop()
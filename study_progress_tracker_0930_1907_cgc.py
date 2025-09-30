# 代码生成时间: 2025-09-30 19:07:56
import tkinter as tk
from tkinter import messagebox

"""
Study Progress Tracker
====================
A simple Python program using Tkinter to track study progress.
"""

class StudyProgressTracker:
    def __init__(self, master):
        """Initialize the Study Progress Tracker application."""
        self.master = master
        self.master.title("Study Progress Tracker")

        # Create a label for instructions
        self.instructions_label = tk.Label(master, text="Enter the total study hours and completed hours:",
                                      font=("Helvetica", 12))
        self.instructions_label.pack(pady=10)

        # Create entry widgets for total hours and completed hours
        self.total_hours_label = tk.Label(master, text="Total Hours:",
                                       font=("Helvetica\, 10))
        self.total_hours_label.pack()
        self.total_hours_entry = tk.Entry(master, width=10)
        self.total_hours_entry.pack()

        self.completed_hours_label = tk.Label(master, text="Completed Hours:",
                                          font=("Helvetica\, 10))
        self.completed_hours_label.pack()
        self.completed_hours_entry = tk.Entry(master, width=10)
        self.completed_hours_entry.pack()

        # Create a button to calculate the remaining hours
        self.calculate_button = tk.Button(master, text="Calculate Remaining Hours",
                                          command=self.calculate_remaining)
        self.calculate_button.pack(pady=10)

        # Create a label to display the remaining hours
        self.remaining_hours_label = tk.Label(master, text="", font=("Helvetica\, 12))
        self.remaining_hours_label.pack(pady=10)

    def calculate_remaining(self):
        """Calculate and display the remaining study hours."""
        try:
            total_hours = float(self.total_hours_entry.get())
            completed_hours = float(self.completed_hours_entry.get())

            if total_hours < completed_hours:
                messagebox.showerror("Error", "Completed hours cannot be more than total hours.")
                return

            remaining_hours = total_hours - completed_hours
            self.remaining_hours_label.config(text=f"Remaining Hours: {remaining_hours:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for hours.")

def main():
    """Run the Study Progress Tracker application."""
    root = tk.Tk()
    app = StudyProgressTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
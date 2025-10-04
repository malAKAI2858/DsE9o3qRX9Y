# 代码生成时间: 2025-10-04 19:05:50
import tkinter as tk
from tkinter import messagebox

"""
Health Monitor Application

This application is designed to simulate a health monitoring device using the Tkinter framework.
It allows the user to input health data and displays the results.
"""

class HealthMonitorApp:
    def __init__(self, master):
        """Initialize the Health Monitor Application."""
        self.master = master
        self.master.title("Health Monitor Device")

        # Create the main frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        # Create labels and entry widgets for heart rate and blood pressure
        self.heart_rate_label = tk.Label(self.main_frame, text="Heart Rate (bpm): ")
        self.heart_rate_label.grid(row=0, column=0)
        self.heart_rate_entry = tk.Entry(self.main_frame)
        self.heart_rate_entry.grid(row=0, column=1)

        self.blood_pressure_label = tk.Label(self.main_frame, text="Blood Pressure (mmHg): ")
        self.blood_pressure_label.grid(row=1, column=0)
        self.blood_pressure_entry = tk.Entry(self.main_frame)
        self.blood_pressure_entry.grid(row=1, column=1)

        # Create a button to submit the data
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def submit_data(self):
        """Handle the submission of health data."""
        try:
            # Retrieve the heart rate and blood pressure values from the user inputs
            heart_rate = int(self.heart_rate_entry.get())
            blood_pressure = float(self.blood_pressure_entry.get())

            # Validate the data
            if heart_rate < 30 or heart_rate > 200:
                messagebox.showerror("Error", "Invalid heart rate value.")
                return
            if blood_pressure < 50 or blood_pressure > 200:
                messagebox.showerror("Error", "Invalid blood pressure value.")
                return

            # Display the submitted data
            messagebox.showinfo("Submitted Data", f"Heart Rate: {heart_rate} bpm, Blood Pressure: {blood_pressure} mmHg")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for heart rate and blood pressure.")

# Create the main window and run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = HealthMonitorApp(root)
    root.mainloop()
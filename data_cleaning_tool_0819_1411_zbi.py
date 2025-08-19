# 代码生成时间: 2025-08-19 14:11:51
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

"""
A simple GUI tool for data cleaning and preprocessing using Python and Tkinter.
"""

class DataCleaningTool:
    def __init__(self, root):
        self.root = root
        root.title('Data Cleaning Tool')

        # Create menus
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # File operations menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save Cleaned Data", command=self.save_cleaned_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Widgets
        self.status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.file_path = ""

    def open_file(self):
        """Open a file dialog to select a CSV file."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.read_file(file_path)

    def read_file(self, file_path):
        """Read the selected CSV file into a DataFrame."""
        try:
            self.data = pd.read_csv(file_path)
            self.status_label.config(text="File loaded: " + os.path.basename(file_path))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the file: {e}")

    def save_cleaned_data(self):
        """Save the cleaned data to a new CSV file."""
        if not hasattr(self, "data"):
            messagebox.showinfo("Info", "No data to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.data.to_csv(file_path, index=False)
                self.status_label.config(text="Data saved: " + os.path.basename(file_path))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save the file: {e}")

    def run(self):
        """Run the Tkinter event loop."""
        self.root.mainloop()

# Create the main window and pass it to the DataCleaningTool class
if __name__ == "__main__":
    root = tk.Tk()
    app = DataCleaningTool(root)
    app.run()
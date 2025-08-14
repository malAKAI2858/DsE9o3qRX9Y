# 代码生成时间: 2025-08-15 01:27:09
import tkinter as tk
from tkinter import messagebox
import random
import string

"""
Test Data Generator

This program generates random test data using Python and Tkinter framework.
It provides a simple GUI to specify the type of data to generate and
displays the generated data in a label.
"""

class TestDataGenerator:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title('Test Data Generator')

        # Create a frame for the data type selection
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # Create a label for the data type selection
        self.label = tk.Label(self.frame, text='Select Data Type:', font=('Arial', 12))
        self.label.pack(pady=10)

        # Create a dropdown menu for data type selection
        self.data_type = tk.StringVar(self.root)
        self.data_type.set('Select Data Type')  # default value
        self.data_type_options = ['Select Data Type', 'Random String', 'Random Integer', 'Random Float']
        self.dropdown = tk.OptionMenu(self.frame, self.data_type, *self.data_type_options)
        self.dropdown.pack(pady=10)

        # Create a button to generate data
        self.generate_button = tk.Button(self.frame, text='Generate', command=self.generate_data)
        self.generate_button.pack(pady=10)

        # Create a label to display generated data
        self.result_label = tk.Label(self.root, text='', font=('Arial', 12))
        self.result_label.pack(pady=20)

    def generate_data(self):
        # Get the selected data type
        data_type = self.data_type.get()

        # Handle different data types
        if data_type == 'Random String':
            self.result_label.config(text=self.generate_random_string())
        elif data_type == 'Random Integer':
            self.result_label.config(text=str(self.generate_random_integer()))
        elif data_type == 'Random Float':
            self.result_label.config(text=str(self.generate_random_float()))
        else:
            # Show error message if invalid data type is selected
            messagebox.showerror('Error', 'Please select a valid data type')

    def generate_random_string(self):
        # Generate a random string of 10 characters
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

    def generate_random_integer(self):
        # Generate a random integer between 1 and 100
        return random.randint(1, 100)

    def generate_random_float(self):
        # Generate a random float between 0.0 and 100.0
        return round(random.uniform(0.0, 100.0), 2)

# Create the main window
root = tk.Tk()

# Create an instance of TestDataGenerator and pass the main window
test_data_generator = TestDataGenerator(root)

# Start the event loop
root.mainloop()
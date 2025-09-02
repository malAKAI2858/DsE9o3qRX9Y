# 代码生成时间: 2025-09-02 17:14:23
import tkinter as tk
from tkinter import messagebox
import random

"""
A simple GUI application using Python and Tkinter to generate random numbers.
This program allows the user to specify the range and count of random numbers.
It demonstrates basic Tkinter usage, error handling, and user input validation.
"""

class RandomNumberGenerator:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title('Random Number Generator')
        self.root.geometry('300x200')

        # Create input fields
        self.lower_label = tk.Label(root, text='Lower Bound:')
        self.lower_label.grid(row=0, column=0)
        self.lower_entry = tk.Entry(root)
        self.lower_entry.grid(row=0, column=1)

        self.upper_label = tk.Label(root, text='Upper Bound:')
        self.upper_label.grid(row=1, column=0)
        self.upper_entry = tk.Entry(root)
        self.upper_entry.grid(row=1, column=1)

        self.count_label = tk.Label(root, text='Count:')
        self.count_label.grid(row=2, column=0)
        self.count_entry = tk.Entry(root)
        self.count_entry.grid(row=2, column=1)

        # Create generate button
        self.generate_button = tk.Button(root, text='Generate', command=self.generate_numbers)
        self.generate_button.grid(row=3, column=0, columnspan=2)

    def generate_numbers(self):
        try:
            lower_bound = int(self.lower_entry.get())
            upper_bound = int(self.upper_entry.get())
            count = int(self.count_entry.get())

            # Error handling
            if lower_bound >= upper_bound:
                messagebox.showerror('Error', 'Lower bound must be less than upper bound.')
                return
            if count <= 0:
                messagebox.showerror('Error', 'Count must be a positive integer.')
                return

            random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(count)]
            messagebox.showinfo('Random Numbers', '
'.join(map(str, random_numbers)))
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid integers for bounds and count.')

def main():
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
# 代码生成时间: 2025-08-30 07:01:36
import tkinter as tk
from tkinter import messagebox

"""
A simple Tkinter-based form validator application.
This script creates a window with form input fields and
validates the input data before closing the window.
"""

class FormValidator:
    def __init__(self, master):
        """Initialize the FormValidator instance."""
        self.master = master
        self.master.title("Form Validator")

        # Define input fields
        self.name = tk.StringVar()
        self.email = tk.StringVar()

        # Create labels and entry widgets
        tk.Label(master, text="Name: ").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.name).grid(row=0, column=1)
        tk.Label(master, text="Email: ").grid(row=1, column=0)
        tk.Entry(master, textvariable=self.email).grid(row=1, column=1)

        # Create a submit button
        submit_button = tk.Button(master, text="Submit", command=self.validate_form)
        submit_button.grid(row=2, column=0, columnspan=2)

    def validate_form(self):
        """Validate the form input and show an error message if validation fails."""
        try:
            # Validate name
            if not self.name.get().strip():
                raise ValueError("Name is required.")

            # Validate email
            if not self.email.get().strip() or "@" not in self.email.get():
                raise ValueError("Invalid email address.")

            # If no errors, close the window
            self.master.destroy()
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = FormValidator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
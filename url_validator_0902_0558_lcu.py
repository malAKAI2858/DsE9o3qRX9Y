# 代码生成时间: 2025-09-02 05:58:49
import tkinter as tk
from tkinter import messagebox
import requests

"""
A GUI application to validate the validity of a URL using Tkinter and requests library.

Features:
- Validate URL links
- Error handling"""

class URLValidator:
    def __init__(self, master):
        """Initialize the main window and components."""
        self.master = master
        self.master.title("URL Validator")

        # Label for input URL
        self.label = tk.Label(self.master, text="Enter URL: ")
        self.label.pack(pady=(10, 0))

        # Entry widget to input URL
        self.url_entry = tk.Entry(self.master, width=40)
        self.url_entry.pack(pady=5)

        # Button to validate URL
        self.validate_button = tk.Button(self.master, text="Validate URL", command=self.validate_url)
        self.validate_button.pack(pady=5)

    def validate_url(self):
        """Validate the URL entered in the entry widget."""
        url = self.url_entry.get()

        # Check if the URL is empty
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        try:
            # Use requests.head to check the URL without downloading the content
            response = requests.head(url)
            # Check if the HTTP status code is 200 OK
            if response.status_code == 200:
                messagebox.showinfo("Success", "The URL is valid.")
            else:
                messagebox.showerror("Error", "The URL is not valid.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = URLValidator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
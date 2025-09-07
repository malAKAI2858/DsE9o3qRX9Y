# 代码生成时间: 2025-09-07 22:50:56
import tkinter as tk
from tkinter import messagebox
import requests
from urllib.parse import urlparse

"""
URL Validator application using Python and Tkinter framework.
This program allows users to input a URL and checks if it is valid and reachable.
"""

class URLValidator:
    def __init__(self, master):
        """Initialize the application window."""
        self.master = master
        self.master.title("URL Validator")
        self.master.geometry("300x200")

        # Label for the input field
        self.label = tk.Label(master, text="Enter URL: ")
        self.label.pack(pady=10)

        # Text entry field for user input
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Check button to validate URL
        self.check_button = tk.Button(master, text="Check URL", command=self.validate_url)
        self.check_button.pack(pady=20)

    def validate_url(self):
        """Validate the URL entered by the user."""
        url = self.entry.get()
        try:
            # Parse the URL to check its format
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                # Check if the URL is reachable
                response = requests.get(url)
                if response.status_code == 200:
                    messagebox.showinfo("URL Validity", "The URL is valid and reachable.")
                else:
                    messagebox.showerror("URL Validity", "The URL is not reachable.")
            else:
                messagebox.showerror("URL Validity", "The URL format is invalid.")
        except requests.RequestException as e:
            messagebox.showerror("URL Validity", f"An error occurred: {e}")
        except Exception as e:
            messagebox.showerror("URL Validity", f"An unexpected error occurred: {e}")

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = URLValidator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
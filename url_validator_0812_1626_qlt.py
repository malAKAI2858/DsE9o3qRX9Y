# 代码生成时间: 2025-08-12 16:26:08
import tkinter as tk
from tkinter import messagebox
import requests
from urllib.parse import urlparse

"""
URL Validator App

This application uses the tkinter framework to create a GUI that allows users to input a URL
and validate its effectiveness.
"""

class URLValidator:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("URL Validator")

        # Input field for URL
        self.url_label = tk.Label(master, text="Enter URL: ")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to validate the URL
        self.validate_button = tk.Button(master, text="Validate", command=self.validate_url)
        self.validate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def validate_url(self):
        """Validate the URL entered by the user."""
        url = self.url_entry.get()
        try:
            # Parse the URL to check its format
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                # Make a request to the URL to check its effectiveness
                response = requests.head(url, allow_redirects=True, timeout=5)
                if response.status_code == 200:
                    messagebox.showinfo("Validation Result", "The URL is valid and accessible.")
                else:
                    messagebox.showerror("Validation Result", 
                                      "The URL is valid but returned status code: {}".format(response.status_code))
            else:
                messagebox.showerror("Validation Error", "Please enter a valid URL with scheme and netloc.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", "Failed to reach the URL. Error: {}".format(str(e)))
        except ValueError:
            messagebox.showerror("Validation Error", "The URL entered is not valid.")

def main():
    # Create the main window and pass it to the URLValidator class
    root = tk.Tk()
    app = URLValidator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
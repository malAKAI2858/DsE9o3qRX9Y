# 代码生成时间: 2025-08-11 16:23:10
import tkinter as tk
from tkinter import messagebox
import requests
from urllib.parse import urlparse

"""
URL Validator using Python and Tkinter framework.
This program allows users to input a URL and validates its validity.
"""

class UrlValidator:
    def __init__(self, root):
        """Initialize the Tkinter application."""
        self.root = root
        self.root.title('URL Validator')
        self.root.geometry('300x150')

        # URL label and entry
        self.url_label = tk.Label(self.root, text='Enter URL: ')
        self.url_label.pack()
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack()

        # Validate button
        self.validate_button = tk.Button(self.root, text='Validate', command=self.validate_url)
        self.validate_button.pack()

    def validate_url(self):
        """Validate the entered URL."""
        url = self.url_entry.get()
        try:
            # Check if the URL is valid
            result = self.is_valid_url(url)
            if result:
                messagebox.showinfo('Validation Result', 'The URL is valid.')
            else:
                messagebox.showerror('Validation Result', 'The URL is invalid.')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')

    def is_valid_url(self, url):
        """Check if the URL is valid using urlparse."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def check_url_status_code(self, url):
        """Check the HTTP status code of the URL."""
        try:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

if __name__ == '__main__':
    root = tk.Tk()
    app = UrlValidator(root)
    root.mainloop()
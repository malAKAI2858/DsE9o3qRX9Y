# 代码生成时间: 2025-08-20 03:33:52
import tkinter as tk
from tkinter import messagebox
import requests
import threading

"""
A simple HTTP request handler GUI application using Python and Tkinter.
This application allows users to enter a URL and send an HTTP GET request.
The response is then displayed in a messagebox.
"""

class HttpRequestHandler:
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        root.title("HTTP Request Handler")

        # Create a label and entry widget for the URL
        url_label = tk.Label(root, text="URL:")
        url_label.pack()
        self.url_entry = tk.Entry(root)
        self.url_entry.pack()

        # Create a button to send the HTTP GET request
        send_button = tk.Button(root, text="Send Request", command=self.send_request)
        send_button.pack()

    def send_request(self):
        """Send an HTTP GET request to the provided URL and display the response."""
        url = self.url_entry.get()

        # Check if the URL is empty
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        # Create a new thread to send the request to avoid blocking the GUI
        thread = threading.Thread(target=self.send_request_thread, args=(url,))
        thread.start()

    def send_request_thread(self, url):
        """Send an HTTP GET request to the provided URL in a separate thread."""
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.RequestException as e:
            # Handle any request-related errors
            error_message = f"Error: {e}"
        else:
            # Display the response in a messagebox
            error_message = response.text
        finally:
            messagebox.showinfo("Response", error_message)

def main():
    """Create and run the GUI application."""
    root = tk.Tk()
    app = HttpRequestHandler(root)
    root.mainloop()

if __name__ == "__main__":
    main()
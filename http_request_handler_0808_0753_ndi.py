# 代码生成时间: 2025-08-08 07:53:16
import tkinter as tk
from tkinter import messagebox
import requests

"""
HTTP Request Handler GUI Application

This application allows users to send HTTP requests (GET, POST, PUT, DELETE) to a specified URL.
It displays the response from the server.
"""

class HttpRequestHandler:
    """Class to handle HTTP requests and update the GUI."""
    def __init__(self, master):
        self.master = master
        self.master.title('HTTP Request Handler')
        self.master.geometry('400x300')

        # URL Entry
        self.url_label = tk.Label(master, text='URL:')
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack(pady=5)

        # Method Selection
        self.method_label = tk.Label(master, text='Method:')
        self.method_label.pack(pady=5)
        self.method_var = tk.StringVar(master)
        self.method_var.set('GET')  # default value
        self.method_options = ['GET', 'POST', 'PUT', 'DELETE']
        self.method_menu = tk.OptionMenu(master, self.method_var, *self.method_options)
        self.method_menu.pack(pady=5)

        # Headers Entry
        self.headers_label = tk.Label(master, text='Headers (format: key:value):')
        self.headers_label.pack(pady=5)
        self.headers_entry = tk.Entry(master, width=50)
        self.headers_entry.pack(pady=5)

        # Send Request Button
        self.send_button = tk.Button(master, text='Send', command=self.send_request)
        self.send_button.pack(pady=10)

        # Response Label
        self.response_label = tk.Label(master, text='Response:', wraplength=380)
        self.response_label.pack(pady=5)
        self.response_text = tk.Text(master, height=10, width=50)
        self.response_text.pack(pady=5)

    def send_request(self):
        """Send an HTTP request to the specified URL and update the GUI with the response."""
        try:
            url = self.url_entry.get()
            method = self.method_var.get()
            headers = self.headers_entry.get().split(',')
            headers_dict = {}
            for header in headers:
                key, value = header.split(':')
                headers_dict[key.strip()] = value.strip()

            response = requests.request(method, url, headers=headers_dict)
            response_text = f'Status Code: {response.status_code}
Response Body:
{response.text}'
            self.response_text.delete('1.0', tk.END)
            self.response_text.insert(tk.END, response_text)
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
        except Exception as e:
            messagebox.showerror('Error', f'An unexpected error occurred: {e}')

# Create and run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = HttpRequestHandler(root)
    root.mainloop()
# 代码生成时间: 2025-09-07 08:20:51
import tkinter as tk
from tkinter import messagebox
import requests

"""
HTTP Request Handler GUI Application
This application uses tkinter for the graphical user interface and requests to handle HTTP requests.
"""

class HttpRequestHandler:
    def __init__(self, master):
        self.master = master
        master.title("HTTP Request Handler")

        # URL label and entry
        tk.Label(master, text="URL:").grid(row=0, column=0)
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1)

        # Method label and option menu
        tk.Label(master, text="Method:").grid(row=1, column=0)
        self.method_var = tk.StringVar()
        self.method_var.set("GET")  # default method
        self.method_menu = tk.OptionMenu(master, self.method_var, "GET", "POST", "PUT\, "DELETE")
        self.method_menu.grid(row=1, column=1)

        # Headers label and entry
        tk.Label(master, text="Headers (JSON):
        self.headers_entry = tk.Entry(master, width=50)
        self.headers_entry.grid(row=2, column=1)

        # Body label and text area
        tk.Label(master, text="Body (optional):
        self.body_text = tk.Text(master, height=10, width=50)
        self.body_text.grid(row=3, column=1)

        # Send button
        self.send_button = tk.Button(master, text="Send", command=self.send_request)
        self.send_button.grid(row=4, column=0, columnspan=2)

        # Response label and text area
        self.response_label = tk.Label(master, text="Response:")
        self.response_label.grid(row=5, column=0)
        self.response_text = tk.Text(master, height=10, width=50)
        self.response_text.grid(row=5, column=1)

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()
        headers = self.headers_entry.get()
        body = self.body_text.get("1.0", tk.END)

        try:
            # Parse headers from JSON string
            headers = self.parse_json(headers)
        except ValueError:
            messagebox.showerror("Error", "Invalid JSON for headers")
            return

        # Send HTTP request
        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, data=body)
            elif method == "PUT":
                response = requests.put(url, headers=headers, data=body)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                messagebox.showerror("Error", "Unsupported method")
                return

            # Display response
            self.response_text.delete("1.0", tk.END)
            self.response_text.insert(tk.END, response.text)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))

    def parse_json(self, json_str):
        """Parse a JSON string into a Python dictionary."""
        try:
            import json
            return json.loads(json_str)
        except ValueError:
            raise ValueError("Invalid JSON string")



def main():
    root = tk.Tk()
    app = HttpRequestHandler(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# 代码生成时间: 2025-08-09 15:49:40
import tkinter as tk
from tkinter import messagebox
import json

"""
API Response Formatter Tool
This tool allows users to format API responses into a more readable JSON format.
"""

class ApiResponseFormatter:
    def __init__(self, window):
        """Initialize the GUI components."""
        self.window = window
        self.window.title("API Response Formatter Tool")
        self.window.geometry("600x400")

        # Text area for input API response
        self.input_text = tk.Text(window, height=15, width=80)
        self.input_text.pack(pady=10)

        # Button to format the API response
        self.format_button = tk.Button(window, text="Format Response", command=self.format_response)
        self.format_button.pack(pady=10)

        # Text area for formatted output
        self.output_text = tk.Text(window, height=15, width=80)
        self.output_text.pack(pady=10)

    def format_response(self):
        """Format the input API response into a readable JSON format."""
        try:
            # Get the input text from the text area
            input_text = self.input_text.get("1.0", tk.END)

            # Attempt to parse the input text as JSON
            try:
                data = json.loads(input_text)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON format. Please check the input.")
                return

            # Format the JSON data into a pretty-printed string
            formatted_json = json.dumps(data, indent=4)

            # Insert the formatted JSON into the output text area
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, formatted_json)
        except Exception as e:
            # Handle any unexpected errors
            messagebox.showerror("Error", str(e))


def main():
    """Create the main application window and run the event loop."""
    root = tk.Tk()
    app = ApiResponseFormatter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# 代码生成时间: 2025-09-17 08:59:42
import tkinter as tk
from tkinter import messagebox
import re

"""
This is a simple GUI application using Python and Tkinter that demonstrates
XSS (Cross-Site Scripting) protection by sanitizing user input.
"""

class XSSProtectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("XSS Protection GUI")
        
        # Label for input
        self.label = tk.Label(master, text="Enter text to sanitize: ")
        self.label.pack()
        
        # Text input for user
        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.pack()
        
        # Button to sanitize input
        self.sanitize_button = tk.Button(master, text="Sanitize Input", command=self.sanitize_input)
        self.sanitize_button.pack()
        
        # Label to display sanitized text
        self.sanitized_label = tk.Label(master, text="")
        self.sanitized_label.pack()
        
    def sanitize_input(self):
        """
        This function sanitizes the input to prevent XSS attacks.
        It uses regular expressions to remove potentially harmful scripts.
        """
        try:
            # Get user input
            user_input = self.input_text.get("1.0", tk.END)
            
            # Sanitize input by removing tags and script content
            sanitized_input = re.sub(r'<script>.*?</script>', '', user_input, flags=re.DOTALL)
            sanitized_input = re.sub(r'<.*?>', '', sanitized_input)
            
            # Display sanitized text
            self.sanitized_label.config(text=sanitized_input)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window and pass it to the application
root = tk.Tk()
app = XSSProtectionApp(root)

# Start the GUI event loop
root.mainloop()
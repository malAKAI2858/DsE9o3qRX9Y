# 代码生成时间: 2025-09-13 02:23:33
import tkinter as tk
from tkinter import messagebox

"""
Access Control Application using Tkinter Framework.
This application allows users to login with a predefined username and password.
"""

# Predefined username and password for demonstration purposes
PREDEFINED_USERNAME = 'admin'
PREDEFINED_PASSWORD = 'password123'

class AccessControlApp:
    def __init__(self, root):
        """Initialize the application and set up the GUI."""
        self.root = root
        self.root.title('Access Control App')

        # Create login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        # Create username label and entry
        tk.Label(self.login_frame, text='Username:').grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        # Create password label and entry
        tk.Label(self.login_frame, text='Password:').grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        # Create login button
        tk.Button(self.login_frame, text='Login', command=self.login).grid(row=2, column=0, columnspan=2)

    def login(self):
        """Handle the login logic."""
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()

            # Check if credentials match the predefined ones
            if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
                messagebox.showinfo('Success', 'Login successful!')
                # Redirect to the main application window or perform further actions
            else:
                messagebox.showerror('Error', 'Invalid username or password')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')

def main():
    """Main function to start the application."""
    root = tk.Tk()
    app = AccessControlApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

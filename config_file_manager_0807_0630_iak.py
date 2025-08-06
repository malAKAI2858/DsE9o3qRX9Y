# 代码生成时间: 2025-08-07 06:30:33
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

"""
Config File Manager is a simple graphical application that allows users to manage configuration files.
It provides an interface to open, edit, and save configuration files.
"""


class ConfigFileManager:
    def __init__(self, root):
        self.root = root
        self.root.title('Config File Manager')
        self.create_widgets()

    def create_widgets(self):
        # File Menu
        self.file_menu = tk.Menu(self.root)
        self.root.config(menu=self.file_menu)
        
        # Open File Option
        open_file_item = tk.Menu(self.file_menu, tearoff=0)
        open_file_item.add_command(label='Open', command=self.open_file)
        self.file_menu.add_cascade(label='File', menu=open_file_item)
        
        # Text Widget for displaying the file
        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(expand=True, fill='both')

    def open_file(self):
        """Opens a configuration file for editing."""
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_widget.delete('1.0', tk.END)  # Clear the text widget
                    self.text_widget.insert('1.0', file.read())  # Insert the file content
            except Exception as e:
                messagebox.showerror('Error', f'Failed to open file: {e}')

    def save_file(self):
        """Saves the currently edited file."""
        file_path = filedialog.asksaveasfilename()
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_widget.get('1.0', tk.END))
            except Exception as e:
                messagebox.showerror('Error', f'Failed to save file: {e}')

    def exit_app(self):
        """Exits the application."""
        if messagebox.askyesno('Exit', 'Do you want to exit?'):
            self.root.destroy()

# Create the main window
root = tk.Tk()
app = ConfigFileManager(root)

# Add Save and Exit options to the File Menu
save_item = tk.Menu(self.file_menu, tearoff=0)
save_item.add_command(label='Save', command=app.save_file)
self.file_menu.add_cascade(label='File', menu=save_item)

exit_item = tk.Menu(self.file_menu, tearoff=0)
exit_item.add_command(label='Exit', command=app.exit_app)
self.file_menu.add_cascade(label='File', menu=exit_item)

# Start the GUI event loop
root.mainloop()
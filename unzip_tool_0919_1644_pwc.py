# 代码生成时间: 2025-09-19 16:44:50
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

class UnzipTool:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title('Unzip Tool')

        # Setup the main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Create a button to select a zip file
        self.select_button = tk.Button(self.frame, text='Select Zip File', command=self.select_zip_file)
        self.select_button.grid(row=0, column=0, padx=5, pady=5)

        # Create a button to extract the zip file
        self.extract_button = tk.Button(self.frame, text='Extract Zip File', command=self.extract_zip_file, state='disabled')
        self.extract_button.grid(row=1, column=0, padx=5, pady=5)

        # Create a label to display the status
        self.status_label = tk.Label(self.frame, text='')
        self.status_label.grid(row=2, column=0, padx=5, pady=5)

    def select_zip_file(self):
        # Open a file dialog to select a zip file
        self.zip_file_path = filedialog.askopenfilename(filetypes=[('Zip Files', '*.zip')], title='Select Zip File')
        if self.zip_file_path:
            # Enable the extract button
            self.extract_button.config(state='normal')
            self.status_label.config(text=f'Zip file selected: {os.path.basename(self.zip_file_path)}')

    def extract_zip_file(self):
        # Check if a zip file is selected
        if not self.zip_file_path:
            messagebox.showerror('Error', 'No zip file selected.')
            return

        # Extract the zip file
        try:
            with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
                # Get the directory where the zip file is located
                zip_dir = os.path.dirname(self.zip_file_path)
                # Extract all the contents into the directory
                zip_ref.extractall(zip_dir)
                self.status_label.config(text='Extraction successful!')
        except zipfile.BadZipFile:
            messagebox.showerror('Error', 'The selected file is not a valid zip file.')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')

    def run(self):
        # Start the main event loop
        self.root.mainloop()

# Create the main window
root = tk.Tk()

# Create an instance of the UnzipTool class
unzip_tool = UnzipTool(root)

# Run the application
unzip_tool.run()
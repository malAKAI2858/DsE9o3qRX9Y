# 代码生成时间: 2025-09-21 21:34:19
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import numpy as np

"""
Data Cleaning and Preprocessing Tool using Python and Tkinter

This script creates a GUI application that allows users to load a dataset,
perform basic data cleaning and preprocessing operations,
and save the cleaned dataset.
"""

class DataCleaningApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Data Cleaning and Preprocessing Tool')

        # Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # File menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self.load_data)
        file_menu.add_command(label='Save', command=self.save_data)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.quit)

        # Operations menu
        operations_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Operations', menu=operations_menu)
        operations_menu.add_command(label='Remove Duplicates', command=self.remove_duplicates)
        operations_menu.add_command(label='Fill Missing Values', command=self.fill_missing_values)

        # Status label
        self.status_label = tk.Label(self.root, text='', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def load_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.status_label.config(text='Data loaded successfully.')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to load data: {e}')

    def save_data(self):
        if hasattr(self, 'df'):
            file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])
            if file_path:
                try:
                    self.df.to_csv(file_path, index=False)
                    self.status_label.config(text='Data saved successfully.')
                except Exception as e:
                    messagebox.showerror('Error', f'Failed to save data: {e}')
        else:
            messagebox.showwarning('Warning', 'No data to save. Please load a dataset first.')

    def remove_duplicates(self):
        if hasattr(self, 'df'):
            try:
                self.df = self.df.drop_duplicates()
                self.status_label.config(text='Duplicates removed successfully.')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to remove duplicates: {e}')
        else:
            messagebox.showwarning('Warning', 'No data to process. Please load a dataset first.')

    def fill_missing_values(self):
        if hasattr(self, 'df'):
            method = simpledialog.askstring('Input', 'Enter the method to fill missing values (e.g., mean, median, mode, constant):', parent=self.root)
            if method:
                try:
                    self.df.fillna(self.df.mean() if method.lower() == 'mean' else
                                   self.df.median() if method.lower() == 'median' else
                                   self.df.mode().iloc[0] if method.lower() == 'mode' else
                                   simpledialog.askstring('Input', 'Enter a constant value to fill missing values:', parent=self.root),
                                   inplace=True)
                    self.status_label.config(text='Missing values filled successfully.')
                except Exception as e:
                    messagebox.showerror('Error', f'Failed to fill missing values: {e}')
        else:
            messagebox.showwarning('Warning', 'No data to process. Please load a dataset first.')

if __name__ == '__main__':
    root = tk.Tk()
    app = DataCleaningApp(root)
    root.mainloop()
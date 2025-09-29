# 代码生成时间: 2025-09-29 20:21:10
import tkinter as tk
from tkinter import ttk


class TableSortingFilter:
    def __init__(self, master):
        self.master = master
        self.master.title('Table Sorting Filter')
        self.master.geometry('800x600')

        # Initialize table
        self.tree = ttk.Treeview(self.master, columns=('Name', 'Age', 'City'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Age', text='Age')
        self.tree.heading('City', text='City')
        self.tree.column('Name', width=200)
        self.tree.column('Age', width=100)
        self.tree.column('City', width=200)
        self.tree.pack(pady=20)

        # Initialize data
        self.data = [
            ('Alice', 30, 'New York'),
            ('Bob', 25, 'San Francisco'),
            ('Charlie', 35, 'Los Angeles'),
            ('David', 22, 'Chicago'),
            ('Eve', 26, 'Houston')
        ]
        for item in self.data:
            self.tree.insert('', 'end', values=item)

        # Initialize filters
        self.filters = {}
        self.filters['Name'] = tk.StringVar()
        self.filters['Age'] = tk.IntVar()
        self.filters['City'] = tk.StringVar()

        # Create filter frame
        self.filter_frame = tk.Frame(self.master)
        self.filter_frame.pack(pady=10)

        # Create filter entries and labels
        for column, var in self.filters.items():
            tk.Label(self.filter_frame, text=f'Filter {column}:').pack(side=tk.LEFT, padx=5)
            tk.Entry(self.filter_frame, textvariable=var).pack(side=tk.LEFT, padx=5)

        # Filter button
        tk.Button(self.filter_frame, text='Filter', command=self.filter_data).pack(side=tk.LEFT, padx=5)

    def filter_data(self):
        "
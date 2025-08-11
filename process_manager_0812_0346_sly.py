# 代码生成时间: 2025-08-12 03:46:39
import tkinter as tk
from tkinter import ttk
import psutil
import os

"""
Process Manager application using Python and Tkinter.
This application allows users to view and terminate system processes.
"""

class ProcessManager:
    def __init__(self, master):
        """Initialize the ProcessManager GUI."""
        self.master = master
        self.master.title('Process Manager')
        self.tree = None
        self.create_widgets()
        self.update_process_list()

    def create_widgets(self):
        """Create the GUI widgets."""
        self.tree = ttk.Treeview(self.master)
        self.tree['columns'] = ('PID', 'Name', 'Status')
        self.tree.heading('#0', text='Processes')
        self.tree.heading('PID', text='PID')
        self.tree.heading('Name', text='Process Name')
        self.tree.heading('Status', text='Status')
        self.tree.grid(row=0, column=0, sticky='nsew')

        ttk.Button(self.master, text='Update List', command=self.update_process_list).grid(row=1, column=0)
        ttk.Button(self.master, text='Kill Process', command=self.kill_process).grid(row=2, column=0)

    def update_process_list(self):
        """Update the process list in the GUI."""
        self.tree.delete(*self.tree.get_children())  # Clear the treeview
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            self.tree.insert('', 'end', values=(proc.info['pid'], proc.info['name'], proc.info['status']))

    def kill_process(self):
        """Kill the selected process."""
        selected_item = self.tree.selection()[0]
        pid = int(self.tree.item(selected_item, 'values')[0])
        try:
            process = psutil.Process(pid)
            process.terminate()
            self.master.bell()  # Notify the user
            self.update_process_list()  # Update the process list
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            self.master.bell()  # Notify the user of the error
            print(f'Error terminating process with PID {pid}: Access denied or process does not exist.')

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = ProcessManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()
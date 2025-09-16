# 代码生成时间: 2025-09-16 21:32:16
import tkinter as tk
from tkinter import ttk
import subprocess
import psutil
import sys

"""
Process Manager GUI Application using Python and Tkinter.
This application allows users to view and manage system processes.
"""

class ProcessManager:
    def __init__(self, root):
        self.root = root
        self.root.title('Process Manager')

        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Define columns
        self.tree = ttk.Treeview(self.main_frame, columns=('PID', 'Name', 'Status'), show='headings')
        self.tree.heading('PID', text='PID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Status', text='Status')
        self.tree.grid(column=0, row=0, sticky='nsew')

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # Scrollbar for Treeview
        self.scroll = ttk.Scrollbar(self.main_frame, command=self.tree.yview)
        self.scroll.grid(column=1, row=0, sticky='ns')
        self.tree.configure(yscrollcommand=self.scroll.set)

        # Buttons
        self.start_button = ttk.Button(self.main_frame, text='Start Process', command=self.start_process)
        self.start_button.grid(column=0, row=1, pady=5)

        self.terminate_button = ttk.Button(self.main_frame, text='Terminate Process', command=self.terminate_process)
        self.terminate_button.grid(column=0, row=2, pady=5)

        self.refresh_button = ttk.Button(self.main_frame, text='Refresh', command=self.refresh_processes)
        self.refresh_button.grid(column=1, row=1, pady=5)

        self.refresh_processes()

    def refresh_processes(self):
        """Refresh the list of processes."""
        self.tree.delete(*self.tree.get_children())
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                self.tree.insert('', tk.END, values=(proc.info['pid'], proc.info['name'], proc.info['status']))
            except psutil.NoSuchProcess:
                pass

    def on_select(self, event):
        """Handle selection of a process."""
        item = self.tree.selection()[0]
        pid = self.tree.item(item, 'values')[0]
        self.terminate_button['state'] = 'normal'  # Enable terminate button

    def start_process(self):
        """Start a new process."""
        try:
            # Prompt user for command to run
            cmd = simpledialog.askstring('Input', 'Enter command to run:', parent=self.root)
            if cmd:
                subprocess.Popen(cmd, shell=True)
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def terminate_process(self):
        """Terminate the selected process."""
        item = self.tree.selection()[0]
        pid = self.tree.item(item, 'values')[0]
        try:
            proc = psutil.Process(int(pid))
            proc.terminate()
            self.refresh_processes()
        except Exception as e:
            messagebox.showerror('Error', str(e))

def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = ProcessManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()
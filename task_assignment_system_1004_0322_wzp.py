# 代码生成时间: 2025-10-04 03:22:21
import tkinter as tk
from tkinter import messagebox

"""
Task Assignment System using Python and Tkinter.
This program allows users to assign tasks and view task lists.
"""

class TaskAssignmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Task Assignment System')

        # Initialize task list
        self.tasks = []

        # Create task input frame
        self.task_input_frame = tk.Frame(root)
        self.task_input_frame.pack()

        # Create label for task input
        self.task_label = tk.Label(self.task_input_frame, text='Enter task:')
        self.task_label.pack(side=tk.LEFT)

        # Create input box for task
        self.task_entry = tk.Entry(self.task_input_frame, width=50)
        self.task_entry.pack(side=tk.LEFT)

        # Create add task button
        self.add_task_button = tk.Button(self.task_input_frame, text='Add Task', command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        # Create listbox for displaying tasks
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack()

    def add_task(self):
        """Add a new task to the task list."""
        task = self.task_entry.get()
        if not task:
            messagebox.showwarning('Warning', 'Task cannot be empty.')
            return

        # Add task to the list and clear input box
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def display_tasks(self):
        """Display all tasks in the listbox."""
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = TaskAssignmentSystem(root)
    app.display_tasks()
    root.mainloop()

if __name__ == '__main__':
    main()
# 代码生成时间: 2025-10-14 01:44:25
import tkinter as tk
from tkinter import messagebox

"""
Online Learning Platform GUI Application using Python and Tkinter.
This application provides a simple user interface for an online learning platform.
"""

class OnlineLearningPlatform:
    def __init__(self, root):
        """
        Initialize the Online Learning Platform with Tkinter GUI.
        :param root: The root window of the Tkinter application.
        """
        self.root = root
        self.root.title('Online Learning Platform')
        
        # Create main frame and labels
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets for the application.
        """
        # Create a label for the course title
        self.course_label = tk.Label(self.main_frame, text='Course Title:', font=('Arial', 14))
        self.course_label.grid(row=0, column=0, padx=5, pady=5)
        
        # Create an entry widget for the course title
        self.course_entry = tk.Entry(self.main_frame, font=('Arial', 12))
        self.course_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Create a label for the course description
        self.desc_label = tk.Label(self.main_frame, text='Course Description:', font=('Arial', 14))
        self.desc_label.grid(row=1, column=0, padx=5, pady=5)
        
        # Create a text widget for the course description
        self.desc_text = tk.Text(self.main_frame, height=5, font=('Arial', 12))
        self.desc_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        # Create a button to save the course information
        self.save_button = tk.Button(self.main_frame, text='Save Course', command=self.save_course)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)
        
    def save_course(self):
        """
        Save the course information to a file or database.
        """
        try:
            course_title = self.course_entry.get()
            course_description = self.desc_text.get("1.0", "end-1c")
            
            # Placeholder for saving logic
            print(f"Course Title: {course_title}
Course Description: {course_description}")
            messagebox.showinfo("Success", "Course saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    """
    Create the main application window and run the application.
    """
    root = tk.Tk()
    app = OnlineLearningPlatform(root)
    root.mainloop()

if __name__ == '__main__':
    main()
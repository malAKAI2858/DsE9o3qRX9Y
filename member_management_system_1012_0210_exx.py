# 代码生成时间: 2025-10-12 02:10:26
import tkinter as tk
from tkinter import messagebox

# Define a class for the Member Management System
class MemberManagementSystem:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Member Management System")

        # Create a frame for the form
        self.form_frame = tk.Frame(self.master)
        self.form_frame.pack(pady=20)

        # Create labels and entry fields for member information
        self.create_form_widgets()

        # Create buttons for adding and updating members
        self.create_buttons()

    def create_form_widgets(self):
        # Labels for form fields
        tk.Label(self.form_frame, text="Member ID:").grid(row=0, column=0)
        tk.Label(self.form_frame, text="Name:").grid(row=1, column=0)
        tk.Label(self.form_frame, text="Email:").grid(row=2, column=0)

        # Entry fields for form data
        self.member_id_entry = tk.Entry(self.form_frame)
        self.member_id_entry.grid(row=0, column=1)
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=1, column=1)
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1)

    def create_buttons(self):
        # Add member button
        tk.Button(self.form_frame, text="Add Member", command=self.add_member).grid(row=3, column=0, pady=10)

        # Update member button
        tk.Button(self.form_frame, text="Update Member", command=self.update_member).grid(row=3, column=1, pady=10)

    def add_member(self):
        try:
            member_id = self.member_id_entry.get()
            name = self.name_entry.get()
            email = self.email_entry.get()

            # Here you would normally save the member to a database or other storage
            # For this example, we'll just print to the console
            print(f"Adding member with ID: {member_id}, Name: {name}, Email: {email}")
            messagebox.showinfo("Success", "Member added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_member(self):
        try:
            member_id = self.member_id_entry.get()
            name = self.name_entry.get()
            email = self.email_entry.get()

            # Here you would normally update the member in a database or other storage
            # For this example, we'll just print to the console
            print(f"Updating member with ID: {member_id}, Name: {name}, Email: {email}")
            messagebox.showinfo("Success", "Member updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Function to run the application
def run():
    root = tk.Tk()
    app = MemberManagementSystem(root)
    root.mainloop()

# Check if the script is being run directly and not being imported
if __name__ == "__main__":
    run()
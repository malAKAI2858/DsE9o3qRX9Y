# 代码生成时间: 2025-08-29 02:24:08
import tkinter as tk
from tkinter import messagebox

# User class to manage user details
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # 'admin' or 'user'

# UserPermissionSystem class to manage user permissions
class UserPermissionSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store users

    def add_user(self, username, password, role):
        if username in self.users:
            raise ValueError("User already exists.")

        new_user = User(username, password, role)
        self.users[username] = new_user
        return True

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("User does not exist.")

        del self.users[username]
        return True

    def change_password(self, username, new_password):
        if username not in self.users:
            raise ValueError("User does not exist.")

        self.users[username].password = new_password
        return True

    def change_role(self, username, new_role):
        if username not in self.users:
            raise ValueError("User does not exist.")

        self.users[username].role = new_role
        return True

# Application class to create the GUI
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Permission System")
        self.user_permission_system = UserPermissionSystem()

        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username: ")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password: ")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.role_label = tk.Label(self, text="Role (admin/user): ")
        self.role_label.pack()

        self.role_entry = tk.Entry(self)
        self.role_entry.pack()

        self.add_button = tk.Button(self, text="Add User", command=self.add_user)
        self.add_button.pack()

        self.remove_button = tk.Button(self, text="Remove User", command=self.remove_user)
        self.remove_button.pack()

        self.change_password_button = tk.Button(self, text="Change Password", command=self.change_password)
        self.change_password_button.pack()

        self.change_role_button = tk.Button(self, text="Change Role", command=self.change_role)
        self.change_role_button.pack()

    def add_user(self):
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            role = self.role_entry.get()
            self.user_permission_system.add_user(username, password, role)
            messagebox.showinfo("Success", "User added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_user(self):
        try:
            username = self.username_entry.get()
            self.user_permission_system.remove_user(username)
            messagebox.showinfo("Success", "User removed successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def change_password(self):
        try:
            username = self.username_entry.get()
            new_password = self.password_entry.get()
            self.user_permission_system.change_password(username, new_password)
            messagebox.showinfo("Success", "Password changed successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def change_role(self):
        try:
            username = self.username_entry.get()
            new_role = self.role_entry.get()
            self.user_permission_system.change_role(username, new_role)
            messagebox.showinfo("Success", "Role changed successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Main function to run the application
def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
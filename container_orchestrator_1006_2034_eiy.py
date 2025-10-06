# 代码生成时间: 2025-10-06 20:34:53
import tkinter as tk
from tkinter import messagebox
import subprocess
import json

"""
A simple container orchestrator tool using Python and Tkinter.
This tool allows users to manage Docker containers through a GUI.
"""

class ContainerOrchestrator:
    """Class to handle container orchestration operations."""
    def __init__(self, master):
        """Initialize the Tkinter application."""
        self.master = master
        self.master.title("Container Orchestrator")
        self.create_widgets()

    def create_widgets(self):
        """Create the GUI components."""
        # Container list label
        label = tk.Label(self.master, text="Container List:")
        label.pack()

        # Container list box
        self.container_list = tk.Listbox(self.master)
        self.container_list.pack()

        # Buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack()

        # Refresh button
        refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh_containers)
        refresh_button.pack(side=tk.LEFT)

        # Start button
        start_button = tk.Button(button_frame, text="Start", command=self.start_container)
        start_button.pack(side=tk.LEFT)

        # Stop button
        stop_button = tk.Button(button_frame, text="Stop", command=self.stop_container)
        stop_button.pack(side=tk.LEFT)

    def refresh_containers(self):
        """Refresh the container list."""
        try:
            # Get a list of running containers
            output = subprocess.check_output(
                ["docker", "ps", "--format", "{{.Names}}"]).decode("utf-8")
            container_names = output.strip().split("
")
            # Update the container list box
            self.container_list.delete(0, tk.END)
            for name in container_names:
                self.container_list.insert(tk.END, name)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", "Failed to refresh containers")
            print(f"Error: {e}")

    def start_container(self):
        """Start a selected container."""
        try:
            # Get the selected container name
            container_name = self.container_list.get(
                self.container_list.curselection())
            # Start the container
            subprocess.run(["docker", "start", container_name], check=True)
            messagebox.showinfo("Success", f"Container '{container_name}' started")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", "Failed to start container")
            print(f"Error: {e}")
        except IndexError:  # No container selected
            messagebox.showwarning("Warning", "Please select a container to start")

    def stop_container(self):
        """Stop a selected container."""
        try:
            # Get the selected container name
            container_name = self.container_list.get(
                self.container_list.curselection())
            # Stop the container
            subprocess.run(["docker", "stop", container_name], check=True)
            messagebox.showinfo("Success", f"Container '{container_name}' stopped")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", "Failed to stop container")
            print(f"Error: {e}")
        except IndexError:  # No container selected
            messagebox.showwarning("Warning", "Please select a container to stop")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContainerOrchestrator(root)
    root.mainloop()
# 代码生成时间: 2025-10-05 01:52:25
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

"""
Data Annotation Platform using Python and Tkinter.
This application allows users to annotate data interactively.
"""

class DataAnnotationPlatform:
    def __init__(self, root):
        """Initialize the Data Annotation Platform."""
        self.root = root
        self.root.title("Data Annotation Platform")
        self.root.geometry("800x600")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Annotation menu
        annotate_menu = tk.Menu(self.menu_bar, tearoff=0)
        annotate_menu.add_command(label="Annotate", command=self.annotate_data)
        self.menu_bar.add_cascade(label="Annotate", menu=annotate_menu)

        # Text widget for displaying data
        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

    def open_file(self):
        """Open a file and display its contents in the text widget."""
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        try:
            with open(file_path, 'r') as file:
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, file.read())
        except IOError:
            messagebox.showerror("Error", "Failed to open file.")

    def save_file(self):
        """Save the text widget contents to a file."""
        file_path = filedialog.asksaveasfilename()
        if not file_path:
            return

        try:
            with open(file_path, 'w') as file:
                file.write(self.text_widget.get(1.0, tk.END))
        except IOError:
            messagebox.showerror("Error", "Failed to save file.")

    def annotate_data(self):
        """Prompt the user to annotate the data."""
        annotation = simpledialog.askstring("Annotation", "Enter annotation: ")
        if annotation:
            self.text_widget.insert(tk.INSERT, annotation)

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnnotationPlatform(root)
    root.mainloop()
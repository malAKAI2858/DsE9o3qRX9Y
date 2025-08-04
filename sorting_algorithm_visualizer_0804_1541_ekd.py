# 代码生成时间: 2025-08-04 15:41:35
import tkinter as tk
from tkinter import ttk
import random
import time

"""
Sorting Algorithm Visualizer using Python and Tkinter.
This program provides a GUI to visualize different sorting algorithms.
"""

class SortingAlgorithmVisualizer:
    def __init__(self, root):
        """Initialize the Tkinter window and components."""
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        
        # Frame for the list display
        self.list_frame = ttk.Frame(self.root)
        self.list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Frame for the controls
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        
        # Create the list box to display the array
        self.list_box = tk.Listbox(self.list_frame, width=50, height=20)
        self.list_box.pack(fill=tk.BOTH, expand=True)
        
        # Add buttons to the control frame
        ttk.Button(self.control_frame, text="Generate Random List", command=self.generate_list).pack(fill=tk.X)
        ttk.Button(self.control_frame, text="Sort List", command=self.sort_list).pack(fill=tk.X)
        
        # Algorithm selection
        self.algorithm_var = tk.StringVar()
        ttk.Label(self.control_frame, text="Choose Algorithm: ").pack(fill=tk.X)
        ttk.Combobox(self.control_frame, textvariable=self.algorithm_var, values=["Bubble Sort", "Insertion Sort\].pack(fill=tk.X)
        
    def generate_list(self):
        """Generate a random list of integers."""
        try:
            self.list_box.delete(0, tk.END)
            for _ in range(50):
                self.list_box.insert(tk.END, random.randint(0, 100))
        except Exception as e:
            print(f"Error generating list: {e}")
        
    def sort_list(self):
        """Sort the list using the selected algorithm."""
        try:
            # Get the list of numbers from the Listbox
            numbers = [int(item) for item in self.list_box.get(0, tk.END)]
            
            # Sort the list using the selected algorithm
            if self.algorithm_var.get() == "Bubble Sort":
                self.bubble_sort(numbers)
            elif self.algorithm_var.get() == "Insertion Sort":
                self.insertion_sort(numbers)
            else:
                raise ValueError("Unsupported sorting algorithm")
            
            # Update the Listbox with the sorted list
            self.list_box.delete(0, tk.END)
            for number in numbers:
                self.list_box.insert(tk.END, str(number))
        except ValueError as ve:
            print(f"Error sorting list: {ve}")
        except Exception as e:
            print(f"Error sorting list: {e}")
        
    def bubble_sort(self, numbers):
        """Perform bubble sort on the list of numbers."""
        n = len(numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    self.update_list_box(numbers)
                    time.sleep(0.1)
            
    def insertion_sort(self, numbers):
        """Perform insertion sort on the list of numbers."""
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i-1
            while j >= 0 and key < numbers[j]:
                numbers[j+1] = numbers[j]
                j -= 1
            numbers[j+1] = key
            self.update_list_box(numbers)
            time.sleep(0.1)
        
    def update_list_box(self, numbers):
        """Update the Listbox with the current state of the list."""
        self.list_box.delete(0, tk.END)
        for number in numbers:
            self.list_box.insert(tk.END, str(number))
        
# Create the main window and run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = SortingAlgorithmVisualizer(root)
    root.mainloop()
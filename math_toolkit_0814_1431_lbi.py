# 代码生成时间: 2025-08-14 14:31:44
import tkinter as tk
from tkinter import messagebox

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculate(operation, x, y):
    """Perform the math operation based on the given operation."""
    if operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        raise ValueError("Invalid operation.")

def on_calculate():
    """Event handler for the calculate button."""
    try:
        operation = operation_var.get()
        x = float(num1_var.get())
        y = float(num2_var.get())
        result = calculate(operation, x, y)
        result_var.set(f"{result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_clear():
    """Event handler for the clear button."""
    num1_var.set("")
    num2_var.set("")
    result_var.set("")

def on_quit():
    """Event handler for the quit button."""
    root.quit()

def main():
    """Create the main window and layout."""
    global root, operation_var, num1_var, num2_var, result_var
    root = tk.Tk()
    root.title("Math Toolkit")
    root.geometry("300x200")
    
    tk.Label(root, text="Operation").grid(row=0, column=0)
    operation_var = tk.StringVar()
    tk.OptionMenu(root, operation_var, "add", "add", "subtract", "multiply", "divide").grid(row=0, column=1)
    
    tk.Label(root, text="Number 1").grid(row=1, column=0)
    num1_var = tk.StringVar()
    tk.Entry(root, textvariable=num1_var).grid(row=1, column=1)
    
    tk.Label(root, text="Number 2").grid(row=2, column=0)
    num2_var = tk.StringVar()
    tk.Entry(root, textvariable=num2_var).grid(row=2, column=1)
    
    tk.Button(root, text="Calculate", command=on_calculate).grid(row=3, column=0, columnspan=2)
    
    tk.Button(root, text="Clear", command=on_clear).grid(row=4, column=0)
    
    tk.Button(root, text="Quit", command=on_quit).grid(row=4, column=1)
    
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var).grid(row=5, column=0, columnspan=2)
    
    root.mainloop()

def __name__ == "__main__":
    main()

# 代码生成时间: 2025-07-31 22:13:44
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

"""
A simple shopping cart application using Python and Tkinter.
This application allows users to add items to a cart and view the total cost.
"""

# Define a class to represent a product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Define a class to represent the shopping cart
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a product to the cart."""
        self.products.append(product)

    def get_total_cost(self):
        """Calculate the total cost of all products in the cart."""
        return sum(product.price for product in self.products)

    def get_cart_contents(self):
        """Get a list of all products in the cart."""
        return self.products

# Define the main application class
class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        self.cart = ShoppingCart()

        self.create_widgets()

    def create_widgets(self):
        # Create a label to display the cart contents
        self.label = tk.Label(self.root, text="")
        self.label.pack()

        # Create a button to add items to the cart
        add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        add_button.pack()

        # Create a button to view the cart contents
        view_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        view_button.pack()

    def add_item(self):
        """Prompt the user to add an item to the cart."""
        name = simpledialog.askstring("Input", "Enter the item name: ")
        if not name:
            messagebox.showerror("Error", "Item name cannot be empty.")
            return

        price = simpledialog.askstring("Input", "Enter the item price: ")
        if not price or not price.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Invalid price format. Please enter a numerical value.")
            return

        # Create a new product and add it to the cart
        product = Product(name, float(price))
        self.cart.add_product(product)

        # Update the label to show the cart contents
        self.update_label()

    def view_cart(self):
        """Display the contents of the shopping cart."""
        products = self.cart.get_cart_contents()
        if not products:
            messagebox.showinfo("Info", "Your cart is empty.")
            return

        message = "Items in your cart:"
        for product in products:
            message += f
            "{product.name} - ${product.price}"

        messagebox.showinfo("Cart Contents", message)

    def update_label(self):
        """Update the label to show the cart contents."""
        products = self.cart.get_cart_contents()
        if not products:
            self.label.config(text="Your cart is empty.")
        else:
            message = "Items in your cart:"
            for product in products:
                message += f
                "{product.name} - ${product.price}"
            self.label.config(text=message)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
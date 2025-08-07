# 代码生成时间: 2025-08-07 11:24:14
import tkinter as tk
from tkinter import ttk


class ShoppingCartApp:
    def __init__(self, root):
        """
        Initialize the ShoppingCartApp with a Tkinter window.
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Shopping Cart App")
        self.root.geometry("400x300")
        self.products = {}
        self.cart = {}

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create the UI widgets for the shopping cart application.
        """
        # Add product frame
        self.product_frame = ttk.LabelFrame(self.root, text="Products")
        self.product_frame.grid(sticky="ew", padx=10, pady=10)

        # Add a listbox to display products
        self.product_listbox = tk.Listbox(self.product_frame)
        self.product_listbox.pack(side="left", fill="both", expand=True)

        # Add a scrollbar for the listbox
        self.scrollbar = ttk.Scrollbar(self.product_frame, orient="vertical", command=self.product_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.product_listbox.config(yscrollcommand=self.scrollbar.set)

        # Add buttons to add and remove products from the cart
        self.add_button = ttk.Button(self.root, text="Add to Cart", command=self.add_product)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_button = ttk.Button(self.root, text="Remove from Cart", command=self.remove_product)
        self.remove_button.grid(row=1, column=1, padx=10, pady=10)

        # Add a listbox to display the cart items
        self.cart_listbox = tk.Listbox(self.root)
        self.cart_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Add a scrollbar for the cart listbox
        self.cart_scrollbar = ttk.Scrollbar(self.root, orient="vertical\, command=self.cart_listbox.yview)
        self.cart_scrollbar.grid(row=2, column=2, sticky="ns")
        self.cart_listbox.config(yscrollcommand=self.cart_scrollbar.set)

        # Populate the product listbox with products
        self.populate_product_listbox()

    def populate_product_listbox(self):
        """
        Populate the product listbox with product names.
        """
        products = ["Apple", "Banana", "Cherry", "Date"]
        for product in products:
            self.product_listbox.insert("end", product)

    def add_product(self):
        """
        Add the selected product to the cart.
        """
        try:
            selected_product = self.product_listbox.get(self.product_listbox.curselection())
            if selected_product not in self.cart:
                self.cart[selected_product] = 1
            else:
                self.cart[selected_product] += 1
            self.update_cart_listbox()
        except tk.TclError:
            print("No product selected.")

    def remove_product(self):
        """
        Remove the selected product from the cart.
        """
        try:
            selected_product = self.cart_listbox.get(self.cart_listbox.curselection())
            if selected_product in self.cart:
                if self.cart[selected_product] == 1:
                    del self.cart[selected_product]
                else:
                    self.cart[selected_product] -= 1
            self.update_cart_listbox()
        except tk.TclError:
            print("No product selected.")

    def update_cart_listbox(self):
        """
        Update the cart listbox with the current cart items.
        """
        self.cart_listbox.delete(0, "end")
        for product, quantity in self.cart.items():
            self.cart_listbox.insert("end", f"{product} (x{quantity})")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
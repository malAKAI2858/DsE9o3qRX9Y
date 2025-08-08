# 代码生成时间: 2025-08-09 04:28:13
import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog


class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total_cost = 0.0

    def add_item(self, item_name, quantity, price):
        """
        Add an item to the shopping cart.
        :param item_name: Name of the item as string
        :param quantity: Quantity of the item as integer
        :param price: Price of the item as float
        """
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}
        self.update_total_cost()

    def remove_item(self, item_name, quantity):
        """
        Remove a specified quantity of an item from the shopping cart.
        :param item_name: Name of the item as string
        :param quantity: Quantity to remove as integer
        """
        if item_name in self.items:
            current_quantity = self.items[item_name]['quantity']
            if quantity >= current_quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity
            self.update_total_cost()
        else:
            messagebox.showerror('Error', 'Item not found in cart')

    def update_total_cost(self):
        """
        Update the total cost of the cart after adding or removing items.
        """
        self.total_cost = sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_total_cost(self):
        """
        Return the total cost of the items in the cart.
        """
        return self.total_cost


    def show_cart(self):
        """
        Return a string representation of the shopping cart.
        """
        cart_str = 'Shopping Cart:
'
        for item_name, details in self.items.items():
            cart_str += f'{item_name}: {details[
# 代码生成时间: 2025-08-22 23:31:54
import tkinter as tk
from tkinter import messagebox, simpledialog

# 购物车类
class ShoppingCart:
    def __init__(self):
        self.items = []  # 存储购物车中的商品

    def add_item(self, item):
        """添加商品到购物车"""
        self.items.append(item)

    def remove_item(self, item):
        """从购物车中移除商品"""
        try:
            self.items.remove(item)
        except ValueError:
            messagebox.showerror("Error", "Item not found in the cart")

    def get_cart_items(self):
        """获取购物车中的商品列表"""
        return self.items

# 购物车应用的主窗口类
class ShoppingCartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cart = ShoppingCart()  # 创建购物车实例
        self.title("Shopping Cart App")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # 添加商品按钮
        self.add_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_button.pack(fill="x")

        # 移除商品按钮
        self.remove_button = tk.Button(self, text="Remove Item", command=self.remove_item)
        self.remove_button.pack(fill="x")

        # 显示购物车内容按钮
        self.show_button = tk.Button(self, text="Show Cart", command=self.show_cart)
        self.show_button.pack(fill="x")

        # 清空购物车按钮
        self.clear_button = tk.Button(self, text="Clear Cart", command=self.clear_cart)
        self.clear_button.pack(fill="x")

    def add_item(self):
        """添加商品到购物车"""
        item = simpledialog.askstring("Input", "Enter the item name to add: ")
        if item:
            self.cart.add_item(item)
            messagebox.showinfo("Added", f"Added {item} to the cart")
        else:
            messagebox.showwarning("Warning", "No item entered")

    def remove_item(self):
        """从购物车中移除商品"""
        item = simpledialog.askstring("Input", "Enter the item name to remove: ")
        if item:
            self.cart.remove_item(item)
            messagebox.showinfo("Removed", f"Removed {item} from the cart")
        else:
            messagebox.showwarning("Warning", "No item entered")

    def show_cart(self):
        """显示购物车中的商品列表"""
        items = self.cart.get_cart_items()
        messagebox.showinfo("Cart Contents", ", ".join(items) if items else "Cart is empty")

    def clear_cart(self):
        """清空购物车"""
        self.cart.items.clear()
        messagebox.showinfo("Cleared", "Shopping cart has been cleared")

# 运行购物车应用
if __name__ == '__main__':
    app = ShoppingCartApp()
    app.mainloop()
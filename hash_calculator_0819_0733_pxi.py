# 代码生成时间: 2025-08-19 07:33:18
 * hash_calculator.py - A simple hash calculator tool using Python and Tkinter.
 *
 * Features:
 * - Supports multiple hash algorithms (e.g., MD5, SHA1, SHA256).
 * - Provides a simple GUI for input and display of the hash value.
 * - Includes proper error handling and user feedback.
# 扩展功能模块
 */
# 优化算法效率

import tkinter as tk
from tkinter import messagebox
import hashlib

class HashCalculator:
    """A class to create a GUI for calculating hash values."""
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Calculator Tool")

        # Create input label and entry
        self.label = tk.Label(root, text="Enter text:")
        self.label.pack(pady=5)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
# 扩展功能模块

        # Create dropdown menu for selecting hash algorithm
        self.algorithms = ["MD5", "SHA1", "SHA256"]
        self.algorithm_var = tk.StringVar(root)
        self.algorithm_var.set("MD5")  # default value
        self.algo_menu = tk.OptionMenu(root, self.algorithm_var, *self.algorithms)
# 扩展功能模块
        self.algo_menu.pack(pady=5)
# 优化算法效率

        # Create calculate button
        self.calculate_btn = tk.Button(root, text="Calculate Hash", command=self.calculate_hash)
        self.calculate_btn.pack(pady=5)
# 改进用户体验

        # Create output label and entry
        self.output_label = tk.Label(root, text="Hash value:")
        self.output_label.pack(pady=5)
        self.output_entry = tk.Entry(root, state="readonly")
        self.output_entry.pack(pady=5)

    def calculate_hash(self):
# 改进用户体验
        """Calculate the hash value based on the selected algorithm."""
        text = self.entry.get()
# 添加错误处理
        algorithm = self.algorithm_var.get()

        if not text:
            messagebox.showerror("Error", "Please enter some text to calculate its hash value.")
            return

        try:
            if algorithm == "MD5":
                self.display_hash(hashlib.md5(text.encode()).hexdigest())
            elif algorithm == "SHA1":
                self.display_hash(hashlib.sha1(text.encode()).hexdigest())
            elif algorithm == "SHA256":
                self.display_hash(hashlib.sha256(text.encode()).hexdigest())
            else:
                messagebox.showerror("Error", "Unsupported hash algorithm.")
# NOTE: 重要实现细节
        except Exception as e:
# TODO: 优化性能
            messagebox.showerror("Error", str(e))

    def display_hash(self, hash_value):
        """Display the calculated hash value in the GUI."""
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, hash_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = HashCalculator(root)
    root.mainloop()
# 代码生成时间: 2025-09-24 06:13:20
import tkinter as tk
from tkinter import messagebox
import hashlib
# 优化算法效率

"""
哈希值计算工具
"""

class HashCalculator:
# NOTE: 重要实现细节
    def __init__(self, master):
        """初始化界面"""
# FIXME: 处理边界情况
        self.master = master
        master.title('哈希值计算工具')
        
        # 输入框
        self.input_label = tk.Label(master, text='输入文本:')
# 添加错误处理
        self.input_label.pack()
        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.pack()
# 添加错误处理
        
        # 选择哈希算法
        self.algorithm_label = tk.Label(master, text='选择哈希算法:')
        self.algorithm_label.pack()
        self.algorithm_var = tk.StringVar(master)
        self.algorithm_var.set('sha256')  # 默认选择sha256
# NOTE: 重要实现细节
        self.algorithm_options = ['md5', 'sha1', 'sha256', 'sha512']
        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, *self.algorithm_options)
        self.algorithm_menu.pack()
        
        # 计算按钮
        self.calculate_button = tk.Button(master, text='计算哈希值', command=self.calculate_hash)
        self.calculate_button.pack()
        
        # 输出框
        self.output_label = tk.Label(master, text='哈希值:')
        self.output_label.pack()
        self.output_text = tk.Text(master, height=5, width=50)
        self.output_text.pack()
        
    def calculate_hash(self):
        """计算哈希值"""
        input_text = self.input_text.get(1.0, tk.END).strip()
        if not input_text:
            messagebox.showerror('错误', '请输入文本')
            return
        
        algorithm = self.algorithm_var.get()
        try:
            hash_value = hashlib.new(algorithm, input_text.encode('utf-8')).hexdigest()
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, hash_value)
        except ValueError as e:
            messagebox.showerror('错误', '无效的哈希算法')
# 优化算法效率

if __name__ == '__main__':
    root = tk.Tk()
    app = HashCalculator(root)
    root.mainloop()
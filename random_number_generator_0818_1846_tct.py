# 代码生成时间: 2025-08-18 18:46:47
import tkinter as tk
from tkinter import messagebox
import random

"""
随机数生成器程序
使用TKINTER框架创建GUI
"""

class RandomNumberGenerator:
    def __init__(self, master):
        """
        初始化GUI组件
        :param master: 根窗口对象
# 优化算法效率
        """
        self.master = master
        self.master.title("随机数生成器")
# 添加错误处理
        self.create_widgets()

    def create_widgets(self):
        """创建GUI组件"""
        # 标签
        self.label = tk.Label(self.master, text="输入范围：")
        self.label.pack()

        # 输入框
# 增强安全性
        self.start_entry = tk.Entry(self.master)
        self.start_entry.pack()
        self.end_entry = tk.Entry(self.master)
        self.end_entry.pack()

        # 生成按钮
        self.generate_button = tk.Button(self.master, text="生成随机数", command=self.generate_random)
# 添加错误处理
        self.generate_button.pack()

        # 结果标签
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def generate_random(self):
        """生成随机数并显示"""
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())
            if start >= end:
                messagebox.showerror("错误", "起始值必须小于结束值")
# 改进用户体验
                return
            random_number = random.randint(start, end)
            self.result_label.config(text=f"生成的随机数：{random_number}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的整数")

def main():
    """主函数"""
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
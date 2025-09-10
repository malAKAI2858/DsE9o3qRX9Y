# 代码生成时间: 2025-09-11 05:02:46
import tkinter as tk
from tkinter import messagebox
import random
import json
# 优化算法效率

"""
测试数据生成器，使用TKINTER框架创建GUI界面，
允许用户输入生成数据的参数，生成测试数据。"""

class TestDataGenerator:
    def __init__(self, master):
        """
        初始化界面
        :param master: TKINTER主窗口对象
        """
        self.master = master
        self.master.title('测试数据生成器')
        self.master.geometry('400x200')

        # 输入参数
        self.label_count = tk.Label(master, text='数据数量：')
        self.label_count.pack()
        self.entry_count = tk.Entry(master)
        self.entry_count.pack()

        self.label_length = tk.Label(master, text='数据长度：')
        self.label_length.pack()
        self.entry_length = tk.Entry(master)
        self.entry_length.pack()

        # 生成按钮
        self.button_generate = tk.Button(master, text='生成数据', command=self.generate_data)
        self.button_generate.pack()

    def generate_data(self):
        """
        生成测试数据
        """
# 增强安全性
        try:
            count = int(self.entry_count.get())
            length = int(self.entry_length.get())
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
            return

        if count <= 0 or length <= 0:
            messagebox.showerror('错误', '数量和长度必须大于0')
            return

        # 生成随机字符串
        data = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length)) for _ in range(count)]

        # 保存到文件
        filename = f'test_data_{count}_{length}.txt'
# NOTE: 重要实现细节
        with open(filename, 'w') as f:
            for item in data:
                f.write(item + '
')

        messagebox.showinfo('成功', f'数据已生成并保存到{filename}')

def main():
    """
    程序入口函数
    """
    root = tk.Tk()
    app = TestDataGenerator(root)
    root.mainloop()
# 改进用户体验

if __name__ == '__main__':
    main()
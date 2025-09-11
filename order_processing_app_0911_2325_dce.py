# 代码生成时间: 2025-09-11 23:25:42
import tkinter as tk
from tkinter import messagebox

# 订单处理流程模拟类
class OrderProcessing:
    def __init__(self):
        self.order_status = 'Pending'

    def receive_order(self):
        """接收订单"""
        self.order_status = 'Received'
        print(f'订单已接收，当前状态：{self.order_status}')

    def verify_order(self):
        """验证订单"""
        if self.order_status == 'Received':
            self.order_status = 'Verified'
            print(f'订单已验证，当前状态：{self.order_status}')
        else:
            raise ValueError('订单尚未接收，无法验证')

    def process_order(self):
        """处理订单"""
        if self.order_status == 'Verified':
            self.order_status = 'Processed'
            print(f'订单已处理，当前状态：{self.order_status}')
        else:
            raise ValueError('订单尚未验证，无法处理')

    def deliver_order(self):
        """交付订单"""
        if self.order_status == 'Processed':
            self.order_status = 'Delivered'
            print(f'订单已交付，当前状态：{self.order_status}')
        else:
            raise ValueError('订单尚未处理，无法交付')

# 订单处理应用程序类
class OrderProcessingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('订单处理流程')
        self.geometry('400x300')
        self.order_processing = OrderProcessing()

        self.create_widgets()

    def create_widgets(self):
        # 接收订单按钮
        self.receive_btn = tk.Button(self, text='接收订单', command=self.receive_order)
        self.receive_btn.pack(pady=10)

        # 验证订单按钮
        self.verify_btn = tk.Button(self, text='验证订单', command=self.verify_order)
        self.verify_btn.pack(pady=10)

        # 处理订单按钮
        self.process_btn = tk.Button(self, text='处理订单', command=self.process_order)
        self.process_btn.pack(pady=10)

        # 交付订单按钮
        self.deliver_btn = tk.Button(self, text='交付订单', command=self.deliver_order)
        self.deliver_btn.pack(pady=10)

    def receive_order(self):
        try:
            self.order_processing.receive_order()
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def verify_order(self):
        try:
            self.order_processing.verify_order()
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def process_order(self):
        try:
            self.order_processing.process_order()
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def deliver_order(self):
        try:
            self.order_processing.deliver_order()
        except Exception as e:
            messagebox.showerror('错误', str(e))

# 主函数
if __name__ == '__main__':
    app = OrderProcessingApp()
    app.mainloop()
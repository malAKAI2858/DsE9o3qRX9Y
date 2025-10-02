# 代码生成时间: 2025-10-03 02:02:24
import tkinter as tk
from tkinter import messagebox

# 贷款审批系统
class LoanApprovalSystem:
    def __init__(self):
        # 初始化Tkinter窗口
        self.root = tk.Tk()
        self.root.title('贷款审批系统')

        # 创建贷款信息输入表单
        self.create_loan_form()

        # 设置主窗口尺寸
        self.root.geometry('400x300')
        self.root.mainloop()

    def create_loan_form(self):
        # 创建输入框和标签
        self.label_name = tk.Label(self.root, text='姓名:')
        self.label_name.grid(row=0, column=0)

        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_income = tk.Label(self.root, text='月收入:')
        self.label_income.grid(row=1, column=0)

        self.entry_income = tk.Entry(self.root)
        self.entry_income.grid(row=1, column=1)

        self.label_credit = tk.Label(self.root, text='信用评分:')
        self.label_credit.grid(row=2, column=0)

        self.entry_credit = tk.Entry(self.root)
        self.entry_credit.grid(row=2, column=1)

        # 创建提交按钮
        self.submit_button = tk.Button(self.root, text='提交贷款申请', command=self.submit_loan)
        self.submit_button.grid(row=3, column=1, pady=10)

    def submit_loan(self):
        # 获取用户输入的贷款信息
        name = self.entry_name.get()
        income = self.entry_income.get()
        credit_score = self.entry_credit.get()

        # 验证输入信息
        if not name or not income or not credit_score:
            messagebox.showerror('错误', '请填写所有字段')
            return

        try:
            income = float(income)
            credit_score = int(credit_score)
        except ValueError:
            messagebox.showerror('错误', '输入格式不正确')
            return

        # 根据信用评分和收入审批贷款
        if credit_score >= 700 and income >= 5000:
            messagebox.showinfo('贷款审批结果', f'贷款批准，姓名：{name}')
        else:
            messagebox.showinfo('贷款审批结果', '贷款拒绝')

if __name__ == '__main__':
    # 创建贷款审批系统实例
    LoanApprovalSystem()
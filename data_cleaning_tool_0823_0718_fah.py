# 代码生成时间: 2025-08-23 07:18:25
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import numpy as np

# 数据清洗工具类
class DataCleaningTool:
    def __init__(self, master):
        self.master = master
        self.master.title("数据清洗和预处理工具")
        self.create_widgets()

    def create_widgets(self):
        # 添加文件选择按钮
        self.btn_open_file = tk.Button(self.master, text="选择文件", command=self.open_file)
        self.btn_open_file.pack()

        # 添加数据预处理按钮
        self.btn_preprocess = tk.Button(self.master, text="数据预处理", command=self.preprocess_data)
        self.btn_preprocess.pack()

        # 添加显示结果按钮
        self.btn_display_result = tk.Button(self.master, text="显示结果", command=self.display_result)
        self.btn_display_result.pack()

    def open_file(self):
        # 打开文件对话框
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files\, "*.xlsx"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.load_data()
        else:
            messagebox.showinfo("提示", "未选择文件")

    def load_data(self):
        try:
            if self.file_path.endswith(".csv"):
                self.data = pd.read_csv(self.file_path)
            elif self.file_path.endswith(".xlsx"):
                self.data = pd.read_excel(self.file_path)
            else:
                raise ValueError("不支持的文件类型")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def preprocess_data(self):
        # 数据预处理
        try:
            # 去除空值
            self.data.dropna(inplace=True)
            # 去除重复值
            self.data.drop_duplicates(inplace=True)
            # 填充空值
            fill_value = simpledialog.askstring("输入", "输入填充空值：")
            if fill_value is not None:
                self.data.fillna(fill_value, inplace=True)
        except Exception as e:
            messagebox.showerror("错误\, str(e))

    def display_result(self):
        # 显示处理后的结果
        try:
            result = self.data.to_csv(index=False)
            with open("cleaned_data.csv", "w") as f:
                f.write(result)
            messagebox.showinfo("提示", "数据处理完成，结果已保存为 cleaned_data.csv")
        except Exception as e:
            messagebox.showerror("错误", str(e))

# 创建主窗口
root = tk.Tk()
# 创建工具对象
tool = DataCleaningTool(root)
# 启动主循环
root.mainloop()
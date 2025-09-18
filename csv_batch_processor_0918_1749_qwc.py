# 代码生成时间: 2025-09-18 17:49:53
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

"""
CSV文件批量处理器
使用TKINTER框架，创建一个简单的GUI应用程序，
用于批量处理CSV文件。
"""

class CSVBatchProcessor:
    def __init__(self, root):
        """
        初始化GUI界面
        :param root: 根窗口
        """
        self.root = root
        self.root.title("CSV文件批量处理器")

        # 设置窗口大小
        self.root.geometry("600x400")

        # 添加按钮，用于选择文件夹
        self.select_folder_button = tk.Button(self.root, text="选择文件夹", command=self.select_folder)
        self.select_folder_button.pack()

        # 添加按钮，用于开始处理CSV文件
        self.process_csv_button = tk.Button(self.root, text="开始处理", command=self.process_csv)
        self.process_csv_button.pack()

        # 添加文本框，用于显示状态信息
        self.status_text = tk.Text(self.root, height=10, width=50)
        self.status_text.pack()

    def select_folder(self):
        """
        选择文件夹，并显示在文本框中
        """
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.status_text.delete(1.0, tk.END)
            self.status_text.insert(tk.END, folder_path)
        else:
            messagebox.showerror("错误", "未选择文件夹")

    def process_csv(self):
        """
        处理选择文件夹中的所有CSV文件
        """
        folder_path = self.status_text.get(1.0, tk.END).strip()
        if not folder_path:
            messagebox.showerror("错误", "未选择文件夹")
            return

        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                self.status_text.insert(tk.END, f"处理文件：{filename}...
")

                try:
                    # 读取CSV文件
                    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                        reader = csv.reader(file)

                        # 处理CSV文件内容
                        for row in reader:
                            self.process_row(row)

                except Exception as e:
                    self.status_text.insert(tk.END, f"处理文件：{filename} 失败，错误：{str(e)}
")
                else:
                    self.status_text.insert(tk.END, f"处理文件：{filename} 完成
")

    def process_row(self, row):
        """
        处理CSV文件的一行数据
        :param row: CSV文件的一行数据
        """
        # 这里可以添加处理每行数据的逻辑
        # 示例：打印每行数据
        print(row)


def main():
    """
    主函数，创建GUI界面
    """
    root = tk.Tk()
    app = CSVBatchProcessor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
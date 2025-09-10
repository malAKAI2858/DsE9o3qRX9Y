# 代码生成时间: 2025-09-10 12:15:44
import tkinter as tk
from tkinter import messagebox, scrolledtext
import json

"""
API响应格式化工具，使用Python和Tkinter框架创建。
这个程序允许用户输入JSON格式的API响应，并将其格式化为更易读的形式。
"""

class ApiResponseFormatter:
    """API响应格式化工具的主要类。"""
    def __init__(self, root):
        """初始化GUI界面。"""
        self.root = root
        self.root.title("API响应格式化工具")

        # 创建输入框
        self.input_label = tk.Label(root, text="请输入API响应：")
        self.input_label.pack()
        self.input_text = scrolledtext.ScrolledText(root, width=60, height=10)
        self.input_text.pack()

        # 创建格式化按钮
        self.format_button = tk.Button(root, text="格式化", command=self.format_response)
        self.format_button.pack()

        # 创建输出框
        self.output_label = tk.Label(root, text="格式化后的API响应：")
        self.output_label.pack()
        self.output_text = scrolledtext.ScrolledText(root, width=60, height=10)
        self.output_text.pack()

    def format_response(self):
        """格式化输入的API响应。"""
        try:
            # 从输入框获取JSON字符串
            json_str = self.input_text.get("1.0", "end-1c")
            # 尝试解析JSON字符串
            json_obj = json.loads(json_str)
            # 格式化JSON对象并返回格式化后的字符串
            formatted_json = json.dumps(json_obj, indent=4)
            # 将格式化后的字符串显示在输出框中
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", formatted_json)
        except json.JSONDecodeError as e:
            # 如果解析JSON字符串失败，显示错误信息
            messagebox.showerror("错误", f"解析JSON失败：{e}")

def main():
    """程序的主入口。"""
    root = tk.Tk()
    app = ApiResponseFormatter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
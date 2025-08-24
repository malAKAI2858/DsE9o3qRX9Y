# 代码生成时间: 2025-08-24 15:40:28
import tkinter as tk
from tkinter import messagebox

# 导入用于HTML实体编码的模块
import html

class XSSProtectionApp:
    """
    一个简单的Tkinter应用，用于演示XSS攻击防护。
    """
    def __init__(self, master):
        self.master = master
        self.master.title("XSS Attack Protection")
        
        # 用户输入框
        self.input_label = tk.Label(master, text="Enter HTML: ")
        self.input_label.pack()
        self.input_text = tk.Text(master, height=5, width=40)
        self.input_text.pack()
        
        # 清理并显示按钮
        self.clean_button = tk.Button(master, text="Clean HTML", command=self.clean_html)
        self.clean_button.pack()
        
        # 显示清理后的HTML
        self.output_label = tk.Label(master, text="Cleaned HTML: ")
        self.output_label.pack()
        self.output_text = tk.Text(master, height=5, width=40)
        self.output_text.pack()
        
    def clean_html(self):
        """
        清理HTML输入，防止XSS攻击。
        """
        try:
            # 获取用户输入
            raw_html = self.input_text.get("1.0", tk.END)
            
            # 使用html模块进行HTML实体编码
            cleaned_html = html.escape(raw_html)
            
            # 将清理后的HTML显示在输出框中
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, cleaned_html)
        except Exception as e:
            # 错误处理
            messagebox.showerror("Error", str(e))

# 创建主窗口并运行应用
if __name__ == "__main__":
    root = tk.Tk()
    app = XSSProtectionApp(root)
    root.mainloop()
# 代码生成时间: 2025-10-11 18:39:23
import tkinter as tk
from tkinter import colorchooser

# ColorSelectorApp 是一个使用Tkinter和colorchooser模块的颜色选择器应用
class ColorSelectorApp:
    def __init__(self, master):
        """初始化颜色选择器应用

        :param master: Tkinter窗口对象
        """
        self.master = master
        self.master.title("Color Selector")
        self.create_widgets()

    def create_widgets(self):
        """创建应用的界面元素"""
        # 创建一个按钮用于打开颜色选择对话框
        self.color_button = tk.Button(self.master, text="Choose a Color", command=self.choose_color)
        self.color_button.pack(pady=20)

        # 创建一个标签用于显示选择的颜色
        self.color_label = tk.Label(self.master, text="Selected Color: None", fg="black")
        self.color_label.pack(pady=20)

    def choose_color(self):
        """打开颜色选择对话框并更新标签显示选中的颜色

        :return: None
        """
        # 使用colorchooser.askcolor()函数获取颜色
        color_code, color_name = colorchooser.askcolor(title="Choose a Color")
        if color_code:
            # 更新标签的文本和前景色
            self.color_label.config(text=f"Selected Color: {color_name}", fg=color_code)
        else:
            # 如果用户取消选择，则重置为默认颜色
            self.color_label.config(text="Selected Color: None", fg="black")


# 主函数，运行颜色选择器应用
def main():
    try:
        # 创建Tkinter主窗口
        root = tk.Tk()
        # 创建ColorSelectorApp实例
        app = ColorSelectorApp(root)
        # 运行Tkinter事件循环
        root.mainloop()
    except Exception as e:
        # 错误处理
        print(f"An error occurred: {e}")

# 确保这段代码作为脚本运行时执行main()函数
if __name__ == '__main__':
    main()
# 代码生成时间: 2025-08-19 21:21:23
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# 图片尺寸批量调整器的类
class ImageResizer:
    def __init__(self, master):
        self.master = master
        self.master.title("图片尺寸批量调整器")
        self.setup_ui()

    def setup_ui(self):
        # 文件选择按钮
        self.open_button = tk.Button(self.master, text="选择文件夹", command=self.open_folder_dialog)
        self.open_button.pack()

        # 目标尺寸输入框
        self.width_label = tk.Label(self.master, text="宽度：")
        self.width_label.pack()
        self.width_entry = tk.Entry(self.master)
        self.width_entry.pack()

        self.height_label = tk.Label(self.master, text="高度：")
        self.height_label.pack()
        self.height_entry = tk.Entry(self.master)
        self.height_entry.pack()

        # 开始批量调整按钮
        self.start_button = tk.Button(self.master, text="开始调整", command=self.resize_images)
        self.start_button.pack()

    def open_folder_dialog(self):
        # 弹出文件夹选择对话框
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path
            messagebox.showinfo("选择成功", f"已选择文件夹：{self.folder_path}")
        else:
            messagebox.showerror("错误", "未选择任何文件夹")

    def resize_images(self):
        try:
            target_width = int(self.width_entry.get())
            target_height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的尺寸数值")
            return

        if not self.folder_path:
            messagebox.showerror("错误", "请先选择文件夹")
            return

        # 遍历文件夹中的所有图片文件
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if file.lower().endswith((".png", ".jpg", ".jpeg")):
                    try:
                        img_path = os.path.join(root, file)
                        img = Image.open(img_path)
                        # 调整图片尺寸
                        img = img.resize((target_width, target_height), Image.ANTIALIAS)
                        # 保存调整后的图片
                        img.save(img_path)
                        messagebox.showinfo("进度", f"已调整：{file}")
                    except Exception as e:
                        messagebox.showerror("错误", f"调整图片 {file} 时出错：{str(e)}")

    def run(self):
        self.master.mainloop()

# 创建Tkinter主窗口并运行
root = tk.Tk()
app = ImageResizer(root)
app.run()
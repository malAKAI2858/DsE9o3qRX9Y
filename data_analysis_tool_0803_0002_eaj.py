# 代码生成时间: 2025-08-03 00:02:17
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""
数据统计分析器，使用Python和Tkinter框架创建。
该程序允许用户加载数据文件，计算基本统计数据，并绘制图表。
"""

class DataAnalysisTool:
    def __init__(self, root):
        """初始化界面"""
        self.root = root
        self.root.title("数据统计分析器")
        self.root.geometry("800x600")

        # 创建菜单栏
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        self.file_menu.add_command(label="打开", command=self.load_data)
        self.file_menu.add_command(label="退出", command=self.root.quit)

        # 创建标签和文本框用于显示数据
        self.label = tk.Label(self.root, text="无数据")
        self.label.pack()
        self.text_area = tk.Text(self.root, height=20, width=80)
        self.text_area.pack()

        # 创建绘图区域
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def load_data(self):
        "
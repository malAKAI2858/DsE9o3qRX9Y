# 代码生成时间: 2025-09-10 21:43:16
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""
统计数据分析器，使用TKINTER框架创建GUI界面，实现数据文件的加载、统计分析和图表展示功能。
"""

class DataAnalysisStatistics:
    def __init__(self, root):
        """
        初始化GUI界面。
        :param root: Tkinter的根窗口对象。
        """
        self.root = root
        self.root.title("统计数据分析器")
        self.root.geometry("800x600")

        # 创建菜单栏
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="加载数据", command=self.load_data)
        self.file_menu.add_command(label="退出", command=self.root.quit)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # 创建数据加载状态标签
        self.status_label = tk.Label(self.root, text="未加载数据", font=("Arial", 12))
        self.status_label.pack()

        # 创建绘图区域
        self.fig, self.ax = plt.subplots()
        self.plot_canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.plot_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def load_data(self):
        "
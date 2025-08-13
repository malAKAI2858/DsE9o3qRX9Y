# 代码生成时间: 2025-08-13 09:19:09
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""
Interactive Chart Generator

This program allows users to select a CSV file, specify chart type,
and generate an interactive chart.

Attributes:
    - root (tk.Tk): The main application window.
    - file_path (str): The path to the selected CSV file.
    - df (pd.DataFrame): The data from the selected CSV file.
    - chart_type (str): The type of chart to generate.
    
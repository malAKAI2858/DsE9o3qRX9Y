# 代码生成时间: 2025-10-10 01:37:38
import tkinter as tk
from math import exp, sqrt

# 定义Black-Scholes期权定价模型函数
def black_scholes(call_price, put_price, s, k, t, r, sigma):
    """
    Black-Scholes模型计算期权价格。
    
    参数：
    call_price (float): 看涨期权的价格。
    put_price (float): 看跌期权的价格。
    s (float): 当前股票价格。
    k (float): 执行价格。
    t (float): 期权到期时间（年）。
    r (float): 无风险利率。
    sigma (float): 股票年化波动率。
    """
    d1 = (np.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    
    call = (s * exp(-r * t) * norm.cdf(d1) - k * exp(-r * t) * norm.cdf(d2))
    put = (k * exp(-r * t) * norm.cdf(-1 * d2) - s * exp(-r * t) * norm.cdf(-1 * d1))
    
    return call, put

# 导入NumPy和SciPy库
import numpy as np
from scipy.stats import norm

# 创建主窗口
root = tk.Tk()
root.title('Option Pricing Model')

# 设置窗口大小
root.geometry('600x400')

# 创建标签和输入框
tk.Label(root, text='Current Stock Price:').grid(row=0, column=0)
tk.Label(root, text='Strike Price:').grid(row=1, column=0)
tk.Label(root, text='Time to Expiration (years):').grid(row=2, column=0)
tk.Label(root, text='Risk-Free Rate:').grid(row=3, column=0)
tk.Label(root, text='Volatility:').grid(row=4, column=0)

s = tk.StringVar()
k = tk.StringVar()
t = tk.StringVar()
r = tk.StringVar()
sigma = tk.StringVar()

tk.Entry(root, textvariable=s).grid(row=0, column=1)
tk.Entry(root, textvariable=k).grid(row=1, column=1)
tk.Entry(root, textvariable=t).grid(row=2, column=1)
tk.Entry(root, textvariable=r).grid(row=3, column=1)
tk.Entry(root, textvariable=sigma).grid(row=4, column=1)

# 创建按钮，点击时计算期权价格
def calculate():
    try:
        s = float(s.get())
        k = float(k.get())
        t = float(t.get())
        r = float(r.get())
        sigma = float(sigma.get())
        call, put = black_scholes(0, 0, s, k, t, r, sigma)
        
        call_result.set(f'{call:.2f}')
        put_result.set(f'{put:.2f}')
    except ValueError:
        call_result.set('Invalid input')
        put_result.set('Invalid input')

calculate_button = tk.Button(root, text='Calculate', command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2)

# 创建标签显示结果
call_result = tk.StringVar()
put_result = tk.StringVar()
tk.Label(root, textvariable=call_result).grid(row=6, column=0)
tk.Label(root, textvariable=put_result).grid(row=6, column=1)

# 运行主循环
root.mainloop()
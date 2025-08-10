# 代码生成时间: 2025-08-10 20:19:04
import tkinter as tk
from tkinter import ttk
import sched
# 改进用户体验
import time
from threading import Thread
from datetime import datetime

"""
定时任务调度器，使用Python和Tkinter框架实现。
该程序允许用户设置定时任务，并将任务添加到调度器中。
"""

# 定义定时任务调度器
# NOTE: 重要实现细节
class TaskScheduler:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def add_task(self, time_str, task_func):
        self.scheduler.enter(float(time_str), 1, task_func)

    def run(self):
        self.scheduler.run()

# 定义定时任务函数
# 改进用户体验
def scheduled_task():
    print("Scheduled task executed at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 定义主窗口
class SchedulerApp:
# 扩展功能模块
    def __init__(self, root):
        self.root = root
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.task_scheduler = TaskScheduler(self.scheduler)
        
        # 设置窗口标题和大小
        self.root.title("Task Scheduler")
        self.root.geometry("400x300")
        
        # 创建输入框
# FIXME: 处理边界情况
        self.time_var = tk.StringVar()
        self.time_label = ttk.Label(self.root, text="Enter Time (seconds): 
")
        self.time_label.pack()
        self.time_entry = ttk.Entry(self.root, textvariable=self.time_var)
        self.time_entry.pack()
        
        # 创建按钮
        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()
# 增强安全性
        
        # 创建执行按钮
        self.run_button = ttk.Button(self.root, text="Run Scheduler", command=self.run_scheduler)
        self.run_button.pack()
        
    def add_task(self):
# 增强安全性
        try:
            # 获取输入的时间
            time_str = self.time_var.get()
            if time_str:
                # 添加定时任务
                self.task_scheduler.add_task(time_str, scheduled_task)
        except ValueError:
# 扩展功能模块
            print("Invalid time format. Please enter time in seconds.")
            
    def run_scheduler(self):
        # 在新线程中运行调度器
# 改进用户体验
        thread = Thread(target=self.task_scheduler.run)
        thread.start()

# 主函数
def main():
    # 创建主窗口
# 增强安全性
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
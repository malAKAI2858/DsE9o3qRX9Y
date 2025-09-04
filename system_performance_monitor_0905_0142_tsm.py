# 代码生成时间: 2025-09-05 01:42:13
import tkinter as tk
from tkinter import ttk
import psutil
import threading


# 系统性能监控工具类
class SystemPerformanceMonitor:
    def __init__(self, root):
        """初始化监控工具界面"""
        self.root = root
        self.root.title("系统性能监控工具")

        # 创建标签显示CPU、内存和磁盘的信息
        self.cpu_label = ttk.Label(root, text="CPU使用率: 0%")
        self.cpu_label.pack(pady=10)

        self.memory_label = ttk.Label(root, text="内存使用率: 0%")
        self.memory_label.pack(pady=10)

        self.disk_label = ttk.Label(root, text="磁盘使用率: 0%")
        self.disk_label.pack(pady=10)

        # 开始监控
        self.start_monitoring()

    def get_cpu_usage(self):
        """获取CPU使用率"""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        """获取内存使用率"""
        memory = psutil.virtual_memory()
        return memory.percent

    def get_disk_usage(self):
        """获取磁盘使用率"""
        disk = psutil.disk_usage('/')
        return disk.percent

    def update_labels(self):
        """更新界面标签的显示"""
        cpu_usage = self.get_cpu_usage()
        memory_usage = self.get_memory_usage()
        disk_usage = self.get_disk_usage()

        self.cpu_label.config(text=f"CPU使用率: {cpu_usage}%")
        self.memory_label.config(text=f"内存使用率: {memory_usage}%")
        self.disk_label.config(text=f"磁盘使用率: {disk_usage}%")

    def start_monitoring(self):
        """开始监控"""
        self.update_labels()
        self.root.after(1000, self.start_monitoring)

    def run(self):
        """运行监控工具"""
        self.root.mainloop()


# 主函数
def main():
    """创建Tkinter窗口并运行监控工具"""
    root = tk.Tk()
    monitor = SystemPerformanceMonitor(root)
    monitor.run()

if __name__ == '__main__':
    """程序入口"""
    main()
# 代码生成时间: 2025-09-23 01:08:41
import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time
# 扩展功能模块

"""
系统性能监控工具
"""

class SystemMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("系统性能监控工具")

        # 创建标签
        self.label_cpu = ttk.Label(root, text="CPU 使用率: 0%")
        self.label_mem = ttk.Label(root, text="内存使用率: 0%")
        self.label_disk = ttk.Label(root, text="磁盘使用率: 0%")

        # 布局标签
        self.label_cpu.grid(row=0, column=0)
# TODO: 优化性能
        self.label_mem.grid(row=1, column=0)
        self.label_disk.grid(row=2, column=0)

        # 启动监控线程
        self.monitoring_thread = threading.Thread(target=self.monitor_system)
        self.monitoring_thread.start()

    def monitor_system(self):
        """监控系统性能"""
        while True:
            try:
                # 获取CPU使用率
# 优化算法效率
                cpu_usage = psutil.cpu_percent(interval=1)
                self.label_cpu.config(text=f"CPU 使用率: {cpu_usage}%")
# 扩展功能模块

                # 获取内存使用率
                mem = psutil.virtual_memory()
# 扩展功能模块
                mem_usage = mem.percent
                self.label_mem.config(text=f"内存使用率: {mem_usage}%")

                # 获取磁盘使用率
                disk_usage = psutil.disk_usage('/').percent
# FIXME: 处理边界情况
                self.label_disk.config(text=f"磁盘使用率: {disk_usage}%")

                # 每秒更新一次
# FIXME: 处理边界情况
                time.sleep(1)

            except Exception as e:
                print(f"监控系统性能出错: {e}")
                break

    def start(self):
        """启动GUI主循环"""
        self.root.mainloop()

def main():
    """主函数"""
    root = tk.Tk()
# FIXME: 处理边界情况
    app = SystemMonitor(root)
    app.start()

if __name__ == '__main__':
# 增强安全性
    main()
# 代码生成时间: 2025-09-21 01:45:10
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import json
import datetime

# 测试报告生成器类
class TestReportGenerator:
    def __init__(self, master):
        # 初始化主窗口
        self.master = master
        self.master.title('测试报告生成器')
        self.master.geometry('400x300')

        # 添加按钮，选择测试数据文件
        self.choose_file_button = tk.Button(master, text='选择测试数据文件', command=self.choose_file)
        self.choose_file_button.pack(pady=10)

        # 添加按钮，生成测试报告
        self.generate_report_button = tk.Button(master, text='生成测试报告', command=self.generate_report)
        self.generate_report_button.pack(pady=10)

        # 测试数据文件路径
        self.file_path = ''

    def choose_file(self):
        # 选择测试数据文件
        self.file_path = filedialog.askopenfilename(filetypes=[('JSON files', '*.json')])
        if self.file_path:
            messagebox.showinfo('文件选择', '文件选择成功')
        else:
            messagebox.showwarning('文件选择', '未选择任何文件')

    def generate_report(self):
        # 生成测试报告
        try:
            if not self.file_path:
                messagebox.showerror('错误', '请先选择测试数据文件')
                return
            
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                
            report_title = data.get('report_title', '测试报告')
            report_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            report_content = data.get('report_content', [])
            
            # 生成测试报告内容
            report = f"报告标题：{report_title}
报告日期：{report_date}
"
            for item in report_content:
                report += f"{item['test_case']}: {item['result']}
"
                
            # 保存测试报告到文件
            report_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
            if report_file_path:
                with open(report_file_path, 'w') as file:
                    file.write(report)
                messagebox.showinfo('报告生成', '测试报告生成成功')
            else:
                messagebox.showwarning('报告生成', '未保存测试报告')
        except Exception as e:
            messagebox.showerror('错误', str(e))

# 主函数
def main():
    root = tk.Tk()
    app = TestReportGenerator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
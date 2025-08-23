# 代码生成时间: 2025-08-23 16:19:54
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
文件夹结构整理器

这个程序提供了一个图形界面，允许用户选择一个文件夹，
然后自动将文件夹中的文件按照扩展名分类到子文件夹中。
"""

class FolderStructureOrganizer:
    def __init__(self, root):
        """
        初始化界面
        :param root: 根窗口
        """
        self.root = root
        self.root.title('文件夹结构整理器')
        
        # 创建按钮
        self.button_select_folder = tk.Button(root, text='选择文件夹', command=self.select_folder)
        self.button_select_folder.pack()
        
        self.button_organize = tk.Button(root, text='整理文件夹', command=self.organize_folder, state='disabled')
        self.button_organize.pack()
        
        self.folder_path = ''

    def select_folder(self):
        """
        选择文件夹
        """
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.button_organize['state'] = 'normal'
        else:
            self.button_organize['state'] = 'disabled'
        
    def organize_folder(self):
        """
        整理文件夹
        """
        if not self.folder_path:
            messagebox.showerror('错误', '请先选择一个文件夹')
            return
        
        try:
            # 遍历文件夹中的所有文件
            for file_name in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file_name)
                
                # 获取文件扩展名
                if os.path.isfile(file_path):
                    extension = os.path.splitext(file_name)[1]
                    
                    # 创建以扩展名命名的子文件夹
                    folder_name = extension[1:]  # 去掉点
                    folder_path = os.path.join(self.folder_path, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    # 移动文件到子文件夹
                    os.rename(file_path, os.path.join(folder_path, file_name))
            messagebox.showinfo('成功', '文件夹整理完成')
        except Exception as e:
            messagebox.showerror('错误', f'发生错误: {str(e)}')

    def run(self):
        """
        运行主循环
        """
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    organizer = FolderStructureOrganizer(root)
    organizer.run()
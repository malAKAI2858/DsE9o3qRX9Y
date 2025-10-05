# 代码生成时间: 2025-10-06 02:36:27
import tkinter as tk
from tkinter import messagebox
import sqlite3

# 函数：初始化数据库
def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 创建时序数据库表
    cursor.execute('''CREATE TABLE IF NOT EXISTS time_series
                    (date TEXT, value REAL)''')
    conn.commit()
    conn.close()

# 函数：添加数据到时序数据库
def add_data(db_path, date, value):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO time_series (date, value) VALUES (?, ?)''', (date, value))
        conn.commit()
    except sqlite3.IntegrityError as e:
        messagebox.showerror('Error', f"Could not add data: {e}")
    finally:
        conn.close()

# 函数：从时序数据库读取数据
def read_data(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM time_series')
    data = cursor.fetchall()
    conn.close()
    return data

# 函数：更新时序数据库中的数据
def update_data(db_path, date, new_value):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('''UPDATE time_series SET value = ? WHERE date = ?''', (new_value, date))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror('Error', f"Could not update data: {e}")
    finally:
        conn.close()

# 函数：删除时序数据库中的数据
def delete_data(db_path, date):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('''DELETE FROM time_series WHERE date = ?''', (date,))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror('Error', f"Could not delete data: {e}")
    finally:
        conn.close()

# 函数：创建主窗口
def create_main_window():
    root = tk.Tk()
    root.title('Time Series DB Tool')

    # 数据库路径输入框
    db_path_label = tk.Label(root, text='Database Path:')
    db_path_label.pack()
    db_path_entry = tk.Entry(root)
    db_path_entry.pack()

    # 添加数据按钮
    add_button = tk.Button(root, text='Add Data', command=lambda: add_data(db_path_entry.get(), '2023-04-01', 100))
    add_button.pack()

    # 读取数据按钮
    read_button = tk.Button(root, text='Read Data', command=lambda: read_data_button_pressed(db_path_entry.get()))
    read_button.pack()

    # 更新数据按钮
    update_button = tk.Button(root, text='Update Data', command=lambda: update_data(db_path_entry.get(), '2023-04-01', 200))
    update_button.pack()

    # 删除数据按钮
    delete_button = tk.Button(root, text='Delete Data', command=lambda: delete_data(db_path_entry.get(), '2023-04-01'))
    delete_button.pack()

    root.mainloop()

# 函数：处理读取数据按钮的点击事件
def read_data_button_pressed(db_path):
    try:
        data = read_data(db_path)
        messagebox.showinfo('Data', data)
    except sqlite3.Error as e:
        messagebox.showerror('Error', f"Could not read data: {e}")

# 主函数
def main():
    create_main_window()

if __name__ == '__main__':
    main()
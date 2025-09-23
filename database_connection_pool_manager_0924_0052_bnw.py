# 代码生成时间: 2025-09-24 00:52:52
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2
import psycopg2.pool

# 数据库连接池管理类
class DBConnectionPoolManager:
    def __init__(self, minconn, maxconn, host, dbname, user, password):
        """
        初始化数据库连接池。

        :param minconn: 连接池最小连接数
        :param maxconn: 连接池最大连接数
        :param host: 数据库主机地址
        :param dbname: 数据库名称
        :param user: 数据库用户名
        :param password: 数据库密码
        """
        self.minconn = minconn
        self.maxconn = maxconn
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.pool = psycopg2.pool.SimpleConnectionPool(
            minconn, maxconn,
            user=user,
            password=password,
            host=host,
            port='5432',
            dbname=dbname)

    def get_connection(self):
        """
        从连接池获取一个数据库连接。

        :return: 数据库连接对象
        """
        try:
            conn = self.pool.getconn()
            return conn
        except psycopg2.Error as e:
            messagebox.showerror("数据库连接失败", str(e))
            return None

    def release_connection(self, conn):
        """
        释放数据库连接。

        :param conn: 需要释放的数据库连接对象
        """
        try:
            self.pool.putconn(conn)
        except psycopg2.Error as e:
            messagebox.showerror("释放连接失败", str(e))

# Tkinter GUI 界面
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('数据库连接池管理')
        self.geometry('400x300')
        self.create_widgets()

    def create_widgets(self):
        # 连接池参数设置
        tk.Label(self, text='最小连接数:').grid(column=0, row=0)
        self.minconn_entry = tk.Entry(self)
        self.minconn_entry.grid(column=1, row=0)

        tk.Label(self, text='最大连接数:').grid(column=0, row=1)
        self.maxconn_entry = tk.Entry(self)
        self.maxconn_entry.grid(column=1, row=1)

        tk.Label(self, text='数据库主机地址:').grid(column=0, row=2)
        self.host_entry = tk.Entry(self)
        self.host_entry.grid(column=1, row=2)

        tk.Label(self, text='数据库名称:').grid(column=0, row=3)
        self.dbname_entry = tk.Entry(self)
        self.dbname_entry.grid(column=1, row=3)

        tk.Label(self, text='数据库用户名:').grid(column=0, row=4)
        self.user_entry = tk.Entry(self)
        self.user_entry.grid(column=1, row=4)

        tk.Label(self, text='数据库密码:').grid(column=0, row=5)
        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=5)

        # 按钮
        tk.Button(self, text='创建连接池', command=self.create_pool).grid(column=0, row=6)
        tk.Button(self, text='获取连接', command=self.get_connection).grid(column=1, row=6)
        tk.Button(self, text='释放连接', command=self.release_connection).grid(column=2, row=6)

    def create_pool(self):
        minconn = int(self.minconn_entry.get())
        maxconn = int(self.maxconn_entry.get())
        host = self.host_entry.get()
        dbname = self.dbname_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()

        try:
            self.pool_manager = DBConnectionPoolManager(minconn, maxconn, host, dbname, user, password)
            messagebox.showinfo("连接池创建成功", "连接池已成功创建")
        except Exception as e:
            messagebox.showerror("连接池创建失败", str(e))

    def get_connection(self):
        if not hasattr(self, 'pool_manager'):
            messagebox.showerror("错误", "请先创建连接池")
            return

        conn = self.pool_manager.get_connection()
        if conn:
            messagebox.showinfo("获取连接成功", "成功获取数据库连接")

    def release_connection(self):
        if not hasattr(self, 'pool_manager'):
            messagebox.showerror("错误", "请先创建连接池")
            return

        conn = self.pool_manager.get_connection()
        if conn:
            self.pool_manager.release_connection(conn)
            messagebox.showinfo("释放连接成功", "成功释放数据库连接")

if __name__ == '__main__':
    app = App()
    app.mainloop()
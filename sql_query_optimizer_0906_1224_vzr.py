# 代码生成时间: 2025-09-06 12:24:54
import tkinter as tk
from tkinter import messagebox
import sqlite3

"""
SQL Query Optimizer GUI Application
This application provides a simple interface to optimize SQL queries.
"""

class SQLQueryOptimizer:
    def __init__(self, master):
        """Initialize the main window and its components."""
        self.master = master
        master.title("SQL Query Optimizer")

        # Create frames
        self.top_frame = tk.Frame(master)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create input text area for SQL query
        self.query_label = tk.Label(self.top_frame, text="Enter SQL Query: ")
        self.query_label.pack(side=tk.LEFT)

        self.query_text = tk.Text(self.top_frame, height=10, width=50)
        self.query_text.pack(side=tk.LEFT, fill=tk.X)

        # Create optimize button
        self.optimize_button = tk.Button(self.bottom_frame, text="Optimize Query", command=self.optimize_query)
        self.optimize_button.pack(side=tk.LEFT, padx=10)

        # Create result text area for optimized query
        self.result_label = tk.Label(self.bottom_frame, text="Optimized Query: ")
        self.result_label.pack(side=tk.LEFT)

        self.result_text = tk.Text(self.bottom_frame, height=10, width=50)
        self.result_text.pack(side=tk.LEFT, fill=tk.X)

    def connect_to_database(self):
        """Connect to the SQLite database."""
        try:
            self.conn = sqlite3.connect('example.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
            self.conn = None
            self.cursor = None

    def optimize_query(self):
        """Optimize the SQL query entered by the user."""
        query = self.query_text.get("1.0", tk.END).strip()

        # Check if the query is empty
        if not query:
            messagebox.showinfo("Info", "Please enter a SQL query.")
            return

        try:
            # Connect to the database
            self.connect_to_database()

            # Execute the query and analyze the execution plan
            self.cursor.execute("EXPLAIN QUERY PLAN " + query)
            results = self.cursor.fetchall()

            # Get the optimized query from the execution plan
            optimized_query = ""
            for row in results:
                optimized_query += str(row) + "
"

            # Update the result text area with the optimized query
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", optimized_query)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            # Close the database connection
            if self.conn:
                self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = SQLQueryOptimizer(root)
    root.mainloop()
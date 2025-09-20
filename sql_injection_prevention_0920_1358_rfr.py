# 代码生成时间: 2025-09-20 13:58:43
import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        messagebox.showerror("Connection error", f"Error connecting to database: {e}")
    return conn

def execute_query(conn, query, params=None):
    """ execute a query with optional parameters and prevent SQL injection """
    try:
        if params:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
        else:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        messagebox.showerror("Query error", f"Error executing query: {e}")

def main():
    # Database file
    db_file = "example.db"
    # Establish database connection
    conn = create_connection(db_file)
    if conn is not None:
        # Create a table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )"""
        execute_query(conn, create_table_query)
        
        # Example query to prevent SQL injection
        # Using parameterized queries to prevent SQL injection
        search_query = "SELECT * FROM users WHERE username = ?"
        search_username = "example_user"
        execute_query(conn, search_query, (search_username,))
        
        # Close connection
        conn.close()
    else:
        messagebox.showerror("Connection error", "Failed to connect to database")

def run_app():
    root = tk.Tk()
    root.withdraw()  # hide the main window
    main()
    root.destroy()
if __name__ == "__main__":
    run_app()
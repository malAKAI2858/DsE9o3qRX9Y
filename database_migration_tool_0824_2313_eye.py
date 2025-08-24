# 代码生成时间: 2025-08-24 23:13:03
import tkinter as tk
from tkinter import messagebox
import psycopg2
import os

"""
Database Migration Tool
A simple GUI application to migrate databases using psycopg2.
"""

class DatabaseMigrationTool:
    def __init__(self, master):
        """Initialize the main window and components."""
        self.master = master
        self.master.title('Database Migration Tool')

        # Create labels and entry fields for database connection info
        tk.Label(master, text='Source Database Host:').grid(row=0, column=0)
        self.source_host = tk.Entry(master)
        self.source_host.grid(row=0, column=1)

        tk.Label(master, text='Source Database Name:').grid(row=1, column=0)
        self.source_name = tk.Entry(master)
        self.source_name.grid(row=1, column=1)

        tk.Label(master, text='Source Database User:').grid(row=2, column=0)
        self.source_user = tk.Entry(master)
        self.source_user.grid(row=2, column=1)

        tk.Label(master, text='Source Database Password:').grid(row=3, column=0)
        self.source_password = tk.Entry(master, show='*')
        self.source_password.grid(row=3, column=1)

        tk.Label(master, text='Destination Database Host:').grid(row=4, column=0)
        self.dest_host = tk.Entry(master)
        self.dest_host.grid(row=4, column=1)

        tk.Label(master, text='Destination Database Name:').grid(row=5, column=0)
        self.dest_name = tk.Entry(master)
        self.dest_name.grid(row=5, column=1)

        tk.Label(master, text='Destination Database User:').grid(row=6, column=0)
        self.dest_user = tk.Entry(master)
        self.dest_user.grid(row=6, column=1)

        tk.Label(master, text='Destination Database Password:').grid(row=7, column=0)
        self.dest_password = tk.Entry(master, show='*')
        self.dest_password.grid(row=7, column=1)

        # Create a button to perform the migration
        self.migrate_button = tk.Button(master, text='Migrate', command=self.migrate)
        self.migrate_button.grid(row=8, column=0, columnspan=2)

    def migrate(self):
        """Migrate data from source to destination database."""
        # Extract connection info from entry fields
        source = {
            'host': self.source_host.get(),
            'database': self.source_name.get(),
            'user': self.source_user.get(),
            'password': self.source_password.get()
        }

        destination = {
            'host': self.dest_host.get(),
            'database': self.dest_name.get(),
            'user': self.dest_user.get(),
            'password': self.dest_password.get()
        }

        try:
            # Connect to source and destination databases
            with psycopg2.connect(**source) as src_conn:
                with psycopg2.connect(**destination) as dest_conn:
                    # Perform migration logic here
                    # For demonstration purposes, we'll just copy all tables
                    src_cursor = src_conn.cursor()
                    dest_cursor = dest_conn.cursor()

                    # Get list of tables from source database
                    src_cursor.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\'')
                    tables = src_cursor.fetchall()

                    for table in tables:
                        table_name = table[0]
                        # Copy data from source to destination
                        src_cursor.execute(f'SELECT * FROM {table_name}')
                        rows = src_cursor.fetchall()

                        # Create table in destination if not exists
                        dest_cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, data TEXT)')

                        # Insert data into destination table
                        for row in rows:
                            dest_cursor.execute(f'INSERT INTO {table_name} (data) VALUES (%s)', (row[0],))

                    # Commit changes to destination database
                    dest_conn.commit()

            # Show success message
            messagebox.showinfo('Migration Successful', 'Data migration completed successfully.')

        except Exception as e:
            # Show error message if migration fails
            messagebox.showerror('Migration Failed', f'An error occurred: {str(e)}')

# Create the main window and pass it to the DatabaseMigrationTool class
root = tk.Tk()
app = DatabaseMigrationTool(root)

# Start the main loop
root.mainloop()
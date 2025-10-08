# 代码生成时间: 2025-10-09 02:06:29
import tkinter as tk
from tkinter import messagebox
import psutil
import socket
import logging

"""
Network Security Monitor
A simple network security monitoring application using Python and Tkinter.
It checks for network connections and displays the current status.
"""

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkSecurityMonitor:
    def __init__(self, master):
        self.master = master
        self.master.title('Network Security Monitor')
        self.master.geometry('400x200')
        
        # Create a label to display the status
        self.status_label = tk.Label(self.master, text='Checking network connections...', font=('Helvetica', 14))
        self.status_label.pack(pady=10)
        
        # Start monitoring
        self.monitor_network()
        
    def monitor_network(self):
        try:
            # Get current network connections
            connections = psutil.net_connections()
            self.update_status(len(connections))
        except Exception as e:
            logging.error(f'Error monitoring network connections: {e}')
            messagebox.showerror('Error', f'Failed to monitor network connections: {e}')
            
    def update_status(self, connection_count):
        # Update the status label
        if connection_count > 0:
            status_text = f'Active connections: {connection_count}'
        else:
            status_text = 'No active connections.'
        self.status_label.config(text=status_text)
        
        # Schedule the next check
        self.master.after(5000, self.monitor_network)

# Create the main window and pass it to the NetworkSecurityMonitor class
def main():
    root = tk.Tk()
    app = NetworkSecurityMonitor(root)
    root.mainloop()

if __name__ == '__main__':
    main()
# 代码生成时间: 2025-09-16 12:10:32
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading
import queue

"""
Web Content Scraper - A tkinter-based GUI application for scraping web content.
This program allows users to enter a URL and scrape the content of that webpage.

Features:
- Simple GUI with URL input and scrape button.
- Multi-threading to handle web scraping in a separate thread.
- Exception handling for robustness.
- Beautiful Soup for parsing HTML content.
"""

class WebContentScraper:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Content Scraper")
        self.url = ''
        self.q = queue.Queue()
        self.init_gui()

    def init_gui(self):
        # URL input field
        tk.Label(self.root, text="Enter URL:").grid(row=0, column=0)
        self.url_entry = tk.Entry(self.root)
        self.url_entry.grid(row=0, column=1)
        
        # Scrape button
        tk.Button(self.root, text="Scrape", command=self.start_scraping).grid(row=1, column=0, columnspan=2)
        
        # Content label
        self.content_label = tk.Label(self.root, text="")
        self.content_label.grid(row=2, column=0, columnspan=2)

    def start_scraping(self):
        # Get the URL from the input field
        self.url = self.url_entry.get()
        
        # Start the scraping thread
        threading.Thread(target=self.scrape_content, args=(self.url,)).start()

    def scrape_content(self, url):
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content using Beautiful Soup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Get the text content of the webpage
                text = soup.get_text()
                
                # Put the text content into the queue
                self.q.put(text)
            else:
                messagebox.showerror("Error", f"Failed to retrieve webpage. Status code: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_content(self):
        # Get the text content from the queue and update the label
        if not self.q.empty():
            text = self.q.get()
            self.content_label.config(text=text)

def main():
    root = tk.Tk()
    app = WebContentScraper(root)
    root.mainloop()

if __name__ == '__main__':
    main()
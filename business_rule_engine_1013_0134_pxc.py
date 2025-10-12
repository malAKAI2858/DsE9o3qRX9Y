# 代码生成时间: 2025-10-13 01:34:28
import tkinter as tk
from tkinter import messagebox

"""
Business Rule Engine GUI Application
This application allows users to define and execute business rules.
"""

class BusinessRuleEngine:
    """Class representing the business rule engine."""
    def __init__(self):
        self.rules = {}

    def add_rule(self, name, rule_function):
        """Add a rule to the engine."""
        self.rules[name] = rule_function

    def execute_rule(self, name, data):
        """Execute a rule with the given data."""
        if name in self.rules:
            try:
                return self.rules[name](data)
            except Exception as e:
                raise ValueError(f"Error executing rule '{name}': {e}")
        else:
            raise ValueError(f"Rule '{name}' not found.")

class RuleData:
    """Class representing data for a rule."""
    def __init__(self, input_data):
        self.data = input_data

class Application(tk.Tk):
    """The main application window."""
    def __init__(self):
        super().__init__()
        self.title('Business Rule Engine')
        self.engine = BusinessRuleEngine()
        self.create_widgets()

    def create_widgets(self):
        """Create the UI widgets."""
        # Rule Entry Frame
        self.rule_frame = tk.Frame(self)
        self.rule_frame.pack(pady=10)
        tk.Label(self.rule_frame, text='Rule Name:').pack(side=tk.LEFT)
        self.rule_name_entry = tk.Entry(self.rule_frame)
        self.rule_name_entry.pack(side=tk.LEFT, padx=10)
        tk.Button(self.rule_frame, text='Add Rule', command=self.add_rule).pack(side=tk.LEFT)

        # Input Data Frame
        self.data_frame = tk.Frame(self)
        self.data_frame.pack(pady=10)
        tk.Label(self.data_frame, text='Input Data:').pack(side=tk.LEFT)
        self.data_entry = tk.Entry(self.data_frame)
        self.data_entry.pack(side=tk.LEFT, padx=10)
        tk.Button(self.data_frame, text='Execute Rule', command=self.execute_rule).pack(side=tk.LEFT)

    def add_rule(self):
        """Add a rule to the business rule engine."""
        rule_name = self.rule_name_entry.get()
        if not rule_name:
            messagebox.showerror('Error', 'Please enter a rule name.')
            return
        # Example rule function
        def example_rule(data):
            return f'Rule {rule_name} executed with data: {data}'
        try:
            self.engine.add_rule(rule_name, example_rule)
            messagebox.showinfo('Success', 'Rule added successfully.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def execute_rule(self):
        """Execute a rule with the provided data."""
        rule_name = self.rule_name_entry.get()
        input_data = self.data_entry.get()
        if not rule_name or not input_data:
            messagebox.showerror('Error', 'Please enter a rule name and input data.')
            return
        try:
            result = self.engine.execute_rule(rule_name, RuleData(input_data))
            messagebox.showinfo('Result', result)
        except ValueError as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    app = Application()
    app.mainloop()
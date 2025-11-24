import json
import os
from datetime import datetime

class ExpenseTracker:

    def __init__(self):
        self.expenses=[]
        self.categories=["Food","Transport","Entertainment","Shopping","Bills","Education","Health","Other"]
        self.data_file="data/expenses.json"
        self.load_expenses()
    
    def display_menu(self):
        #Display the main menu
        print("\n"+"="*50)
        print("             SMART EXPENSE TRACKER")
        print("="*50)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Monthly Summary")
        print("5. Delete Expense")
        print("6. Exit")
        print("="*50)
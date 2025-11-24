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

    def get_user_choice(self):
        #Get and validate user input
        try:
            choice=int(input("Enter your choice (1-6): "))
            return choice
        except ValueError:
            print("Please enter a valid number!")
            return None
    
    def add_expense(self):
        #Add a new expense
        print("\n--- Add New Expense ---")   
        # Get expense description
        description=input("Enter expense description: ").strip()
        if not description:
            print("Description cannot be empty!")
            return   
        # Get amount with validation
        try:
            amount=float(input("Enter amount: ₹"))
            if amount<=0:
                print("Amount must be positive!")
                return
        except ValueError:
            print("Please enter a valid amount!")
            return     
        # Display categories
        print("\nExpense Categories:")
        for i,category in enumerate(self.categories,1):
            print(f"{i}. {category}")     
        # Get category choice
        try:
            cat_choice=int(input("Choose category (1-8): "))
            if 1<=cat_choice<=len(self.categories):
                category=self.categories[cat_choice - 1]
            else:
                print("Invalid category choice!")
                return
        except ValueError:
            print("Please enter a valid number!")
            return  
        # Get current date
        current_date=datetime.now().strftime("%Y-%m-%d %H:%M")    
        # Create expense dictionary
        expense = {
            'id': len(self.expenses) + 1,
            'description': description,
            'amount': amount,
            'category': category,
            'date': current_date
        }   
        # Add to expenses list
        self.expenses.append(expense)
        self.save_expenses() 
        print(f"Expense added successfully!")
        print(f"{description} - ₹{amount} - {category}")

    
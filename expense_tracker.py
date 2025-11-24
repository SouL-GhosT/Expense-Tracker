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

    def monthly_summary(self):
        #Show monthly expense summary
        print("\n--- Monthly Summary ---")  
        if not self.expenses:
            print("No expenses recorded yet!")
            return  
        # Group expenses by month
        monthly_data={}
        for expense in self.expenses:
            # Extract year-month from date (format: YYYY-MM)
            month_key=expense['date'][:7]  # Gets "YYYY-MM" 
            if month_key not in monthly_data:
                monthly_data[month_key]=[]
            monthly_data[month_key].append(expense)       
        # Display monthly summary
        print(f"{'Month':<10} {'Total Expenses':<15} {'Number of Expenses':<20}")
        print("-" * 50)    
        for month, expenses_list in monthly_data.items():
            total = sum(exp['amount'] for exp in expenses_list)
            count = len(expenses_list)
            print(f"{month:<10} ₹{total:<13.2f} {count:<20}")   
        # Category-wise breakdown for current month
        current_month=datetime.now().strftime("%Y-%m")
        current_month_expenses = monthly_data.get(current_month,[])    
        if current_month_expenses:
            print(f"\nCategory-wise breakdown for {current_month}:")
            category_totals = {}     
            for expense in current_month_expenses:
                category=expense['category']
                category_totals[category]=category_totals.get(category, 0) + expense['amount']     
            for category,total in category_totals.items():
                percentage=(total/sum(category_totals.values()))*100
                print(f"{category}: ₹{total:.2f} ({percentage:.1f}%)")

    def delete_expense(self):
        #Delete an expense by ID
        print("\n--- Delete Expense ---")   
        if not self.expenses:
            print("No expenses to delete!")
            return       
        self.view_all_expenses()
        try:
            expense_id=int(input("\nEnter expense ID to delete: "))
        except ValueError:
            print("Please enter a valid ID!")
            return    
        # Find and remove expense
        for i,expense in enumerate(self.expenses):
            if expense['id']==expense_id:
                deleted_expense=self.expenses.pop(i)
                # Update IDs for remaining expenses
                for j in range(i,len(self.expenses)):
                    self.expenses[j]['id']=j+1           
                self.save_expenses()
                print(f"Expense deleted: {deleted_expense['description']} - ₹{deleted_expense['amount']}")
                return  
        print("Expense ID not found!")
    
    def save_expenses(self):
        #Save expenses to JSON file
        try:
            # Create data directory if it doesn't exist
            os.makedirs(os.path.dirname(self.data_file),exist_ok=True)         
            with open(self.data_file,'w') as f:
                json.dump(self.expenses,f,indent=2)
        except Exception as e:
            print(f"Error saving expenses: {e}")
    
    def load_expenses(self):
        #Load expenses from JSON file
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file,'r') as f:
                    self.expenses=json.load(f)
        except Exception as e:
            print(f"Error loading expenses: {e}")
            self.expenses=[]
  
    def run(self):
        #Main program loop
        print("Welcome to Smart Expense Tracker!")
        print("Keep track of your daily expenses easily!")      
        while True:
            self.display_menu()
            choice=self.get_user_choice()     
            if choice==1:
                self.add_expense()
            elif choice==2:
                self.view_all_expenses()
            elif choice==3:
                self.view_by_category()
            elif choice==4:
                self.monthly_summary()
            elif choice==5:
                self.delete_expense()
            elif choice==6:
                print("\nSaving your expenses...")
                self.save_expenses()
                print("Thank you for using Smart Expense Tracker!")
                print("Goodbye!")
                break
            else:
                if choice is not None:
                    print("Invalid choice! Please enter 1-6.")         
            # Wait for user to press Enter before continuing
            input("\nPress Enter to continue...")

# Main program execution
if __name__=="__main__":
    tracker=ExpenseTracker()
    tracker.run()
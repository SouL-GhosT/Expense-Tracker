import os
import json
import tempfile
from expense_tracker import ExpenseTracker

def test_add_expense():
    #Test adding expenses
    print("Testing expense addition...") 
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w',delete=False,suffix='.json') as f:
        test_file=f.name 
    try:
        tracker=ExpenseTracker()
        tracker.data_file=test_file
        tracker.expenses=[] # Clear any existing expenses    
        # Test data
        test_expense={'id': 1,'description': 'Test Lunch','amount': 250.0,'category': 'Food','date': '2025-11-25 12:00'}    
        tracker.expenses.append(test_expense)
        tracker.save_expenses()   
        # Verify the expense was saved
        with open(test_file, 'r') as f:
            saved_data = json.load(f)
        assert len(saved_data) == 1
        assert saved_data[0]['description']=='Test Lunch'
        assert saved_data[0]['amount']==250.0
        assert saved_data[0]['category']=='Food'     
        print("Expense addition test passed!")    
    finally:
        # Clean up
        if os.path.exists(test_file):
            os.unlink(test_file)

def test_expense_categories():
    #Test expense categories
    print("Testing expense categories...")    
    tracker = ExpenseTracker() 
    # Check if default categories exist
    expected_categories = ["Food","Transport","Entertainment","Shopping","Bills","Education","Health","Other"]
    assert tracker.categories==expected_categories
    assert len(tracker.categories)==8
    print("Expense categories test passed!")

def test_file_operations():
    #Test saving and loading expenses
    print("Testing file operations...")   
    with tempfile.NamedTemporaryFile(mode='w',delete=False,suffix='.json') as f:
        test_file=f.name  
    try:
        tracker=ExpenseTracker()
        tracker.data_file = test_file   
        # Add test expenses
        test_expenses = [
            {
                'id': 1,
                'description': 'Movie',
                'amount': 300.0,
                'category': 'Entertainment',
                'date': '2025-11-25 18:00'
            },
            {
                'id': 2,
                'description': 'Bus Ticket',
                'amount': 50.0,
                'category': 'Transport',
                'date': '2025-11-25 08:00'
            }
        ]    
        tracker.expenses = test_expenses
        tracker.save_expenses()  
        # Create new tracker instance and load data
        new_tracker=ExpenseTracker()
        new_tracker.data_file=test_file
        new_tracker.load_expenses()    
        assert len(new_tracker.expenses)==2
        assert new_tracker.expenses[0]['description']=='Movie'
        assert new_tracker.expenses[1]['amount']==50.0
        print("File operations test passed!")     
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)

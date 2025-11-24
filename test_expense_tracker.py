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


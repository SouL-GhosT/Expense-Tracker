# Smart Expense Tracker 💰

**Simple effective expense tracking application built with Python, perfect for 1st year BTech students to learn programming fundamentals.**

Take control of your finances, one expense at a time!

 ## 📋 Overview
The Smart Expense Tracker is a Python-based application designed to help students and young professionals manage their daily expenses efficiently. Built with simplicity in mind, it provides an intuitive way to track spending, analyze patterns, and maintain financial awareness without complex setups or technical knowledge.

  - 🎯 Why This Project?
  - 🧮 Stop guessing where your money goes
  - 📊 Visualize your spending habits
  - 💰 Take control of your budget
  - 🎓 Perfect for students managing pocket money

## ✨ Features

### 🎯 Core Features
| Feature | Description | Status |
|---------|-------------|--------|
| **➕ Add Expenses** | Record expenses with categories and descriptions | ✅ |
| **👀 View All** | See complete expense history in formatted tables | ✅ |
| **🗂️ Category Filter** | Filter expenses by specific categories | ✅ |
| **📈 Monthly Reports** | View spending patterns by month | ✅ |
| **🗑️ Delete Expenses** | Remove incorrect or unwanted entries | ✅ |
| **💾 Auto-Save** | Automatic data persistence between sessions | ✅ |

### 🏷️ Expense Categories
| Category | Icon | Description |
|----------|------|-------------|
| **Food & Dining** | 🍕 | Meals, snacks, coffee, restaurants |
| **Transport** | 🚗 | Bus, train, fuel, taxi, flights |
| **Entertainment** | 🎬 | Movies, games, concerts, hobbies |
| **Shopping** | 🛍️ | Clothes, electronics, accessories |
| **Bills & Utilities** | 📠 | Rent, electricity, internet, phone |
| **Education** | 📚 | Books, courses, stationery, fees |
| **Health & Medical** | 🏥 | Medicine, doctor visits, fitness |
| **Other Expenses** | 📦 | Miscellaneous and uncategorized |

### 📊 Analytics Features
| Feature | Description | Benefit |
|---------|-------------|---------|
| **Monthly Summaries** | View spending by month with totals | Track trends over time |
| **Category Breakdown** | Percentage distribution by category | Identify spending patterns |
| **Expense Count** | Number of expenses per period | Understand frequency of spending |
| **Visual Reports** | Formatted tables and percentages | Easy-to-understand insights |

## 🛠️ Technologies & Tools

### 💻 Programming & Frameworks
| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.6+ |
| **JSON** | Data storage and persistence | Built-in |
| **datetime** | Date and time handling | Built-in |
| **os** | File system operations | Built-in |

## 🎨 Development Tools

  - VS Code - Recommended code editor
  - Git - Version control
  - Markdown - Documentation

## 📦 Dependencies

 ```python
    # No external dependencies required!
    # Uses only Python standard library:
    import json
    import os  
    from datetime import datetime
```

## 🚀 Installation & Setup

### Prerequisites

  - ✅ Python 3.6 or higher installed
  - ✅ Basic understanding of command line
  - ✅ Text editor (VS Code recommended)

### Step-by-Step Installation
   
#### 1. Download the Project
 ```bash
# Method 1: Clone repository (if using Git)
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

# Method 2: Download ZIP file
# Extract to your preferred location
```

#### 2. Verify Python Installation
```bash
# Check Python version
python --version
# Should show: Python 3.x.x

# If not installed, download from: https://python.org
```

#### 3. Run the Application
```bash
# Navigate to project directory
cd expense-tracker

# Run the main file
python expense_tracker.py
```

#### 4. First-Time Setup
- The application automatically creates necessary folders
- Data file will be generated on first expense addition
- No additional configuration required!

 ## 🎮 How to Use

### Getting Started
 1. Launch the application using the steps above
 2. Follow the menu prompts to navigate features
 3. Start adding expenses to build your financial history

### Sample Usage Flow
#### Adding Your First Expense:

```python
    Welcome to Smart Expense Tracker!
    ==================================================
            SMART EXPENSE TRACKER
    ==================================================
    1. Add New Expense
    2. View All Expenses
    3. View Expenses by Category
    4. Monthly Summary
    5. Delete Expense
    6. Exit
    ==================================================

    Enter your choice (1-6): 1

    --- Add New Expense ---
    Enter expense description: College textbooks
    Enter amount: ₹1200

    Expense Categories:
    1. Food
    2. Transport
    3. Entertainment
    4. Shopping
    5. Bills
    6. Education
    7. Health
    8. Other

    Choose category (1-8): 6

    Expense added successfully!
    College textbooks - ₹1200 - Education
```

 #### Viewing Monthly Summary:

    --- Monthly Summary ---
    Month      Total Expenses   Number of Expenses
    --------------------------------------------------
    2024-01    ₹4500.00        8
    2024-02    ₹3800.00        6

    Category-wise breakdown for 2024-02:
    Food: ₹1500.00 (39.5%)
    Education: ₹1200.00 (31.6%)
    Transport: ₹800.00 (21.1%)
    Other: ₹300.00 (7.9%)


## 🧪 Testing Instructions

### Manual Testing Guide
####  1. Basic Functionality Test
    # Test 1: Application Launch
    python expense_tracker.py
    # Expected: Menu displays without errors

    # Test 2: Add Expense
    # Choose option 1, enter valid data
    # Expected: Success message appears

    # Test 3: View Expenses  
    # Choose option 2
    # Expected: Expenses display in table format

#### 2. Input Validation Test 
- ✅ Test with empty descriptions
- ✅ Test with negative amounts
- ✅ Test with invalid category numbers
- ✅ Test with non-numeric amounts

#### 3. Data Persistence Test
- Add several expenses
- Exit the application (option 6)
- Restart the application
-  View expenses - they should persist

###  Automated Testing
```python
    python test_expense_tracker.py
```

 ## 📸 Application Screenshots

###  Main Menu
<img width="567" height="338" alt="Screenshot 2025-11-24 232006" src="https://github.com/user-attachments/assets/d3bda488-e1f5-4fa1-b69c-cf98a35f890f" />

###  Adding Expenses
<img width="574" height="875" alt="Screenshot 2025-11-24 232028" src="https://github.com/user-attachments/assets/9b4b07c0-4315-4f24-8780-9707c9f103ec" />
<img width="586" height="813" alt="Screenshot 2025-11-24 232054" src="https://github.com/user-attachments/assets/7679cc3e-4134-4937-906e-1c3c80904435" />

### Expense Listing
<img width="799" height="563" alt="Screenshot 2025-11-24 232123" src="https://github.com/user-attachments/assets/8888b3b0-4812-428f-be2e-3af1ee9cb702" />

### Monthly Report
<img width="590" height="675" alt="Screenshot 2025-11-24 232854" src="https://github.com/user-attachments/assets/bf03077c-8ff6-4abe-b306-f9d27981c8e4" />

## 🐛 Troubleshooting

### Common Issues & Solutions

| Problem | Solution | Severity |
|---------|----------|----------|
| **"Python not found"** | Install Python from python.org | 🔴 Critical |
| **Permission errors** | Run as administrator or check folder permissions | 🔴 Critical |
| **Data not saving** | Check if data/ folder is created in project directory | 🟡 Medium |
| **Import errors** | Ensure all files are in same directory | 🟡 Medium |

###  Getting Help
1. Check this README for solutions
2. Verify Python installation
3. Ensure all project files are present
4. Check file permissions in project directory

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
- 🐛 Bug Reports: Describe the issue and steps to reproduce
- 💡 Feature Requests: Suggest new features or improvements
- 📚 Documentation: Help improve this documentation

### Development
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Standards
- Follow PEP 8 style guide
- Add comments for complex logic
- Include error handling
- Write clear commit messages

## 🎓 Learning Resources

### Python Concepts Demonstrated
- Object-Oriented Programming
- File Handling (JSON)
- Data Structures (Lists, Dictionaries)
- Error Handling
- User Input Validation
- Date/Time Operations

### Next Steps for Learning
- Add graphical user interface (GUI)
- Implement database storage
- Create web version with Flask/Django
- Add data visualization with charts
- Develop mobile app version

## 📞 Support & Contact

### Need Help?
- 📧 Email: sakchamshaw1234@gmail.com
- 💬 Issues: [GitHub Issues Page]
- 📚 Documentation: Check this README first

Project Maintainers
SouL GhosT - Lead Developer

## 🚀 Ready to Start?

    # Clone and run today!
    git clone https://github.com/SouL-GhosT/expense-tracker.git
    cd expense-tracker
    python expense_tracker.py

 **Start tracking your expenses and take control of your finances! 💰**

Built with ❤️ for the student community

**⭐ Don't forget to star the repository if you find this helpful!**

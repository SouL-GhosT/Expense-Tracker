# Smart Expense Tracker - Project Report

## 1. Introduction
The Smart Expense Tracker is a Python-based application that helps users track their daily expenses. It's designed specifically for 1st year BTech students to understand programming fundamentals while building a useful real-world application.

## 2. Problem Statement
Many students struggle with managing their pocket money and daily expenses. Manual tracking using notebooks or memory is inefficient and error-prone. There's a need for a simple digital solution that helps track spending habits.

## 3. Functional Requirements
- **Add New Expense**: Record expense with description, amount, category, and date
- **View All Expenses**: Display all recorded expenses in tabular format
- **Category Filter**: View expenses filtered by specific categories
- **Monthly Summary**: Show spending patterns by month and category
- **Delete Expense**: Remove unwanted expense entries
- **Data Persistence**: Automatically save and load data from file

## 4. Non-Functional Requirements
- **Usability**: Simple text-based interface easy for beginners
- **Reliability**: Handles invalid inputs gracefully without crashing
- **Performance**: Fast response time for all operations
- **Maintainability**: Clean, well-commented code structure

## 5. System Architecture
    User Input → ExpenseTracker Class → JSON File Storage
    ↓ ↓ ↓
    Menu Business Logic Data Persistence
    Display Data Processing File Operations 


# Expense Management System

A simple and efficient application to track, analyze, and manage daily expenses.  
It allows users to add and update expenses, view category-wise trends, and analyze monthly spending patterns through a clean and interactive interface.

## 📌 Overview

The Expense Management System helps users stay in control of their finances by providing a structured way to record and analyze expenses.  
It includes three major views:

- **Tab 1:** Add and update daily expenses  
- **Tab 2:** View expense breakdown by categories like rent, shopping, travel, entertainment and more  
- **Tab 3:** View month-wise financial trends to understand spending habits over time  

The goal of the project is to make personal finance tracking simple, fast, and visually clear.

## 🛠️ Tech Stack

| **Layer**      | **Tool**        |
|------------|-------------|
| Frontend   | Streamlit   |
| Backend    | FastAPI     |
| Database   | MySQL       |
| Visualization | pandas, matplotlib |


##  Setup Instructions

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

##  Running the Project

1. **Clone the repository**:
   ```bash
   https://github.com/vishu-01/Expense-Tracking-System.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
---


##  Dashboard Preview

- **Form**: quick add/update of daily expenses

- **Table**: total and percentage share by category

- **Bar chart**: category-wise expense breakdown

- **Bar chart**: month-wise spending overview

- **Summary**: clear monthly and category totals

---

##  TODO / Future Improvements

- Add user authentication
- Export filtered data as CSV/Excel
---

##  Author

**Vishu**  
 [LinkedIn](www.linkedin.com/in/vishu-936ba1280)  
 [GitHub](https://github.com/vishu-01)

---

##  License

MIT License – free to use and modify.

from fastapi import FastAPI, HTTPException
from datetime import date

# we need to write full path name orherwise it will make python confuse
# First we need to check the connection by testing basic return fucntion not data from our database
# And after this paste our link into the thunder client to test 

from backend import db_helper
from pydantic import BaseModel
app = FastAPI() 

# We don't want to get data in another format so for data validation we will use pydantic here
class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

# Now we are extracting the data from SQL database 
# After this paste the link(http://127.0.0.1:8000/expenses/2024-08-01) into the thunder client
# And then we will get data in the form of json in thunder client 

@app.get("/expenses/{expense_date}",response_model=list[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses 


# This function is used in updatation and deletion of the data in database as we know we need to use post function for this
@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses:list[Expense]):
    # We can't insert the new data without deleting previous records so we need to delete the pervious data
    db_helper.delete_expenses_for_date(expense_date)
    # We will insert multiple expenses so that's why we need to use for loop here.
    for expense in expenses:
        db_helper.insert_expenses(expense_date, expense.amount, expense.category, expense.notes)
    
    return {'message': 'Expenses updated successfully'}


# This function is used for expense analytics 
@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown


@app.get("/monthly_summary/")
def get_analytics():
    monthly_summary = db_helper.fetch_monthly_expense_summary()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary
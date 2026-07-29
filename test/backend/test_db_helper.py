# we are using the pytest concept here to test our code. 

from backend import db_helper

def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date('2024-08-15')
    # we only have one record in database so that's why we use this here
    # And our data is stored in list of dictionaries in database.
    # To access those record we need to set the index to 0 because by default the indexing starts from 0.
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'
    
# we can write multiple tests

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date('2028-08-15')
    assert len(expenses) == 0
    

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary('202333-08-01', '203334-08-05')
    assert len(summary) == 0
    
def test_fetch_expenses_by_august_and_september():
    monthes = db_helper.fetch_expenses_by_month()
    
    result = {m['month_name']: m['total_amount'] for m in monthes}
    assert result['August'] ==  26042.0
    assert result['September'] ==  4790.0
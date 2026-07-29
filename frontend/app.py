import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_monthes import analytics_months_tab


st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()
    
# type pip freeze in terminal and it will show you all the modules which has been used in the project
# if other person want to use my project they can use. 
#just type pip install -r .\requirements.txt in terminal and all my packages will be downloaded
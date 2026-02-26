'''
Task 4: Mini Dashboard (app_dashboard.py)

Create a small dashboard with:

    1. Title + Description

        "Simple Sales Dashboard"

    2. A select box with months

        months = ["January", "February", "March", "April"]

    3. A Static Dictionary of monthly sales:

        Sales = {
                "January":1200,
                "February":1500,
                "March":900,
                "April":2000
        }

    4. Display selected months sales using st.metric() or st.write()
    5. Display a bar chart using st.bar_chart(list(sales.values()))

(No pandas required -- simple list is allowed)

'''

import streamlit as st

st.title("Simple Sales Dashboard")
st.caption('This is a simple sales dashboard')

months = st.selectbox('Choose the month: ',("Choose Month","January", "February", "March", "April"))

sales = {
                "Choose Month":0,
                "January":1200,
                "February":1500,
                "March":900,
                "April":2000
        }

if months:
    chosen_sales = sales[months]
    #st.write(f'The sales of the {months} month is: {chosen_sales}')
    st.metric(label=f'The sales of the {months} month is', value=chosen_sales)

bar = st.bar_chart(list(sales.values()))

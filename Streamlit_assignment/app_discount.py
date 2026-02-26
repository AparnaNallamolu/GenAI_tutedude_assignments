'''
Task 2: Price Calculator (app_discount.py)
Build a simple price calculator app that:

    1. takes product price (number input)
    2. Takes discount percentage (slider from 0 to 50%)
    3. On button click, calculate discounted price
    4. Shows result using st.success()

Example:
    Original Price: 1000
    Discount: 10%
    Final Price: 900

Extra (optional): Show comparison in a small table

Before | After
(Use st.table() with simple list of lists.)
'''

import streamlit as st


product_price = st.text_input("Enter the Product Price: ")
discount_slider = st.slider("Discount Percentage: ", 0,50)
if discount_slider:
    st.write(f"The selected discount is: {discount_slider}")
button = st.button('Calculate Discounted Price')

if button:
    disc = int(product_price) * (int(discount_slider) / 100)
    amount = int(product_price) - disc
    st.success(f'The Discounted price is: {amount}')

    comparison = [[{product_price}], [{amount}]]
    heading = ['Before', 'After']
    table = st.table([heading]+[comparison])

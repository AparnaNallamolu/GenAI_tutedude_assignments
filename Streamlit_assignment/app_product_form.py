'''
Crate a Simple Form UI:

    1. Use Streamlit Sidebar to enter
        Product Name
        Category (select box with 3 - 5 options)
        Price

    2. When user click 'Add Product' Show:

        A Success message
        The product details in clean format

    Use:
        st.sidebar.text_input
        st.sidebar.selectbox
        st.sidebar.number_input
        st.sidebar.button
'''

import streamlit as st

st.title('Product Details')
product_name = st.sidebar.text_input('Enter the product name: ')

product_category = st.sidebar.selectbox('Enter the category: ',('Select category','Mobile', 'Grocery', 'Laptop'))
price = st.sidebar.number_input('Enter the price: ')
button = st.sidebar.button('Add Product')

if button:
    st.success('The data is successfully added')
    data = [[product_name], [product_category], [price]]
    heading = ['product name', 'product Category', 'price']
    st.table([heading]+[data])
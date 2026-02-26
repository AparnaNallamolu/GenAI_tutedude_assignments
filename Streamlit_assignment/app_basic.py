'''
Task 1 Basic Streamlit App

Create a basic Streamlit app that:

    1. Displays the title: 'Welcome to Streamlit'
    2. Shows a text input box for entering your name.
    3. When use clicks a button 'Greet Me' display:
        "Hello, !"
    
    Use: 
        st.title()
        st.text_input()
        st.button()
        st.write()
'''


import streamlit as st

st.title('Welcome to Streamlit ...!')
name = st.text_input('Enter your name: ')

button = st.button('Greet Me')

if button:
    st.write(f'Hello, {name}..!')
import streamlit as st
from db import DB

db= DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One', 'Check Flights','Analytics'])
if user_option == 'Check Flights':
    st.title('Welcome to Flights Analytics')
    col1, col2 = st.columns(2)
    city=db.fetch_city_names()  
    with  col1:
        st.selectbox('Select Source City', sorted(city))
    with col2:
        st.selectbox('Select Destination City', sorted(city))
elif user_option == 'Analytics':
    st.title('Welcome to Flights Analytics')
else:
    pass


   
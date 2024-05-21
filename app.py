import streamlit as st
import plotly.graph_objects as go
from db import DB

db= DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One', 'Check Flights','Analytics'])
if user_option == 'Check Flights':
    st.title('Welcome to Flights Analytics')
    col1, col2 = st.columns(2)
    city=db.fetch_city_names()  
    with  col1:
        source=st.selectbox('Select Source City', sorted(city))
    with col2:
        destination=st.selectbox('Select Destination City', sorted(city))
    if st.button('Search'):
        results= db.fetch_all_flights(source, destination)
        st.dataframe(results)
elif user_option == 'Analytics':
    st.title('Welcome to Flights Analytics')
    airline, frequency = db.fetch_airline_frequency()
    fig= go.Figure(
        go.Pie(
            labels= airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)


else:
    pass


   
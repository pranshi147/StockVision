import streamlit as st

#Function for Stock Comparison tab display as soon as the dashboard opens
def showSecond():

    mytext1= "Stock Comparison enables users to analyze and compare the performance of multiple stocks simultaneously through interactive visualizations and comparative analytics. Users can select different companies and evaluate their market behavior over a chosen time period to gain deeper investment insights."

    mytext2= "The comparison dashboard provides key metrics such as stock prices, percentage returns, trading volumes, and historical performance trends. Through visual tools like multi-line charts, bar charts, and comparative graphs, users can easily identify similarities, differences, and market trends across selected stocks."

    mytext3= "Stock Comparison is designed to simplify financial analysis by presenting multiple stocks in a single, intuitive interface. It helps users make informed decisions by offering clear visual comparisons and comprehensive performance insights."

    st.write(mytext1)
    st.write(mytext2)
    st.write(mytext3)
 
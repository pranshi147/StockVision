import streamlit as st

#Function for Stock Prediction tab display as soon as the dashboard opens
def showThird():

    mytext1= "Stock Prediction uses machine learning techniques to forecast future stock prices of next 5 days based on historical market data and price trends. Users can select a stock and generate predictions to gain insights into potential future market movements."

    mytext2= "The prediction module analyzes historical closing prices and identifies patterns using a trained predictive model. It generates future price forecasts and presents them through interactive visualizations, allowing users to observe expected trends and potential market directions over a selected forecast period."

    mytext3= "Stock Prediction is designed to provide an intuitive and data-driven forecasting experience. By combining historical analysis with predictive modeling, it helps users explore possible future stock behavior and better understand market dynamics."

    st.write(mytext1)
    st.write(mytext2)
    st.write(mytext3)
 
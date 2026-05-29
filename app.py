import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.data_loader import multiple_data
from utils.plots import plotting
from data.intro import showIntro
from utils.comparison import compare

st.set_page_config(
    page_title="Stock Vision",
    page_icon="assets/logo.png",
    layout="wide"
)

tab1, tab2= st.tabs(["Stock Analysis", "Stock Comparison"])
with tab1:
    st.sidebar.image("assets\elongated.png", width="stretch")
    st.title("Stock Vision")
    st.sidebar.title("Stock Vision Analysis")

    option = st.sidebar.selectbox("Select Stock",("AAPL", "TSLA", "MSFT", "NVDA", "GOOGL"), key="1")
    start = st.sidebar.date_input("Start Date",pd.to_datetime("2024-01-01"), key="1.1")
    end = st.sidebar.date_input("End Date",pd.to_datetime("today"), key="1.2")
    graph = st.sidebar.selectbox("Select Graph",("Line", "Bar", "Boxplot", "Heatmap"), key="1.3")

    data = load_data(option, start, end)

    if st.sidebar.button("Enter"):
        fig = plotting(graph, data, option)
        st.pyplot(fig)

        current_price = round(float(data['Close'].values[-1].item()), 2)
        highest_price = round(float(data['High'].values.max().item()), 2)
        lowest_price = round(float(data['Low'].values.min().item()), 2)
        avg_volume = int(float(data['Volume'].mean().item()))
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Current Price", f"${current_price}")
        col2.metric("Highest Price", f"${highest_price}")
        col3.metric("Lowest Price", f"${lowest_price}")
        col4.metric("Average Volume", f"{avg_volume:,}")

        csv = data.to_csv().encode('utf-8')

        st.download_button(label="Download CSV",data=csv,file_name=f"{option}_stock_data.csv",mime="text/csv")

    else:
        showIntro()

with tab2:
    st.title("Stock Vision")
    st.sidebar.title("Stock Vision Comparison")
    option=[]
    option1=(st.sidebar.multiselect("Select Stocks",("AAPL", "TSLA", "MSFT", "NVDA", "GOOGL"), key="2"))
    start1 = st.sidebar.date_input("Start Date",pd.to_datetime("2024-01-01"), key="2.1")
    end1 = st.sidebar.date_input("End Date",pd.to_datetime("today"), key="2.2")
    graph1 = st.sidebar.selectbox("Select Graph",("Line", "Bar", "Boxplot", "Heatmap"), key="2.3")

    if st.sidebar.button("Compare"):
        stocks= {}
        for x in option1:
            stocks[x] = load_data(x,start1,end1)
        fig = compare(stocks)
        st.pyplot(fig)
            

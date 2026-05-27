import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.plots import plotting

st.set_page_config(
    page_title="Stock Vision",
    page_icon="assets/logo.png",
    layout="wide"
)

st.title("📈 Stock Vision")
st.sidebar.title("Stock Vision")

option = st.sidebar.selectbox(
    "Select Stock",
    ("AAPL", "TSLA", "MSFT", "NVDA", "GOOGL")
)

start = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2024-01-01")
)

end = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("today")
)

graph = st.sidebar.selectbox(
    "Select Graph",
    ("Line", "Bar", "Boxplot", "Heatmap")
)

data = load_data(option, start, end)

if st.sidebar.button("Enter"):
    fig = plotting(graph, data, option)
    st.pyplot(fig)
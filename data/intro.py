import streamlit as st

#Function for introduction display as soon as the dashboard opens
def showIntro():

    mytext1="StockVision is an interactive stock market analytics dashboard that allows users to explore and analyze stock market trends through dynamic visualizations and financial insights. Users can select different stocks, customize date ranges, and study market behavior using multiple analytical charts and visual tools."
    mytext2="The dashboard provides important market insights including current stock price, highest and lowest prices, average trading volume, and historical trend analysis. It also supports data exploration through graphical representations such as line charts, bar charts, heatmaps, and boxplots, making it easier to identify patterns and compare stock performance."
    mytext3="StockVision is designed to deliver a clean, modern, and user-friendly analytics experience while helping users better understand stock market movements and financial data trends."

    st.write(mytext1)
    st.write(mytext2)
    st.write(mytext3)
 
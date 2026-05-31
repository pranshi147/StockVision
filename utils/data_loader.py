import yfinance as yf

#Function to retrieve data for Stock Analysis
def load_data(option, start, end):
    data = yf.download(option, start=start, end=end)
    return data

#Function to retrieve data for Stock Comparison
def multiple_data(option1, start1, end1):
    data=yf.download(option1, start1, end1)
    return data
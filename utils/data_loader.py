import yfinance as yf

def load_data(option, start, end):
    data = yf.download(option, start=start, end=end)
    return data

def multiple_data(option1, start1, end1):
    data=yf.download(option1, start1, end1)
    return data
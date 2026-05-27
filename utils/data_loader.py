import yfinance as yf

def load_data(option, start, end):
    data = yf.download(
        option,
        start=start,
        end=end
    )
    return data
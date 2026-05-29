import matplotlib.pyplot as plt

def compare(stocks):
    fig, ax = plt.subplots(figsize=(12, 5))

    for ticker, data in stocks.items():
        ax.plot(data.index,data['Close'],label=ticker)
    ax.set_title("Stock Comparison")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.legend()

    return fig
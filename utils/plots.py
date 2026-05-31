import matplotlib.pyplot as plt
import seaborn as sns

#Function to display graphs based on the user input
def plotting(graph, data, ticker):

    fig=plt.figure(figsize=(12, 5))

    if graph == "Line":
        plt.plot(data.index, data['Close'])
        plt.title(f"{ticker} Closing Price")
        plt.xlabel("Date")
        plt.ylabel("Price")

    elif graph == "Bar":
        plt.bar(data.index, data['Volume'].values.flatten())
        plt.title(f"{ticker} Trading Volume")
        plt.xlabel("Date")
        plt.ylabel("Volume")

    elif graph == "Heatmap":
        correlation = data.corr(numeric_only=True)
        sns.heatmap(
            correlation,
            annot=True,
            cmap="viridis"
        )

        plt.title(f"{ticker} Correlation Heatmap")

    else:
        plt.boxplot(data['Close'])
        plt.title(f"{ticker} Closing Price Distribution")
        plt.ylabel("Price")
    return fig
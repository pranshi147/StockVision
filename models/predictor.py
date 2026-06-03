from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def prepare(data):
    data = data.copy()

    # Previous 5 closing prices
    data["Close_1"] = data["Close"].shift(1)
    data["Close_2"] = data["Close"].shift(2)
    data["Close_3"] = data["Close"].shift(3)
    data["Close_4"] = data["Close"].shift(4)
    data["Close_5"] = data["Close"].shift(5)

    # Tomorrow's close price
    data["Future_Close"] = data["Close"].shift(-1)
    data.dropna(inplace=True)
    return data

def trainer(data):
    data = prepare(data)
    X = data[["Close_1", "Close_2", "Close_3", "Close_4", "Close_5"]]
    y = data["Future_Close"]

    trainx, testx, trainy, testy = train_test_split(
        X,
        y,
        test_size=0.2,
        shuffle=False
    )

    reg = LinearRegression()
    reg.fit(trainx, trainy)
    return reg, testx, testy, X
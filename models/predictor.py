from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def trainer(data):
    x=data[["Open", "High", "Low", "Volume"]]
    y=data[["Close"]]
    trainx, testx, trainy, testy= train_test_split(x,y, test_size=0.2, random_state=42)

    reg= LinearRegression()
    reg.fit(trainx, trainy)
    return reg, testx, testy

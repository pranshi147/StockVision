# 📈 StockVision

StockVision is an interactive stock market analytics and prediction dashboard that enables users to explore stock trends, compare multiple stocks, visualize financial data, and generate machine learning-based stock price predictions through an intuitive interface.

The project combines financial analytics, data visualization, and predictive modeling to help users better understand stock market behavior using real-world market data.

---

## 🚀 Features
![Screenshot 1](assets/ss1.png)

![Screenshot 2](assets/ss2.png)

![Screenshot 3](assets/ss3.png)

![Screenshot 4](assets/ss4.png)

### 📊 Stock Analysis Dashboard

* Analyze individual stocks using historical market data
* Interactive date range selection
* Multiple visualization options:

  * Line Charts
  * Bar Charts
  * Boxplots
  * Correlation Heatmaps
* Dark themed analytics dashboard

### 📈 Key Performance Indicators (KPIs)

* Current Stock Price
* Highest Price
* Lowest Price
* Average Trading Volume

### 🔍 Multi-Stock Comparison

* Compare multiple stocks simultaneously
* Visual comparison of stock performance
* Trend analysis across different companies

### 🤖 Machine Learning Prediction

* Stock price prediction using Linear Regression
* Actual vs Predicted stock price visualization
* Historical trend-based forecasting

### 📥 Data Export

* Download analyzed stock data as CSV files
* Easy access for further analysis and research

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Yahoo Finance API (yfinance)

---

## 📂 Project Structure

```text
StockVision/
│
├── app.py
│
├── assets/
│   ├── logo.png
│   └── elongated.png
│
├── data/
│   └── intro.py
│
├── models/
│   └── predictor.py
│
├── utils/
│   ├── data_loader.py
│   ├── plots.py
│   └── comparison.py
│
├── requirements.txt
└── README.md
```

---

## 📷 Dashboard Modules

### Stock Analysis

Analyze historical stock data with multiple chart types and financial metrics.

### Stock Comparison

Compare multiple stocks on a single visualization to identify performance trends and market behavior.

### Prediction Module

Generate stock price predictions using machine learning and compare predicted values with actual market data.

---

## 📈 Machine Learning Workflow

The prediction system follows a supervised machine learning approach:

1. Historical stock data is collected.

2. Features such as:

   * Open
   * High
   * Low
   * Volume

   are used as inputs.

3. Closing Price is used as the target variable.

4. A Linear Regression model is trained on historical market data.

5. Predictions are generated and visualized against actual stock prices.

---

## 🎯 Learning Outcomes

This project demonstrates practical applications of:

* Financial Data Analysis
* Data Visualization
* Machine Learning
* Time-Series Exploration
* Dashboard Development
* Data Processing and Feature Engineering

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/pranshi147/StockVision.git
```

Move into the project directory:

```bash
cd StockVision
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

* Moving Average Indicators
* RSI and MACD Analysis
* Candlestick Charts
* Random Forest Regression
* LSTM-based Forecasting
* Real-Time Market News Integration
* Sentiment Analysis
* Portfolio Optimization Tools

---

## 👩‍💻 Author

**Pranshi Mittal**

GitHub: https://github.com/pranshi147

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

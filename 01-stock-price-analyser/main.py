# what should the project do: 
# 1. download ticker stock data 
# 2. show first rows of the dataset
# 3. plots the closing price over time
# 4. Calculates the total return
# 5. Prints a short summary

#Example output: 
# Ticker: AAPL
# Start price: $125.07
# End price: $192.53
# Total return: 53.94%
# Highest close: $196.45
# Lowest close: $124.17
# Average close: $172.38

#Could add some cool visualizations using other libraries

# Workflow: 
#user enters ticker
#→ yfinance downloads data
#→ pandas stores it as a table
#→ we inspect the table
#→ we calculate numbers
#→ we print summary
#→ later we plot charts

import yfinance as yf

ticker = input("Input a stock ticker symbol: ").upper()

stock_data = yf.download(ticker, start="2023-01-01", end="2024-01-01")

print(stock_data.head())

#conventional analyst metric used is the closing price which we will need for all calculations 
close_prices = stock_data["Close"][ticker]

starting_price = close_prices.iloc[0]
ending_price = close_prices.iloc[-1]
highest_close = close_prices.max()
lowest_close = close_prices.min()
average_close = close_prices.mean()


print("Stock price")
print("-------------------------------------")
print(f"Ticker: {ticker}")
print(f"Starting Price: {starting_price:.2f}")
print(f"ending Price: {ending_price:.2f}")
print(f"highest Close = {highest_close:.2f}")
print(f"lowest Close: {lowest_close:.2f}")
print(f"Average Close: {average_close:.2f}")

# Total return is endprice minus starting price over starting price times 100
total_return = ((ending_price-starting_price)/starting_price * 100)
print(f"RETURN:\n{total_return:.2f}%")

#plot closing price over time: 
import matplotlib.pyplot as plt

plt.plot(close_prices)
plt.title(f"{ticker}'s closing prices over time")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.show()

#project finished
#future things to add: 
#Multi-ticker input
#Price chart
#Moving averages
#Return %
#Volatility
#Maximum drawdown
#SPY comparison
#Streamlit dashboard
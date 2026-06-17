#write out what the project should do and a specific example of its performance break the problem down into steps and code each step to the best of your ability before moving onto 
# tip: hardcode first don't worry about user input 

import pandas as pd 
import yfinance as yf
import matplotlib as plt

#user inputs data
#data input includes: stock tickers, weights for each stock ticker, date range to pull the data from

tickers = ["AAPL", "MSFT", "NVDA"]
weights = [0.50, 0.25, 0.25]
start_date = "2024-01-01"
end_date = "2025-01-01"

if sum(weights) != 1:
    print("Sum of weights must be = to 1")

total_portfolio_daily_returns = 0

for i, ticker in enumerate(tickers): 
    stock_data = yf.download(ticker,
                             start_date, 
                             end_date
                            )
    print(f"--------------------------------------------\nStock Data for: {ticker}\n--------------------------------------------\n")
    print(stock_data.head())
    # access the daily closing price data 
    closing_price = stock_data["Close"][ticker]
    #ticker = 1 #reinitialize the counter for the loop idk how to do that
    print(f"--------------------------------------------\nClosing Price for: {ticker}\n--------------------------------------------\n")
    print(closing_price.head())

    #start and end price access
    starting_price = stock_data["Open"][ticker]
    
    returns = (starting_price - closing_price)/starting_price #For portfolio calculations do not multiply by 100, only multiply by 100 when displaying returns
    #print(f"--------------------------------------------\nDaily Returns for: {ticker}\n--------------------------------------------\n") #print(returns.head()) DEBUG: to check if printing correctly

    for weight in weights:
        portfolio_weighted_returns = returns * weight[i]
    print(f"--------------------------------------------\nWeighted Returns for: {ticker}\n--------------------------------------------\n")
    print(portfolio_weighted_returns) 
 
    total_portfolio_daily_returns += portfolio_weighted_returns
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

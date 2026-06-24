#write out what the project should do and a specific example of its performance break the problem down into steps and code each step to the best of your ability before moving onto 
# tip: hardcode first don't worry about user input 

import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

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
    


    # access the daily closing price data 
    closing_price = stock_data["Close"][ticker]
    #ticker = 1 #reinitialize the counter for the loop idk how to do that

    #start and end price access
    starting_price = stock_data["Open"][ticker]
    
    returns = closing_price.pct_change() #For portfolio calculations do not multiply by 100, only multiply by 100 when displaying returns
    
    portfolio_weighted_returns = returns * weights[i]
    
    print(portfolio_weighted_returns) 
    
    total_portfolio_daily_returns += portfolio_weighted_returns




#Plot the growth of portfolio weighted returns for each ticker using plt
portfolio_growth = (1 + total_portfolio_daily_returns).cumprod() #gives you the multiplier of each day
plt.plot(portfolio_growth)
plt.title("Growth of Weighted Returns")
plt.xlabel("Time")
plt.ylabel("Weighted Returns")
plt.show()

initial_investment = 1000
portfolio_value = portfolio_growth * initial_investment


growth_multiplier = portfolio_growth.iloc[-1]
final_value = initial_investment * growth_multiplier
total_percentage_returns = (growth_multiplier - 1) * 100
#calculate best day and worst day
best_day = total_portfolio_daily_returns.max()
worst_day = total_portfolio_daily_returns.min()


#calculate volatility: 
volatility = total_portfolio_daily_returns.std()

total_percentage_return = (growth_multiplier-1)* 100


#summary and formatting (will just check formatting right now)
#print("hello") #DEBUG: checking if it gets this far...
print(f"----------------SUMMARY----------------\n ")
print(f"Initial investment: {initial_investment}\n")
print(f"Final Value: {final_value}\n")
print(f"Percentage Return: {total_percentage_return}\n") 
print(f"Best day: {best_day}\n") 
print(f"Worst day: {worst_day}\n")
print(f"volatility: {volatility}")

# TODO tomorrow:
# Fix portfolio_growth bug.
# total_portfolio_daily_returns should be a pandas Series, not int. so that .cumprod() can work on it.
# Check closing_price extraction inside loop.


given a set of stocks and weights, calculate how the portfolio perfomed over time 
user provides something like: 
msft - 50 
aapl - 30 
nvda - 20 

Program should:
download the price data for each ticker
gets the daily closing prices
calculates daily return for each stock
multiply each stock by return by its portfolio weight
adds them together to get portfolio return
shows: 
- total portfolio return
- start value 
- end value 
- best performing stock 
- worst perfoming stock
- graph of portfolio growth

Requirements: 
pandas - for data manipulation
matplotlib - visualize the portfolio growth over time 
yfinance - to pull historical ticker data


Example input
Tickers: AAPL, MSFT, NVDA
Weights: 50, 30, 20
Start date: 2023-01-01
End date: 2024-01-01
Initial investment: 10000
Example output
Portfolio Summary
-----------------
Initial Investment: $10,000
Final Value: $14,250
Total Return: 42.5%

Best Stock: NVDA
Worst Stock: AAPL
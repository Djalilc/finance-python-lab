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
import pandas as pd 
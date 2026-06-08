# Momentum-strategy
Time series momentum strategy based on Moskowitz, Ooi, and Pedersen (2012)
# Overview
This project implements a time series momentum strategy based on Moskowitz, Ooi, and Pedersen (2012). The strategy uses 12-month 
historical returns as a signal to take long or short positions on futures contracts. Initially tested on crude oil futures, which 
produced negative returns, the strategy was expanded to five futures contracts across commodities, equity indexes, bonds, and 
currencies. Results confirmed the paper's findings — equity index and bond futures showed stronger momentum with positive cumulative 
returns and higher Sharpe Ratios.

# Academic Foundation
As stated this project is based on the momentum strategy by Moskowitz and tested on similar markets but also looking at something more  
geopolically structured like Crude Oil.

Moskowitz, T., Ooi, Y.H., and Pedersen, L.H. (2012). "Time Series Momentum." Journal of Financial Economics, 104(2), 228-250.

# Project Structure
`data_collection.py`
  This file collects the data through yFinance on the chosen ticker.
`signal_construction.py`
  This file setups our signal by calling the closing prices of each day and the closing price of the same day a year prior and   
  calculate the percent change between the two days.
`strategy.py`
  This file takes the percent changes previously calculated and assigns a position to each.
`backtest.py`
  This file s backtesting the data to see if this is a profitable strategy
`performance.py`
  This file calculates the average daily return, standard deviation, and the sharpe ratio to determine the success of the strategy.
`multi_asset.py`
  Combines all the files above into one for loop that can run multiple tickers at once and compare them. 
  
# Results
| Ticker | Sharpe Ratio | Cumulative Return |
|--------|--------------|-------------------|
| CL=F | 0.2798 | 0.8892 |
| GC=F | -0.1192 | 0.7758 |
| ES=F | 0.2613 | 1.3193 |
| ZN=F | 0.3941 | 1.1987 |
| EURUSD=X | -0.0518 | 0.9422 |

# How to Run
Adjust the tickers in the provided locations in either the data_collection.py for one singular run of multi_asset.py to run numerous. 
To use the singular ticker system, run the data_collection.py first then the signal_construction.py, then strategy.py, then backtest.py 
and finally performance.py. Or, adjust the tickers in the multi_asset.py folder and run it. 

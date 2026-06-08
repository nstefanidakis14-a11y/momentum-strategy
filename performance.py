import pandas as pd
import numpy as np

#import and organize the data
data = pd.read_csv("backtest_data.csv", index_col=0, parse_dates=True)

# Find the average profit or loss per day of the strategy return data
avg_daily_return = data["Strategy_Return"].mean()

# Standard deviation of the data set
std_daily_return = data["Strategy_Return"].std()

#Using the standard deviation and average caluculate the sharpe ratio

sharpe_ratio = avg_daily_return/std_daily_return * np.sqrt(252)

print("Average Daily Return", avg_daily_return)
print("Standard Deviation",std_daily_return)
print("Sharpe Ratio",sharpe_ratio)
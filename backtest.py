import pandas as pd

data = pd.read_csv("strategy_data.csv", index_col=0, parse_dates=True)

print(data.head())

# This line is the calculation for the percent change from one day to the day before
data["Daily_Return"] = data["Close"].pct_change(1)

# This is the actual return based on the position from 
# Basically what I made whether or not it is correct
data["Strategy_Return"] = data["Position"].shift(1) * data["Daily_Return"]

# dropping all NaN values because there are no values
data = data.dropna()

# Every column that I want I amcalling here 
print(data[["Close", "Position", "Daily_Return", "Strategy_Return"]].head(10))

# This tells me if I would make money from using this strategy if I started with $1 
# cumprod is multiplying the money I enter the trade with every day times the percentage change to get our new total
data["Cumulative_Return"] = (1 + data["Strategy_Return"]).cumprod()
print(data["Cumulative_Return"].tail())

# Oil is an exogenous shock. (Geopolitical events have a major effect not just market cycles) Less to do with actual price momentum

data.to_csv("backtest_data.csv")
print("Backtest saved successfully")
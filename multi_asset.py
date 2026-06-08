import pandas as pd
import yfinance as yf
import numpy as np

#This is calling the ticker symbols we want to study for crude oil gold s and P 500 rasury and euro to usd
tickers = ["CL=F", "GC=F", "ES=F", "ZN=F", "EURUSD=X"]

results = []

for ticker in tickers:
#Indent to create loop download the data
    data = yf.download(ticker, start= "2015-01-01", end= '2025-01-01')
    #grabbing these specific columns
    data = data[["Close", "Volume"]]
    #relabeling to liimit NaN recults
    data.columns = ["Close", "Volume"]
    #Creating the momentum file
    data["Momentum"] = data["Close"].pct_change(252)
    data = data.dropna()
    #Relabeling each with a position value of 1 or -1
    data["Position"] = data["Momentum"].apply(lambda x: 1 if x>0 else-1)
    #percent change of the close price 
    data["Daily_Return"] = data["Close"].pct_change(1)
    #shift to avoid look ahead bias muliptly by return to find total return
    data["Strategy_Return"] = data["Position"].shift(1) * data["Daily_Return"]
    data = data.dropna()
    #calculate the cumulative return
    data["Cumulative_Return"] = (1+data["Strategy_Return"]).cumprod()
    #calculate the cumulative return iloc gives you the last value in the last row
    cumulative_return = data["Cumulative_Return"].iloc[-1]
    #calcaulate sharpe ratio
    sharpe_ratio = (data["Strategy_Return"].mean()/ data["Strategy_Return"].std()) * np.sqrt(252)
    #filling in the results table we created earlier with labeled values 
    results.append({
        "Ticker": ticker,
        "Sharpe Ratio": round(sharpe_ratio, 4),
        "Cumulative_Return": round(cumulative_return, 4)
    })
# This converts the results to a data frame and creates a table comparing all the tickers
results_df = pd.DataFrame(results)
print(results_df)
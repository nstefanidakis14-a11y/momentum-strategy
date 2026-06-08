# importing the yfinance data while also renaming it simpler same goes for the pandas
import yfinance as yf
import pandas as pd

# doing this so that each time I want to pull a new stock only have to change it here
ticker = "CL=F"

#pulling the ticker I just named and the dates of the information I want between
data = yf.download(ticker, start="2015-01-01",end="2025-01-01")

# The [[]] is how to pull out multiple columns 
data = data[["Close","Volume"]]

# labeling the columns in the data so that when the columns are pulled in other files
# they are properly labeled and not processed as NaN code
#basically flattens out the headers before saving so no mess when pulling later on
data.columns = ["Close","Volume"]

print(data)

#Saving the data to my laptop so it is easily accessible and does not have to be pulled online everytime
data.to_csv("crude_oil_data.csv")
print("data saved successfully")

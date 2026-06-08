import pandas as pd

# This is telling the pandas to read the csv of our signal data create the index column 
# and set the parse dates as true so python knows it is reading dates
data = pd.read_csv("signal_data.csv", index_col=0, parse_dates=True)

# This is creating the position statement where I am telling python to go through the momentum data
# and any positive values label with 1 and else label -1
# +1 means go long and -1 means go short
# lambda is a function that applies a rule to every row
data["Position"] = data["Momentum"].apply(lambda x:1 if x > 0 else -1)

# This is to display the data from the columns that we want
# Remember 2 bracket sets for multiple columns called
print(data[["Close", "Momentum", "Position"]].head(10))

# saving the positions data to a new csv file
data.to_csv("strategy_data.csv")
print("strategy saved successfully")

# This represents the percent change between one day and that day 1 year ago 
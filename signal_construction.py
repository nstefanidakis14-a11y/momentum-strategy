import pandas as pd
# This next line calls the csv crude oil and then it labels the index column as dates (if needed label it "Date" istead of just numbers
# and then the parse_dates is what tells python to treat the column as dates not just a line of text so we can do date math
# Now that is knows its date I can utilize by calling it to do things between dates
#The header is there so that python knows the first
data = pd.read_csv("crude_oil_data.csv", index_col=0, parse_dates=True)

# head lets it look into the first five rows of data as a check
print(data.head())

#This line sets up the signal by looking at whichever individual day 
# and comparing the percent change of that day exactly a year ago 
data["Momentum"] = data["Close"].pct_change(252)

#drops the empty data slots 
data = data.dropna()
#prints the data from the signal with just showing the close and the momentum 
# head 260 shows the first 260 rows 
print(data[["Close","Momentum"]].head(260))


#converting the signal data to be used as a csv
data.to_csv("signal_data.csv")
print("SIgnal saved successfully")
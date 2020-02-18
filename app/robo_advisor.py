# app/robo_advisor.py

#modules to import
import json
import csv
import os

#packages to import
import requests

#Function to convert Float to USD
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# Information Inputs
#
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)
#print(type(response)) # <class 'requests.models.Response'>
#print(response.status_code) #200 or successful
#print(response.text) #string, import json to convert it to dictionary

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]


#finding the latest day
dates = list(tsd.keys()) #assuming that the latest date is first, if the data structure changes we should sort
latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

#recent high
high_prices = []
low_prices = []

for date in dates:
    high_price = float(tsd[date]["2. high"])
    low_price = float(tsd[date]["3. low"]) #date loops through all available data - limit to 100 days? 
    high_prices.append(high_price)
    low_prices.append(low_price)

recent_high = max(high_prices)
recent_low = min(low_prices)



# writing data to CSV

#breakpoint()

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")

print("-------------------------")
print("LATEST DAY: " + str(last_refreshed))
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")

print("-------------------------")
#if statement for recommendation 
#if blank, print buy
#elif blank, print hold
#else blank: print sell

print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")

print("-------------------------")
print("HAPPY INVESTING!")

print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path} . . .")


#writing data to CSV
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]


with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames= csv_headers)
    writer.writeheader() # uses fieldnames set above

#loop through 
    writer.writerow({
        "timestamp": "Todo",
        "open": "Todo",
        "high": "Todo",
        "low": "Todo",
        "close": "Todo",
        "volume": "Todo",
    })

    writer.writerow({
        "timestamp": "Todo",
        "open": "Todo",
        "high": "Todo",
        "low": "Todo",
        "close": "Todo",
        "volume": "Todo",
    })

#def pritn(value, ..., sep, end, file, flush)
# app/robo_advisor.py

#packages to import

import requests
import json


#old functio to convert float to USD
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

for date in dates:
    high_price = float(tsd[latest_day]["2. high"])
    high_prices.append(high_price)


recent_high = max(high_prices)


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")

print("-------------------------")
print("LATEST DAY: " + str(last_refreshed))
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")

print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")

print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


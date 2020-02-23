# app/robo_advisor.py

#MODULES TO IMPORT
import json
import csv
import os

from datetime import datetime

#PACKAGES TO IMPORT
import requests
from dotenv import load_dotenv
load_dotenv()

#FUNCTION TO FORMAT USD
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# INFORMATION INPUTS
#

symbol = input("Enter the Stock Symbol: ")
#api_key = os.getenv(ALPHAVANTAGE_API_KEY, default="demo")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=demo"
response = requests.get(request_url)

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]


#TIME OF REQUEST
now = datetime.now()
current_time = now.strftime("%H:%M:%S") #help from https://www.programiz.com/python-programming/datetime/current-time
current_year = now.year
current_month = now.month
current_day = now.day
current_hour = now.hour
current_minute = now.minute

#FINDING THE LATEST DAY
dates = list(tsd.keys()) #assuming that the latest date is first
latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

#RECENT HIGH & LOW
high_prices = []
low_prices = []

for date in dates:
    high_price = float(tsd[date]["2. high"])
    low_price = float(tsd[date]["3. low"])
    high_prices.append(high_price)
    low_prices.append(low_price)

recent_high = max(high_prices)
recent_low = min(low_prices)

# WRITE DATA TO CSV FILE

print("-------------------------")
print("SELECTED SYMBOL: " + str(symbol))
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")

#DATE AND TIME OF REQUEST
if int(current_hour) > 12 and int(current_minute) > 9:
    print("REQUEST AT " + str(current_hour - 12) + ":" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
elif int(current_hour) > 12 and int(current_minute) < 9: 
    print ("REQUEST AT " + str(current_hour-12) + ":0" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
elif int(current_hour) is 12 and int(current_minute) < 9:
    print("REQUEST AT " + str(current_hour) + ":0" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
elif int(current_hour) is 12 and int(current_minute) > 9:
    print("REQUEST AT " + str(current_hour) + ":" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
elif int(current_hour) < 12 and int(current_minute) < 9:
    print("REQUEST AT " + str(current_hour) + ":0" + str(current_minute) + "am on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
else:
    print("REQUEST AT " + str(current_time) + "am on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))


#if "Error message" in str(parsed_response) 
 #   print("Oops, we could not find that stock symbol, please try again")
  #  quit()

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


#writing data to CSV
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") # a relative filepath
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above

    writer.writerow({
        "timestamp": "TODO",
        "open": "TODO",
        "high":"TODO",
        "low": "TODO",
        "close": "TODO",
        "volume": "TODO"
    })
    writer.writerow({
        "timestamp": "TODO",
        "open": "TODO",
        "high":"TODO",
        "low": "TODO",
        "close": "TODO",
        "volume": "TODO"
    })

print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")

##loop through 
#    for date in dates:
#        daily_prices = tsd[date]
#        writer.writerow({
#            "timestamp": date,
#            "open": (daily_prices["1. open"]),
#            "high": (daily_prices["2. high"]),
#            "low": (daily_prices["3. low"]),
#            "close": (daily_prices["4. close"]), 
#            "volume": daily_prices["5. volume"],
#        })
#


#def pritn(value, ..., sep, end, file, flush)
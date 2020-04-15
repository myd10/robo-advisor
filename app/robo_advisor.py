# app/robo_advisor.py

#MODULES TO IMPORT
import json
import csv
import os
from datetime import datetime

#PACKAGES TO IMPORT
from dotenv import load_dotenv
load_dotenv()
import requests

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", default = "demo")

def to_usd(my_price):
    """
    Converts float or interger into a readible USD format
    Param: my_price
    Example: to_usd(4000.444)
    Return: $4,000.44
    """
    return "${0:,.2f}".format(my_price)

def get_response(symbol):
    """
    """
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def transform_response(parsed_response):
    """
    """
    tsd = parsed_response["Time Series (Daily)"]

    rows=[]

def lines():
    """
    Improve readability by dividing sections with dashed lines
    Param: none
    Example: lines()
    Return: ("-------------------------")
    """
    print("-------------------------")

def friendly_timestamp(now):
    """
    Converts datetime information into a human friendly string
    Param: now
    Example: 
        current_year = 2020
        current_month = 4
        current_day = 14
        current_hour = 20
        current_minute = 5
        current second = 12
    Returns: 2020-4-13 8:05pm 
    """
    return (now).strftime(("%m/%d/%Y %I:%M %p"))


run = True
while run:


#if __name__ == "__main__":

    
# INFORMATION INPUTS
    symbol = input("Enter the Stock Symbol: ")

    #Error Trapping for Incorrect Ticker format
    while True:
        try:
            symbol = float(symbol)
            print("Oh no, that ticker does not work. Please try again with a properly-formatted stock symbol like 'MSFT'.")
            quit()
        except ValueError:
            break


    string_response = json.dumps(response.text)


    #Error Trapping for incorrect ticker 
    if "Error" in string_response: 
        print("Oops, we could not find that stock symbol. Please check the ticker and try again.") 
        quit()
    else:
        pass

    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


    #TIME OF REQUEST
    now = datetime.datetime.now()
    # current_time = now.strftime("%H:%M:%S") #help from https://www.programiz.com/python-programming/datetime/current-time
    # current_year = now.year
    # current_month = now.month
    # current_day = now.day
    # current_hour = now.hour
    # current_minute = now.minute

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

    #PRINT STOCK SYMBOL HEADER
    lines()
    print("SELECTED SYMBOL: " + str(symbol).upper()) #CONVERTS INPUT TO ALL CAPS
    lines()
    print("REQUESTING STOCK MARKET DATA...")

    #DATE AND TIME OF REQUEST
   # if int(current_hour) > 12 and int(current_minute) > 9:
   #     print("REQUEST AT " + str(current_hour - 12) + ":" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
   # elif int(current_hour) > 12 and int(current_minute) < 9: 
   #     print ("REQUEST AT " + str(current_hour-12) + ":0" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
   # elif int(current_hour) is 12 and int(current_minute) < 9:
   #     print("REQUEST AT " + str(current_hour) + ":0" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
   # elif int(current_hour) is 12 and int(current_minute) > 9:
   #     print("REQUEST AT " + str(current_hour) + ":" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
   # elif int(current_hour) < 12 and int(current_minute) < 9:
   #     print("REQUEST AT " + str(current_hour) + ":0" + str(current_minute) + "am on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
   # else:
   #     print("REQUEST AT " + str(current_hour) + ":" + str(current_minute) + "am on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))

    #PRINTING PRICE INFORMATION

    lines()
    print(datetime.now(("%Y-%m-%d %H:%M:%S") ))
    lines()


    lines()
    print("LATEST DAY: " + str(last_refreshed))
    print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    lines()

    #ROBO ADVISOR RECOMMENDATION
    if float(latest_close) < 1.10 * float(recent_low) and float(latest_close) < 1000.00:
        print("RECOMMENDATION: BUY")
        print("RECOMMENDATION REASON: The price is within 20% of its recent low. This is a good opporunity to buy low and sell high.")
    elif float(latest_close) > 1000.00:
        print("RECOMMENDATION: DO NOT BUY")
        print("RECOMMENDATION REASON: Empirical evidence shows that a diversified portfolio performs better than less diversifed portfolios. Spending more than $1,000 on a single share, will limit your ability to diversify and is therefore not a prudent decision.")
    elif float(latest_close) > 1.10 * float(recent_low) and float(latest_close) < 1.30 * float(recent_low):
       print("RECOMMENDATION: BUY A FEW SHARES.")
       print("RECOMMENDATION REASON: The stock is undervalued and diversfication is important. However we feel less confident about " + str(symbol).upper() + " than we feel about other stocks.")
    else:
        print("RECOMMENDATION: DO NOT BUY")
        print("RECOMMENDATION REASON: The latest closing price is too near its recent high. Wait until the stock price falls to make this purchase.")

    lines()

    #writing data to CSV
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"{symbol.upper()}_prices.csv") # a relative filepath
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date,
                "open": to_usd(float(daily_prices["1. open"])),
                "high":to_usd(float(daily_prices["2. high"])),
                "low": to_usd(float(daily_prices["3. low"])),
                "close": to_usd(float(daily_prices["4. close"])),
                "volume": daily_prices["5. volume"] #string
            })

    lines()
    print(f"WRITING DATA TO CSV: {csv_file_path}...")


    again=str(input("Do you want information on another stock? [y/n] ")) #https://stackoverflow.com/questions/26961427/asking-the-user-if-they-want-to-play-again 
    if again.lower() == "yes" or again.lower() == "y":
        run = True
    else:
        print("HAPPY INVESTING!")
        quit()



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
    return "${0:,.2f}".format(float(my_price))

def get_response(symbol):
    """
    Uses API_KEY and alphavantage to search a stock symbol and convert the dict into str
    Params: symbol inputting by User
    Example: get_response(BUD)
    Returns: ""

    """
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def transform_response(parsed_response):
    """
    Transforms response to match 6 headings and appends row to a list
    Param: parsed_response from request_url
    Example: transform_response(parsed_response)
    Returns: []
    """
    tsd = parsed_response["Time Series (Daily)"]

    rows = []
    for date, daily_prices in tsd.items(): 
        row = {
            "timestamp": date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)
    return rows

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

def write_to_csv(rows, csv_filepath):
    """
    This function writes a list of dictionaries to a csv file given by the filepath
    Params: list of dictionaries, location for csv file
    Example: 
    Returns:
    """
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
    
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    
    return True

run = True
while run:

    if __name__ == "__main__":
    
    # SYMBOL INPUT & ERROR TRAPPING FOR INCORRECT TICKER FORMAT
        symbol = input("Enter the Stock Symbol: ")
    
        while True:
            try:
                symbol = float(symbol)
                print("Oh no, that ticker does not work. Please try again with a properly-formatted stock symbol like 'MSFT'.")
                quit()
            except ValueError:
                break
            
        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(request_url)
        string_response = json.dumps(response.text)
    
        if "Error" in string_response: 
            print("Oops, we could not find that stock symbol. Please check the ticker and try again.") 
            quit()
        else:
            pass
        
        #INFORMATION INPUTS
    
        parsed_response = get_response(symbol)
    
        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
        
        rows = transform_response(parsed_response)
    
        now = datetime.now()
    
        #dates = list(tsd.keys())
    
        latest_day = rows[0]
    
        latest_close = rows[0]["close"]
    
        #RECENT HIGH & LOW
        high_prices = [row["high"] for row in rows]
        low_prices = [row["low"] for row in rows]
        recent_high = max(high_prices)
        recent_low = min(low_prices)
    
       # for date in dates:
       #     high_price = float(tsd[date]["2. high"])
       #     low_price = float(tsd[date]["3. low"])
       #     high_prices.append(high_price)
       #     low_prices.append(low_price)
    #
    
        current_friendly_time = friendly_timestamp(datetime.now())
    
        csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"{symbol.upper()}_prices.csv")
        write_to_csv(rows, csv_file_path)
    
        
        # "w" means "open the file for writing"
    
            #for date in dates:
            #    daily_prices = tsd[date]
            #    writer.writerow({
            #        "timestamp": date,
            #        "open": to_usd(float(daily_prices["1. open"])),
            #        "high":to_usd(float(daily_prices["2. high"])),
            #        "low": to_usd(float(daily_prices["3. low"])),
            #        "close": to_usd(float(daily_prices["4. close"])),
            #        "volume": daily_prices["5. volume"] #string
            #    })
    
    
    lines()
    print(f"SELECTED SYMBOL: {symbol.upper()}")
    lines()
    print("REQUESTING STOCK MARKET DATA...")
    lines()
    print(f"REQUEST AT: {current_friendly_time}")
    print(f"LATEST DAY: {last_refreshed}")
    lines()
    print(f"LATEST CLOSE: {to_usd(latest_close)}")
    print(f"RECENT HIGH: {to_usd(recent_high)}")
    print(f"RECENT LOW: {to_usd(recent_low)}")
    lines()
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
    print(f"WRITING DATA TO CSV: {csv_file_path}...")
    lines()
    
    again=str(input("Do you want information on another stock? [y/n] ")) #https://stackoverflow.com/questions/26961427/asking-the-user-if-they-want-to-play-again 
    if again.lower() == "yes" or again.lower() == "y":
        run = True 
    else:
        print("HAPPY INVESTING!")
        quit()
    lines()
    
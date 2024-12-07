from tweet_scraper import scrape
from data_cleaning import clean_data
from vader import vader_analyze
from historical import get_stock_data

try:
    scrape()
except:
    print("Rate limit exceeded. Please try again later.")
clean_data()
print("\nToday's score:", vader_analyze())

prices = get_stock_data()
print("\nToday's opening price for NVDA:", prices['today_open'])
# print("Yesterday's closing price:", prices['yesterday_close'])
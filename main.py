import json
import datetime
from csv import writer
from tweet_scraper import scrape
from news_scaper import scrape_news
from data_cleaning import clean_data
from vader import vader_analyze
from historical import get_stock_data

f = open('scraper_config.json')
config = json.load(f)
symbol = config['symbols'][0][1:]

tweet_csv = open('results.csv', 'a')
writer_object = writer(tweet_csv)

try:
    scrape()
except:
    print("Tweet rate limit exceeded. Please try again later.")
clean_data()

try:
    pass
    # scrape news
except:
    print("News rate limit exceeded. Please try again later.")
# clean news data

vader_score = vader_analyze()
print("\nToday's score:", vader_score)

bert_score = # call bert function
# print bert score or however its formatted

prices = get_stock_data()
print(f"\nToday's opening price for {symbol}: {prices['today_open']}")

# replace underscore with bert score and other bert data, will need to modify results.csv for right column names
writer_object.writerow([datetime.date.today(), symbol, vader_score, _______, 'NA', prices['yesterday_close'], prices['today_open']])
print("\nData saved to results.csv")
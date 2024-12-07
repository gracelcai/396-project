from tweet_scraper import scrape
from data_cleaning import clean_data
from vader import vader_analyze

try:
    scrape()
except:
    print("Rate limit exceeded. Please try again later.")

clean_data()
print("\nToday's score:", vader_analyze())
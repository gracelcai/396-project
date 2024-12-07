from tweet_scraper import scrape
from data_cleaning import clean_data
from vader import vader_analyze

scrape()
clean_data()
print("\nToday's score:", vader_analyze())
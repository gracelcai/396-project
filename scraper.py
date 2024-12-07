import asyncio
import json
from csv import writer
from twikit import Client

USERNAME = 'DevinLave43610'
EMAIL = 'devinlave02@gmail.com'
PASSWORD = 'CMSC396HProject'

f = open('scraper_config.json')
config = json.load(f)

tweet_csv = open('tweets.csv', 'a')
writer_object = writer(tweet_csv)

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    
    for _ in range (10):
        for symbol in config['symbols']:
            print(f"\nGetting data for {symbol}...")
            data = await client.search_tweet(query=symbol, product='Media', count=20)
            for tweet in data:
                tweet_data = []
                tweet_data.append(tweet.id)
                tweet_data.append(tweet.user.verified)
                tweet_data.append(tweet.created_at_datetime)
                tweet_data.append(tweet.lang)
                tweet_data.append(tweet.favorite_count)
                tweet_data.append(tweet.retweet_count)
                tweet_data.append(tweet.view_count)
                tweet_data.append(tweet.text)
                
                writer_object.writerow(tweet_data)
                            
asyncio.run(main())
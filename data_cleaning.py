import pandas as pd
import json
from datetime import datetime, timedelta

def clean_data():
    f = open('scraper_config.json')
    config = json.load(f)

    df = pd.read_csv('tweets.csv')
    df.drop_duplicates(subset=["id"], inplace=True)

    df = df[df['lang'] == 'en']

    lookback = config['lookback_window']
    cutoff_date = datetime.now() - timedelta(days=lookback)
    df['time'] = df['time'].apply(lambda x: x[:-6])
    df["time"] = pd.to_datetime(df["time"])
    df = df[df['time'] >= cutoff_date]

    df.to_csv('tweets.csv', index=False)

    print("Data cleaning complete")
    print("Number of usable tweets:", len(df))
    
clean_data()
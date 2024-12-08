import pandas as pd

def clean_data():
    df = pd.read_csv('tweets.csv')
    df.drop_duplicates(subset=["id"], inplace=True)

    df = df[df['lang'] == 'en']

    df['time'] = df['time'].apply(lambda x: x[:-6])
    df["time"] = pd.to_datetime(df["time"], format="ISO8601", utc=False)
    
    df.to_csv('tweets.csv', index=False)

    print("\nData cleaning complete")
    print("Number of usable tweets:", len(df))
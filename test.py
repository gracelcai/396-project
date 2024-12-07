import pandas as pd

df = pd.read_csv('tweets.csv')

print((pd.to_datetime(df['time']).dt.date).value_counts())
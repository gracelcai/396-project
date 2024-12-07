import yfinance as yf
import pandas as pd
import json
from datetime import datetime, timedelta

f = open('scraper_config.json')
config = json.load(f)
ticker_symbol = config['symbols'][0][1:]
lookback_window = config['lookback_window']

end_date = datetime.today().strftime('%Y-%m-%d')  # Today's date
start_date = (datetime.today() - timedelta(days=lookback_window)).strftime('%Y-%m-%d')

ticker_data = yf.Ticker(ticker_symbol)
stock_data = ticker_data.history(start=start_date, end=end_date)

output_data = pd.DataFrame()

if 'Adj Close' in stock_data.columns:
    output_data['Adjusted Closing Price'] = stock_data['Adj Close']
elif 'Close' in stock_data.columns:
    output_data['Closing Price'] = stock_data['Close']

if 'Open' in stock_data.columns:
    output_data['Opening Price'] = stock_data['Open']

if not output_data.empty:
    csv_filename = f"{ticker_symbol}.csv"
    output_data.to_csv(csv_filename, index=True)
    print(f"Data saved to {csv_filename}")
import yfinance as yf
import pandas as pd
import json
from datetime import datetime, timedelta

def get_stock_data():
    with open('scraper_config.json') as f:
        config = json.load(f)
    ticker_symbol = config['symbols'][0][1:]
    
    today = datetime.today()
    yesterday = today - timedelta(days=1)

    ticker_data = yf.Ticker(ticker_symbol)
    stock_data = ticker_data.history(start=yesterday.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))
    
    if 'Open' in stock_data.columns and 'Close' in stock_data.columns:
        today_open = stock_data['Open'].iloc[-1] if not stock_data.empty else None
        yesterday_close = stock_data['Close'].iloc[0] if not stock_data.empty else None
    else:
        today_open = None
        yesterday_close = None

    return {
        "today_open": today_open,
        "yesterday_close": yesterday_close
    }

# print(get_stock_data())

# output_data = pd.DataFrame()

# if 'Adj Close' in stock_data.columns:
#     output_data['Adjusted Closing Price'] = stock_data['Adj Close']
# elif 'Close' in stock_data.columns:
#     output_data['Closing Price'] = stock_data['Close']

# if 'Open' in stock_data.columns:
#     output_data['Opening Price'] = stock_data['Open']

# if not output_data.empty:
#     csv_filename = f"{ticker_symbol}.csv"
#     output_data.to_csv(csv_filename, index=True)
#     print(f"Data saved to {csv_filename}")
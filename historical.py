import yfinance as yf
import pandas as pd

ticker_symbol = 'TSLA'
start_date = '2022-08-01'
end_date = '2022-12-31'

ticker_data = yf.Ticker(ticker_symbol)
stock_data = ticker_data.history(start=start_date, end=end_date)

print("Available columns:", stock_data.columns)

if 'Adj Close' in stock_data.columns:
    adjusted_close_data = stock_data[['Adj Close']]
    adjusted_close_data.rename(columns={'Adj Close': 'Adjusted Closing Price'}, inplace=True)
elif 'Close' in stock_data.columns:
    adjusted_close_data = stock_data[['Close']]
    adjusted_close_data.rename(columns={'Close': 'Adjusted Closing Price'}, inplace=True)
else:
    print("No suitable columns found for adjusted or regular closing prices.")
    adjusted_close_data = None

if adjusted_close_data is not None:
    csv_filename = 'TSLA_adjusted_close_aug_dec_2022.csv'
    adjusted_close_data.to_csv(csv_filename, index=True)
    print(f"Data saved to {csv_filename}")
else:
    print("Data could not be saved due to missing closing price columns.")

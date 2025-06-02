# src/data/market_loader.py

import yfinance as yf
import pandas as pd
import numpy as np


def fetch_price_data(tickers, start_date="2018-01-01", end_date=None):
    """
    Downloads Adjusted Close prices using yfinance for a list of tickers.

    Returns:
    - DataFrame of daily adjusted close prices
    """
    data = yf.download(tickers, start=start_date, end=end_date)

    # Handle single vs multiple ticker formats
    if isinstance(data.columns, pd.MultiIndex) and 'Adj Close' in data.columns.levels[0]:
        prices = data['Adj Close']
    elif 'Adj Close' in data.columns:
        prices = data[['Adj Close']]
    else:
        raise KeyError("'Adj Close' not found in yfinance data output")

    if prices.empty:
        raise ValueError("No data fetched from yfinance. Check ticker symbols or rate limits.")

    return prices.dropna()


def calculate_log_returns(price_df):
    """
    Calculates daily log returns from prices.
    """
    return np.log(price_df / price_df.shift(1)).dropna()

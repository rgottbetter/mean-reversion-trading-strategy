import yfinance as yf
import pandas as pd 
from datetime import datetime

start_date = datetime(2024, 12, 1)
end_date = datetime(2025, 12, 1)
def load_data(ticker_symbol, start_date: date, end_date: date):
  

  if isinstance(ticker_symbol, str):
    tickers = [tickers]

  data = yf.download(tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
        group_by="column",
                    )
  if data.empty:
    raise ValueError("No data returned from Yahoo Finance. Check tickers/dates.")

  
  

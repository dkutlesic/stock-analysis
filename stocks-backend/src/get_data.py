"""
Fetches the stock data and inserts it into the database
"""
import yfinance as yf
from stocks_of_interest import stock_names
import pandas as pd

# path to artificial data (created to test front-end real-time frontend)
OUTPUT_PATH_TO_MOCK_DATA = '../tests/mock_data.csv'

def get_mock_data() -> pd.DataFrame:
    """
    created to test front-end and data processing
    """
    mock_data = pd.read_csv(OUTPUT_PATH_TO_MOCK_DATA)
    mock_data['date'] = pd.to_datetime(mock_data['date'])
    return mock_data

def get_sorted_stocks_data() -> pd.DataFrame:
    """
    obtain the newest stock values (from yfinance)
    process it to obtain stock name, date in expected form and stock value

    Returns stock name, stock value and date (sorted by date)
    """
    yt_data = yf.download(stock_names, period='2wk')['Close']
    per_stock_data = yt_data.reset_index().melt(id_vars=['Date'], value_vars=stock_names, var_name='name', value_name='value')
    per_stock_data['date'] = per_stock_data['Date'].dt.date
    per_stock_data.sort_values('date', inplace=True)
    return per_stock_data[['name', 'value', 'date']]


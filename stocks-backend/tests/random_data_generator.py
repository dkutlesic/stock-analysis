"""
File used to test frontend and data fetching
It generates random data with increasing dates and random stock values
"""
import sys
sys.path.append('../src')

import pandas as pd
from datetime import datetime, timedelta
import random
import time
from stocks_of_interest import stock_names

OUTPUT_PATH_TO_MOCK_DATA = './mock_data.csv'

def generate_random_dataframe(start_date, end_date, stock_name):
    dates = pd.date_range(start=start_date, end=end_date).tolist()
    values = [random.randint(0, 100) for _ in range(len(dates))]
    df = pd.DataFrame({'date': dates, 'value': values, 'name': [stock_name]*len(dates)})
    return df

start_date = datetime(2023, 3, 1)
end_date = start_date + timedelta(days=9)

while True:
    # sometimes skip some days to mock weekends and holidays or return the same day as the last day
    skip_days = random.choices([0, 1, 2], weights=[3, 4, 1])[0]
    start_date += timedelta(days=skip_days)
    end_date += timedelta(days=skip_days)
    
    all_dfs = []
    for stock_name in stock_names:
        df = generate_random_dataframe(start_date, end_date, stock_name)
        all_dfs.append(df)
    
    combined_df = pd.concat(all_dfs, ignore_index=True)
    combined_df.to_csv(OUTPUT_PATH_TO_MOCK_DATA, index=False)
    
    time.sleep(10)

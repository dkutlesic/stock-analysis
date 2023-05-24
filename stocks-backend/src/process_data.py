"""
Exposes json values used for creating the plot and the table
"""

from flask import Flask, jsonify, Response
from flask_cors import CORS
from datetime import datetime
import numpy as np
import pandas as pd
import os
from get_data import get_sorted_stocks_data, get_mock_data

app = Flask(__name__)
CORS(app)

GET_DATA_FUNCTION = get_sorted_stocks_data

# approximation for the number of trading days in a year
TRADING_DAYS = 252
PLOT_STARTING_VALUE = 100

@app.route('/graph', methods=['GET'])
def stocks():
    """
    Returns the normalized stock values, stock name and date
    """
    # fetch data
    stock_data = GET_DATA_FUNCTION()
    columns_to_provide = ['name', 'date', 'normalized_value']
    
    # set the starting value to 100 to allow for easier comparison

    # get earliest value for each stock
    earliest_dates = stock_data.groupby('name')['date'].min().reset_index()
    earliest_values = pd.merge(earliest_dates, stock_data, on=['name', 'date'], how='inner')[['name', 'value']]\
                               .set_index('name')['value'].to_dict()
    stock_data['normalized_value'] = stock_data.apply(
        lambda row : row['value'] - earliest_values[row['name']] + PLOT_STARTING_VALUE, axis=1) 

    # convert date column to string, so it can be directly converted to json 
    
    stock_data['date'] = stock_data['date'].map(lambda x : datetime.strftime(x, '%Y-%m-%d')) 

    return Response(stock_data[columns_to_provide].to_json(orient='records'), mimetype='application/json')

@app.route('/statistics', methods=['GET'])
def get_statistics():
    """
    Returns stock name, cumulative return, annualized return and annualized volatility
    """
    # fetch data
    stock_data = GET_DATA_FUNCTION()
    grouped_data = stock_data.groupby('name')

    # calculate cumulative returns, annualized returns and annualized volatility (for each stock)
    results = []
    for name, group in grouped_data:
        stock_values = group['value'].values
        daily_returns = np.diff(stock_values) / stock_values[:-1]
        cumulative_return = np.prod(1 + daily_returns) - 1
        annualized_return = (1 + cumulative_return) ** (TRADING_DAYS / len(stock_values)) - 1
        annualized_volatility = np.std(daily_returns) * np.sqrt(TRADING_DAYS)

        # set inf or nan values to 0
        results.append({
            'name': name,
            'cumulative_return': cumulative_return if not np.isnan(cumulative_return) and not np.isinf(cumulative_return) else 0,
            'annualized_return': annualized_return if not np.isnan(annualized_return) and not np.isinf(annualized_return) else 0,
            'annualized_volatility': annualized_volatility if not np.isnan(annualized_volatility) and not np.isinf(annualized_volatility) else 0
        })

    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
    #app.run(port=8000, debug=True)

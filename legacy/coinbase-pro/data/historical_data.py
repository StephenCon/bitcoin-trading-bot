# data/historical_data.py

import pandas as pd
from utils.api_utils import coinbase_pro_request

def fetch_price_data(symbol, interval, lookback):
    """
    Fetch historical price data from the Coinbase Pro API.

    Args:
        symbol (str): The trading pair symbol, e.g., 'BTC-GBP'.
        interval (int): The granularity of the data in seconds.
        lookback (int): The number of data points to retrieve.

    Returns:
        DataFrame: A Pandas DataFrame containing the historical price data.
        
    Raises:
        Exception: If the API request fails.
    """
    endpoint = f"/products/{symbol}/candles?granularity={interval}"
    response = coinbase_pro_request('GET', endpoint)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
        return df.sort_values('time')
    else:
        raise Exception("Failed to fetch data: " + response.text)

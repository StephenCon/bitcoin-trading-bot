# strategies/moving_average.py

import pandas as pd


def calculate_sma(dataframe, period):
    """
    Calculate the Simple Moving Average (SMA) of a DataFrame.

    Args:
        dataframe (DataFrame): A Pandas DataFrame containing price data with a 'close' column.
        period (int): The number of periods to use for the SMA calculation.

    Returns:
        Series: A Pandas Series containing the SMA values.
    """
    return dataframe['close'].rolling(window=period).mean()


def generate_signals(dataframe, sma_period):
    """
    Generate buy/sell signals based on the SMA strategy.

    Args:
        dataframe (DataFrame): A Pandas DataFrame containing price data with a 'close' column.
        sma_period (int): The number of periods for the SMA calculation.

    Returns:
        DataFrame: A modified DataFrame with buy/sell signals and positions.
    """
    dataframe['sma'] = calculate_sma(dataframe, sma_period)
    dataframe['signal'] = 0
    dataframe['signal'][sma_period:] = dataframe['close'][sma_period:] > dataframe['sma'][sma_period:]
    dataframe['position'] = dataframe['signal'].diff()
    return dataframe

# main.py

from data.historical_data import fetch_price_data
from strategies.moving_average import generate_signals
from execution.trade_executor import execute_trade
from config import settings

def main():
    try:
        # Fetch historical data
        df = fetch_price_data(settings.TRADE_SYMBOL, 3600, 300)  # Example: 1-hour granularity, 300 data points

        # Apply SMA trading strategy
        df_with_signals = generate_signals(df, 20)  # Example: 20 periods for SMA

        # Check the last row for a signal
        latest_signal = df_with_signals.iloc[-1]['position']

        # Execute a trade if there's a valid signal
        if latest_signal == 1:  # Buy signal
            execute_trade(1, settings.TRADE_SYMBOL, settings.TRADE_QUANTITY)
        elif latest_signal == -1:  # Sell signal
            execute_trade(-1, settings.TRADE_SYMBOL, settings.TRADE_QUANTITY)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

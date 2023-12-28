# execution/trade_executor.py

from utils.api_utils import coinbase_pro_request
from config import settings

def execute_trade(signal, product_id, size):
    """
    Execute a market order on Coinbase Pro based on a trading signal.

    Args:
        signal (int): The trading signal (-1 for sell, 1 for buy).
        product_id (str): The trading pair symbol, e.g., 'BTC-GBP'.
        size (float): The quantity of cryptocurrency to trade.

    Returns:
        dict: The response from the Coinbase Pro API in JSON format, containing order details.
    """
    if signal == 1:
        order_type = 'buy'
    elif signal == -1:
        order_type = 'sell'
    else:
        return

    order = {
        'type': 'market',
        'product_id': product_id,
        'size': size
    }

    response = coinbase_pro_request('POST', '/orders', order)
    return response.json()

# utils/api_utils.py

import hmac
import time
import hashlib
import base64
import requests
from config import settings

def coinbase_pro_request(method, path, body=''):
    timestamp = str(time.time())
    message = timestamp + method + path + (body if body else '')
    hmac_key = base64.b64decode(settings.API_SECRET)
    signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode()

    headers = {
        'CB-ACCESS-KEY': settings.API_KEY,
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-PASSPHRASE': settings.API_PASSPHRASE,
        'Content-Type': 'application/json'
    }

    return requests.request(method, settings.BASE_URL + path, headers=headers, json=body)

# Example usage: fetching account information
# response = coinbase_pro_request('GET', '/accounts')
# print(response.json())

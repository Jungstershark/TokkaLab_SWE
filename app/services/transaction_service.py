import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
ETHERSCAN_API_URL = 'https://api.etherscan.io/api'
BINANCE_API_URL = 'https://api.binance.com/api/v3/klines'

def get_transaction_fee(tx_hash):
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640',
        'sort': 'asc',
        'apikey': ETHERSCAN_API_KEY
    }
    response = requests.get(ETHERSCAN_API_URL, params=params)
    data = response.json()
    
    print("Etherscan API response:", data)  # Debug print

    for txn in data['result']:
        print("Processing transaction:", txn['hash'])  # Debug print
        if txn['hash'] == tx_hash:
            eth_price = get_eth_price(int(txn['timeStamp']))
            fee_eth = int(txn['gasUsed']) * int(txn['gasPrice']) / 10**18
            fee_usdt = fee_eth * eth_price
            return {'transaction_fee_usdt': fee_usdt}

    return {'error': 'Transaction not found'}

def get_historical_fees(start_time, end_time):
    # Implement batch processing logic here
    pass

def get_eth_price(timestamp):
    params = {
        'symbol': 'ETHUSDT',
        'interval': '1m',
        'startTime': timestamp * 1000,
        'endTime': (timestamp + 60) * 1000
    }
    response = requests.get(BINANCE_API_URL, params=params)
    data = response.json()

    if len(data) > 0:
        return float(data[0][4])  # Close price

    return None

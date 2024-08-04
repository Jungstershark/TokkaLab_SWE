import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
ETHERSCAN_API_URL = 'https://api.etherscan.io/api'

def fetch_etherscan_data():
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640',
        'sort': 'asc',
        'apikey': ETHERSCAN_API_KEY
    }
    response = requests.get(ETHERSCAN_API_URL, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    data = fetch_etherscan_data()
    print(data)

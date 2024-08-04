# Uniswap Transaction Fee API

## Introduction
This project provides an API to retrieve transaction fees in USDT for Uniswap WETH-USDC transactions.

## Requirements
- Python 3.9+
- Docker

## Setup

### Local Setup
1. Clone the repository:
   ```cmd
   git clone https://github.com/your-username/uniswap-transaction-fee.git
   cd uniswap-transaction-fee

2. Set up a virtual environment:
    ```cmd
    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt

3. Run the application:
    ```cmd
    python app/app.py

### Docker Setup
1. Build and run the Docker containers:
    ```cmd
    docker-compose up --build

## API Endpoints
'GET /api/transaction/<tx_hash>': Get transaction fee for a specific transaction.
'POST /api/transactions/historical': Get transaction fees for a given time period.

## Testing
1. Run the tests:
    ```cmd
    python -m unittest discover tests

## Design Considerations
- The application is designed to handle both real-time and batch processing of transaction data.
- The system is dockerized for easy deployment and scalability.

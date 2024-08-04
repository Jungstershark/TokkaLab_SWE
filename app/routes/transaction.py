from flask import Blueprint, request, jsonify
from app.services.transaction_service import get_transaction_fee, get_historical_fees

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transaction/<string:tx_hash>', methods=['GET'])
def transaction_fee(tx_hash):
    fee = get_transaction_fee(tx_hash)
    return jsonify(fee), 200

@transaction_bp.route('/transactions/historical', methods=['POST'])
def historical_fees():
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    fees = get_historical_fees(start_time, end_time)
    return jsonify(fees), 200

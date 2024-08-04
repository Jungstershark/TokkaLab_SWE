import unittest
from app.services.transaction_service import get_transaction_fee

class TestTransactionService(unittest.TestCase):

    def test_get_transaction_fee(self):
        tx_hash = '0x8395927f2e5f97b2a31fd63063d12a51fa73438523305b5b30e7bec6afb26f48'
        fee = get_transaction_fee(tx_hash)
        self.assertIn('transaction_fee_usdt', fee)

if __name__ == '__main__':
    unittest.main()

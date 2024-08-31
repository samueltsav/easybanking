from datetime import datetime
import uuid

from account import Account, accounts
from loan import Loan, loans

transactions = {}
transaction_history = []

class Transaction:
    def __init__(self, amount, user_id):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.amount = amount

    def deposit(amount):
        if amount > 0: 
            balance += amount
            return balance
        return False

    def withdraw(amount):
        if 0 < amount <= balance:
            balance -= amount
            return True
        return False

    def transfer(target_account, amount):
        if Transaction.withdraw(amount):
            target_account.deposit(amount)
            Transaction.record_transaction('Transfer', amount, target_account.id)
            return True
        return False
    
    def record_transaction(self, type, amount, target_account_id=None):
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Transaction[transaction_id] = {
            'account_id': self.id,
            'type': type,
            'amount': amount,
            'target_account_id': target_account_id,
            'timestamp': timestamp
        }
        self.transaction_history.append(transaction_id)


    def transaction_history(account_id):
        for tx_id, tx in transactions.items():
            if tx['account_id'] == account_id:
                print(f"Transaction ID: {tx_id}, Type: {tx['type']}, Amount: ${tx['amount']:.2f}, "
                  f"Target Account ID: {tx['target_account_id']}, Timestamp: {tx['timestamp']}")

"""def __str__(self):
        return f"Account ID: {self.id}, Name: {self.name}, Balance: ${self.balance:.2f}" """
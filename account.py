from user import User, sessions, users
from transaction import Transaction, transaction_history
import uuid

accounts = {}

class Account:
    def __init__(self, user_id, name, session_id, initial_balance=0):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.name = name
        self.balance = initial_balance
    
    def create_account(session_id, name, initial_balance):
        username = sessions.get(session_id)
        if username:
            user = users.get(username)
            account = Account(user.id, name, initial_balance)
            accounts[account.id] = account
            return account.id
        return None
    
    def get_account(account_id):
        return accounts.get(account_id)
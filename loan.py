from datetime import datetime
import uuid
from account import accounts

loans = {}

class Loan:
    def __init__(self, account_id, amount, interest_rate):
        self.id = str(uuid.uuid4())
        self.account_id = account_id
        self.amount = amount
        self.interest_rate = interest_rate
        self.status = 'Active'
        self.issue_date = datetime.now()

    def repay(self, amount):
        if amount >= self.amount * (1 + self.interest_rate):
            self.status = 'Closed'
            return True
        return False

    def __str__(self):
        return (f"Loan ID: {self.id}, Account ID: {self.account_id}, Amount: ${self.amount:.2f}, "
                f"Interest Rate: {self.interest_rate:.2%}, Status: {self.status}, Issue Date: {self.issue_date}")
    
    def create_loan(account_id, amount, interest_rate):
        if account_id in accounts and amount > 0 and 0 <= interest_rate <= 1:
            loan = Loan(account_id, amount, interest_rate)
            loans[loan.id] = loan
            return loan.id
        return None

    def get_loan(loan_id):
        return loans.get(loan_id)
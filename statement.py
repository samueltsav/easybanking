class Statement:
    def __init__(self, account, transaction_history):
        self.account = account
        self.transaction_history = transaction_history

    def generate_statement(self):
        statement = f"Statement for Account: {self.account.account_number}\n"
        statement += f"Balance: {self.account.get_balance()}\n"
        statement += "Transactions:\n"
        for transaction in self.transaction_history.get_transaction_history():
            statement += f"{transaction.date} - {transaction.transaction_type}: {transaction.amount} - {transaction.description}\n"
        return statement

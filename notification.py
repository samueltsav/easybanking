class NotificationService:
    def send_alert(self, user, message):
        print(f"Alert for {user.username}: {message}")

    def send_transaction_alert(self, user, transaction):
        message = f"Transaction Alert: {transaction.amount} {transaction.transaction_type} on {transaction.date}. Description: {transaction.description}."
        self.send_alert(user, message)
        
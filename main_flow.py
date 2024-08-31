import random

from user import User
from account import Account, accounts
from loan import Loan
from transaction import Transaction, transactions
from customer_service import Customer

def main():
    while True:
        print("\nBanking Application")
        print("1. Create User")
        print("2. Login")
        print("3. Logout")
        print("4. Create Account")
        print("5. View Account")
        print("6. Deposit")
        print("7. Withdraw")
        print("8. Transfer")
        print("9. Take Loan")
        print("10. Repay Loan")
        print("11. Check Loan Record")
        print("12. View Transactions")
        print("13. View Customer Service Requests")
        print("14. Create Customer Service Request")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(User.create_user(username, password))

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            session_id = User.login(username, password)
            if session_id:
                print(f"Login successful! Session ID: {session_id}")
            else:
                print("Incorrect login details.")

        elif choice == '3':
            session_id = input("Enter session ID: ")
            if User.logout(session_id):
                print("Thank you for banking with us. Bye!")
            else:
                print("Unable to log you out. Please try again.")

        elif choice == '4':
            session_id = input("Enter session ID: ")
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter amount to deposit: "))
            account_id = Account.create_account(session_id, name, initial_balance)
            if account_id:
                print(f"Account created successfully! Account ID: {account_id}")
            else:
                print("Account creation failed. Please login first.")

        elif choice == '5':
            account_id = input("Enter account ID: ")
            account = Account.get_account(account_id)
            if account:
                print(account)
            else:
                print("Account not found.")

        elif choice == '6':
            account_id = input("Enter account ID: ")
            amount = float(input("Initial deposit: "))
            account = Account.get_account(account_id)
            if account and Transaction.deposit(amount):
                print("Deposit successful! New balance: {balance}")
            else:
                print("Operation1 failed.")

        elif choice == '7':
            account_id = input("Enter account ID: ")
            amount = float(input("Enter withdrawal amount: "))
            account = Account.get_account(account_id)
            if account and Transaction.withdraw(amount):
                print("Withdrawal successful!")
            else:
                print("Withdrawal failed.")

        elif choice == '8':
            from_account_id = input("Enter your account ID: ")
            to_account_id = input("Enter target account ID: ")
            amount = float(input("Enter transfer amount: "))
            from_account = Account.get_account(from_account_id)
            to_account = Account.get_account(to_account_id)
            if from_account and to_account and from_account.transfer(to_account, amount):
                print("Transfer successful!")
            else:
                print("Transfer failed.")

        elif choice == '9':
            account_id = input("Enter account ID: ")
            amount = float(input("Enter loan amount: "))
            interest_rate = float(input("Enter interest rate (as decimal): "))
            loan_id = Loan.create_loan(account_id, amount, interest_rate)
            if loan_id:
                print(f"Loan created successfully! Loan ID: {loan_id}")
            else:
                print("Loan creation failed.")

        elif choice == '10':
            loan_id = input("Enter loan ID: ")
            amount = float(input("Enter repayment amount: "))
            loan = Loan.get_loan(loan_id)
            if loan and loan.repay(amount):
                print("Loan repaid successfully!")
            else:
                print("Repayment failed.")

        elif choice == '11':
            loan_id = input("Enter loan ID: ")
            loan = Loan.get_loan(loan_id)
            if loan:
                print(loan)
            else:
                print("Loan not found.")

        elif choice == '12':
            account_id = input("Enter account ID: ")
            Transaction.list_transactions(account_id)

        elif choice == '13':
            Customer.list_customer_service_requests()

        elif choice == '14':
            description = input("Enter customer service request description: ")
            request_id = Customer.create_customer_service_request(description)
            print(f"Customer service request created! Request ID: {request_id}")

        elif choice == '15':
            print("Thanks for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
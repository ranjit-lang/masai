class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account {self.account_number} - {self.name}: Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit=0):
        if account_number in self.accounts:
            print("Account with this number already exists.")
        else:
            new_account = Account(account_number, name, initial_deposit)
            self.accounts[account_number] = new_account
            print(f"Account created for {name}. Account Number: {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def display_all_accounts(self):
        if self.accounts:
            print("\nAll Accounts:")
            for account in self.accounts.values():
                account.display_balance()
        else:
            print("No accounts available.")


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder's name: ")
            account_number = input("Enter a unique account number: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(account_number, name, initial_deposit)
        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.display_balance()
            else:
                print("Account not found.")
        elif choice == "5":
            bank.display_all_accounts()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

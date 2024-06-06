class Bank_Account:
     def __init__(self, account_number, account_balance=0):
        self.account_number = account_number
        self.account_balance = account_balance

     def deposit(self, amount):
        self.account_balance += amount
        print(f"You have deposited #{amount} to account {self.account_number}. Current balance: #{self.account_balance}")

     def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"You have Withdrew #{amount} from account {self.account_number}. Current balance: #{self.account_balance}")
        else:
            print("Insufficient funds")

     def transfer(self, recipient, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            recipient.account_balance += amount
            print(f"You have transferred #{amount} from account {self.account_number} to account {recipient.account_number}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account {self.account_number} balance: #{self.account_balance}")


class Banking_system:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = Bank_Account(account_number)
            print(f"Account {account_number} created successfully")
        else:
            print("Account already exists")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found")
            return None
def menu():
    bank = Banking_system()

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Balance")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            bank.create_account(account_number)

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)

        elif choice == '4':
            from_account = input("Enter your account number: ")
            to_account = input("Enter recipient's account number: ")
            amount = float(input("Enter amount to transfer: "))
            sender = bank.get_account(from_account)
            recipient = bank.get_account(to_account)
            if sender and recipient:
                sender.transfer(recipient, amount)

        elif choice == '5':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.display_balance()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Error")



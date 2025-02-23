class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def convert_to_dict(self):
        return {'account_number': self.account_number, 'name': self.name, 'balance': self.balance}


class Bank:
    def __init__(self, accounts=None):
        self.accounts = accounts if accounts is not None else {}

    def create_account(self, name, initial_deposit = 0.0):
        account_number = max(self.accounts.keys(), default=0) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        print(f"Account created successfully! Account Number: {account_number}")

    def view_accounts(self, account_number):
        account_number = int(account_number)
        account = self.accounts.get(account_number)
        if account:
            print(f"Account number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account_number = int(account_number)
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account_number = int(account_number)
        if amount < 0:
            raise ValueError("Withdraw amount cannot be negative")
        account = self.accounts.get(account_number)
        if account:
            if account.balance >= amount:
             account.balance -= amount
            else:
                print("Not enough funds.")
        else:
            print("Account not found.")
    def save_to_file(self):
        with open('bank.txt', 'w') as file:
            for account in self.accounts.values():
                account_dict = account.convert_to_dict()
                file.write(f"{account_dict['account_number']},{account_dict['name']},{account_dict['balance']}\n")

    def load_from_file(self):
            self.accounts = {}
            try:
                with open('bank.txt', 'r') as file:
                    for line in file:
                        account_number, name, balance = line.strip().split(',')
                        account = Account(int(account_number), name, float(balance))
                        self.accounts[account.account_number] = account
                print("Accounts loaded from file.")
            except FileNotFoundError:
                print("File not found. Starting with an empty bank.")

print(""""
1. Create an account
2. View an account
3. Deposit
4. Withdraw
5. Save to file
6. Load from file
""")

bank = Bank()
while True:
    n = int(input("choose an option: "))
    if n == 1:
        name = input("enter your name: ")
        deposit = float(input("enter your initial deposit: "))
        bank.create_account(name, deposit)
    elif n == 2:
        account_number = input("enter your account number: ")
        bank.view_accounts(account_number)

    elif n == 3:
        account_number = input("enter your account number: ")
        deposit = float(input("enter your deposit: "))
        bank.deposit(account_number, deposit)
    elif n == 4:
        account_number = input("enter your account number: ")
        amount = float(input("enter your amount: "))
        bank.withdraw(account_number, amount)
    elif n == 5:
        bank.save_to_file()
    elif n == 6:
        bank.load_from_file()
    elif n == 7:
        break
    else:
        print("Invalid input.")
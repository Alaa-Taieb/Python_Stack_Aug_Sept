class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(Transaction("Deposit" , amount))
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
            self.transaction_history.append(Transaction("Withdraw" , amount))
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
            self.transaction_history.append(Transaction("Fee" , -5))
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def display_transaction_history(self):
        max_width = 20
        for trans in self.transaction_history:
            print(f"|{trans.type}"+" "*(8 - len(trans.type))+f"|${trans.amount}"+" "*(max_width - (len(str(trans.amount))+1))+"|")

    def yield_interest(self):
        if self.balance > 0:
            interest = (self.balance * self.int_rate)
            self.balance += interest
            self.transaction_history.append(Transaction("Interest" , interest))
        return self
    

class User:

    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, id, int_rate, amount):
        self.accounts[id] = BankAccount(int_rate , amount)
        return self

    def make_deposit(self,id, amount):
        if id in self.accounts:
            self.accounts[id].deposit(amount)
        else:
            print(f"A bank account with ID {id} doesn't exist.")
        return self
    
    def make_withdrawal(self,id, amount):
        if id in self.accounts:
            self.accounts[id].withdraw(amount)
        else:
            print(f"A bank account with ID {id} doesn't exist.")
        return self
    
    def make_transfer(self, id1 , id2 , amount):
        if id1 in self.accounts and id2 in self.accounts:
            if self.accounts[id1].balance > amount:
                self.accounts[id1].withdraw(amount)
                self.accounts[id2].deposit(amount)
            else:
                print("Insufficient Funds: Charging a $5 fee")
                self.accounts[id1].balance -= 5
        else:
            print(f"One or more IDs provided don't exist.")
        return self

    def display_user_balance(self, id):
        if id in self.accounts:
            self.accounts[id].display_account_info()
        else:
            print(f"A bank account with ID {id} doesn't exist.")
        return self
    
    def display_all_accounts_balance(self):
        for key, account in self.accounts.items():
            print(f"Account ID: {key} | Balance: {account.balance}")
        return self
    

    
user_1 = User("Elon")
user_1.create_account('#1' , 0.02, 10000).create_account('#2', 0.03, 1000)
user_1.make_transfer('#1' , '#2', 500).display_all_accounts_balance().make_transfer('#2' , '#1', 2000).display_all_accounts_balance()

user_1.make_deposit('#1', 1000)
user_1.accounts['#1'].display_transaction_history()
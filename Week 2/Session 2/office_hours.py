class BankAccount:
    all_accounts = []
    def __init__(self, rib):
        self.rib = rib
        self.balance = 0
        self.operation_history = []
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print(f"Deposit: Successfully deposit ${amount}.")
        self.balance += amount
        self.operation_history.append(f"+${amount} - Balance: ${self.balance}")
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            print(f"Withdraw: Successfully withdrew ${amount}.")
            self.balance -= amount
            self.operation_history.append(f"-${amount} - Balance: ${self.balance}")
        else:
            print(f"Withdraw: Failed - Balance = {self.balance}")
        return self
    
    def display_balance(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def print_history(self):
        print("Your operation history: ")
        for operation in self.operation_history:
            print(operation)
        return self
    
    @classmethod
    def print_all_account_rib(cls):
        for account in cls.all_accounts:
            print(account.rib)

    @classmethod
    def print_all_account_history(cls):
        for account in cls.all_accounts:
            print(f"Account RIB: {account.rib}")
            account.print_history()

    @staticmethod
    def test(cls):
        print(cls.all_accounts)

    
a1 = BankAccount("002574")
a2 = BankAccount("002234")
a3 = BankAccount("012574")
a4 = BankAccount("002584")
# a1.display_balance().deposit(100).withdraw(150).withdraw(20).deposit(80).display_balance().print_history()

# BankAccount.print_all_account_history()
##Bank

class Account:
    class attribute:
        type = "savings"
    def __init__(self, account_number, balance, owner):
# instance variables
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
        print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")
    def check_balance(self):
        print(f"The balance of account {self.account_number} is {self.balance}.")


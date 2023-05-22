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
            print("Insufficient     attributes of a count funds.")
        else:
            self.balance -= amount
        print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")
class Account:
    def __init__(self,account_name):
       self.account_name = account_name
       self.balance = 0 
    def deposit (self,amount):
        self.balance += amount
        return f"You have deposited {amount} your new balance is {self.balance}"
    def withdraw (self,amount):
        if self.balance <= amount:
            self.balance -= amount 
            return f"You have withdraw {amount} your new balance is {self.balance}"
        else:
            f"your balance is{self.balance} you cannot withdraw the {amount}"
    
    def check_balance(self):
        return f"The balance of account {self.account_number} is {self.balance}"
# Add attributes deposits and withdrawals in the init method which are empty lists by 
# default and another attribute loan_balance which is zero by default.
class Bank:
    def __init__(self):
        self.deposits = []
        self.withdrawal = []
        self.loan_balance = 0 
#Add a method check_balance which returns the account’s balance
    def check_balance(self):
        total_deposits = sum(self.deposits)
        total_withdrawals = sum(self.withdrawals)
        balance = total_deposits - total_withdrawals - self.loan_balance
        return f"Your currently balance is{balance}"
#Update the deposit method to append each withdrawal transaction to the deposits list.
#  Each transaction should be in form of a dictionary like this  
#{
   #"amount": amount,
   #"narration": “deposit”
#}
    def deposit(self, amount):
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)

    def check_balance(self):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        total_withdrawals = sum(transaction["amount"] for transaction in self.withdrawals)
        balance = total_deposits - total_withdrawals - self.loan_balance
        return balance
#Update the withdrawal method to append each withdrawal transaction to the withdrawals list.
#  Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }

    def withdrawal(self, amount):
        transaction = {
            "amount": amount,
            "narration": "withdrawal"
        }
        self.withdrawals.append(transaction)

    def check_balance(self):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        total_withdrawals = sum(transaction["amount"] for transaction in self.withdrawals)
        balance = total_deposits - total_withdrawals - self.loan_balance
        return balance
    
#Add a new method  print_statement which combines both deposits and withdrawals into one list and,
#  using a for loop, prints each transaction in a new line like this
#deposit - 1000
#withdrawal - 500



    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def check_balance(self):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        total_withdrawals = sum(transaction["amount"] for transaction in self.withdrawals)
        balance = total_deposits - total_withdrawals - self.loan_balance
        return balance
    
#Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
#Account has no outstanding loan
#Loan amount requested is more than 100
#Customer has made at least 10 deposits.
#Amount requested is less than or equal to 1/3 of their total sum of all deposits.
#A successful loan increases the loan_balance by requested amount

  
    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance += amount
                print(f"Loan of {amount} successfully borrowed.")
            else:
                print("Loan amount exceeds the limit.")
        else:
            print("Loan request was not successfull.")
           
#Add a repay_loan method with this functionality
#A customer can repay a loan to reduce the current loan_balance
#Overpayment of a loan increases the accounts current balance
    def repay_loan(self, amount):
        if amount >= self.loan_balance:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.deposit(overpayment)
            print(f"Loan repaid. Overpayment of {overpayment} added to account balance.")
        else:
            self.loan_balance -= amount
            print(f"Loan balance reduced by {amount}.")




    def transfer(self, amount, destination_account):
        if amount <= self.check_balance():
            self.withdrawal(amount)
            destination_account.deposit(amount)
            print(f"Transferred {amount} to destination account.")
        else:
            print("Insufficient balance for transfer.")


class BankAccount:
    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0, acc_type = "checking"): 
        self.int_rate = int_rate
        self.balance = balance
        self.acc_type = acc_type
        BankAccount.all_accounts.append(self)

# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

#withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging $5 fee")
            self.balance -= 5
        return self

#display_account_info(self) - print to the console: 
    def display_account_info(self):
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: {self.balance}")
        return self

# increases balance by balance* interest rate if balance is greater than 0
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+ self.int_rate)
        return self

##class method to print all instances of a Bank Account's info
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

#create 2 accounts
account1 = BankAccount(.01,500)
account2 = BankAccount(.02,800)

#To the first account, make 3 deposits and 1 withdrawal, then calculate interest 
# and display the account's info all in one line of code
account1.deposit(50).deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()

#To the second account, make 2 deposits and 4 withdrawals, then calculate interest 
# and display the account's info all in one line of code (i.e. chaining)
account2.deposit(100).deposit(200).withdraw(10).withdraw(20).withdraw(30).withdraw(40).yield_interest().display_account_info()

print("Calling class method to display all accounts")
BankAccount.all_balances()
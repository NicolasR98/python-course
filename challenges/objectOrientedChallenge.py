"""
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, qty):
        self.balance += qty
        print('Deposit Accepted')

    def withdraw(self, qty):
        if qty > self.balance:
            print('Funds Unavailable!')
            pass
        else:
            self.balance -= qty
            print('Withdrawal Accepted')

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

# 1. Instantiate the class
acct1 = Account('Nicolas',100)

print(acct1)

# Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)


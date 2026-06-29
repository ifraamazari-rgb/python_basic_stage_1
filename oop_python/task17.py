class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance! Withdrawal denied.")



account = BankAccount(1000)

account.deposit(500)

account.withdraw(300)


account.withdraw(1500)
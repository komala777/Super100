class Bank_Account():
    def __init__(self, Name, Account_number, balance=None):
        self.Name = Name
        self.Account_number = Account_number
        self.balance = balance if balance is not None else 0

    def valid_balance(self, amount):
        if amount < 0:
            print("Invalid, Try Again")

    def deposit(self, amount):
        self.valid_balance(amount)
        self.balance += amount
        print("Deposit Amount: {} and Current Balance: {}".format(amount, self.balance))

    def withdraw(self, amount):
        self.valid_balance(amount)
        if self.balance < amount:
            print("Withdrawal not proceed")
        else:
            self.balance -= amount
            print("Withdraw Amount: {} and Current Balance: {}".format(amount, self.balance))

    def display_balance(self):
        self.valid_balance(0)  
        print("Current Balance:", self.balance)


if __name__ == '__main__':
    Transaction = Bank_Account("Jack", "")

    Transaction.deposit(7000)

    Transaction.withdraw(5200)

    Transaction.display_balance()

            
    
    
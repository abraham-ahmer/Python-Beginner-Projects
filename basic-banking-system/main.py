# Write a program that simulates a simple Bank Account: deposit, withdraw, check balance — all handled through an OOP class with error handling.

class BankAccount: 
    def __init__(self, name, pin, balance):
        self.name = name
        self.__pin = pin
        self.balance = balance
    
    def __str__(self):
        return(f"Dear {self.name}. Your pin code is {self.__pin}. And your initial Balance is {self.balance}")  # basic initial printing statement

    def deposit(self, amount): 
        try:
            amount = int(amount) # try to convert in int
        except ValueError:
            raise ValueError("Amount must always be an integar.") # if contains 
        if amount < 1:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Amount deposited: {amount}")
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise ValueError("Amount must always be an integar.")
        if amount > self.balance:
            raise ValueError(f"Cannot withdraw more than your current balance of {self.balance}.")
        self.balance -= amount
        print(f"Amount Withdraw: {amount}")
        print(f"Balance after Withdrawal: {self.balance}")
    
    def check_balance(self):
        print(f"Dear {self.name} your account's final balance is: {self.balance}")
    

acc1 = BankAccount("Abraham Ahmer", 963, 50000)
print(acc1)

try:
    acc1.deposit("s")
except Exception as e:
    print(e)

try:
    acc1.withdraw(2000)
except Exception as e:
    print(e)

acc1.check_balance()

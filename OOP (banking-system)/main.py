# Implement a class BankAccount with methods deposit, withdraw, and get_balance. Add error handling for insufficient funds.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name # name 
        self.balance = balance # balance
    
    
    def get_balance(self):
        return f"Dear {self.name} your current balance is: {self.balance}"  # general print statament.
    
    
    def withdrawal(self, withdraw):
            if withdraw > self.balance:   # if withdrawal amount is more than current balance
                 raise ValueError("Insufficient funds for withdrawal.")  # raise error.
            self.balance -= withdraw   # else, deduct and make that remaining balance
            return f"After withdrawal: {self.balance}"  # then return
    
    
    def deposit(self, add):
        if add < 0:   # if tried to deposit neg amount
             raise ValueError("cant deposit negative amount.") 
        self.balance += add
        return f"After deposit: {self.balance}"
    
    def __str__(self):
         return f"Final balance: {self.balance}"  # final balance
    
    
acc1 = BankAccount("Abraham Ahmer", 20000)  # name and balance
print(acc1.get_balance())  # print gently with str dunder

try: 
    print(acc1.withdrawal(53000))  # try withdrawing, 
except Exception as e:  # if raises an error, gently handle it by printing that statement we put on top
     print(e) 

try:
     print(acc1.deposit(-33))  # try depositing
except Exception as e:  # if tried to deposit neg val, ently handle it by printing that statement we put on top
     print(e)

print(acc1)  # final balance with last str dunder.
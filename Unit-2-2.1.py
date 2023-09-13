class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print(f"Account Number: {self.__account_number}")
    print(f"Account Holder: {self.__account_holder_name}")
    print(f"Account Balance: ₹{self.__account_balance}")


account1 = BankAccount("16583663", "Kumar", 1000.0)
account1.display_balance()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_balance()

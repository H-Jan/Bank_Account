import re

#First is initializing class
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.balance = 0
        self.account_number = account_number
        self.routing_number = routing_number
        self.full_name = full_name
        #balance is zero, will add deposits to increase balance
        #This also takes care of requirement 1

    def deposit (self, amount):
        #this function will take the amount put in as a deposit and will
        #add it to the current balance 
        #This is why we require both the self and amount parameters
        self.balance = self.balance + amount
        print(f"Amount Deposited: ${amount}")

    def withdraw (self, amount):
        #This function will take the amount withdrawn and subtract from the balance
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Amount Withdrawn: ${amount}")
        else:
            self.balance - 10.00
            print("Insufficient Funds!")
            #The If statements allow to differentiate the returning message depending on overall 
            #amount. If the balance is greater than the amount withdrawn, the transaction will 
            #follow, if not, it will deduct ten dollars for insufficient funds. 
        
    def get_balance(self): 
        print(f"Congratulations! Your balance is ${self.balance} ")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance = self.balance + interest
        print(self.balance)
    
    def print_receipt(self):
        #The below variable 'var' was originally a full function found on Stack Overflow, it is simply modified to 
        #to the requirements of this project. 
        var = re.sub('\d', '*', str(self.account_number), 4)
        print(f"{self.full_name} Account NO.: {var} \n Routing NO.: {self.routing_number} \n Balance: ${self.balance}")

    
#Examples
#1
first_account = BankAccount("Hani Jandali", 99233421, 123456789, 100)
first_account.deposit(100)
first_account.withdraw(50)
first_account.print_receipt()
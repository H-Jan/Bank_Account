
#First is initializing class
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.balance = 0
        self.account_number = account_number
        self.routing_number = routing_number
        self.full_name = full_name
        #balance is zero, will add deposits to increase balance

    def deposit (self, amount) 
        #this function will take the amount put in as a deposit and will
        #add it to the current balance 
        #This is why we require both the self and amount parameters
        self.balance = self.balance + amount

    def withdraw(self, amount):
        #This function will take the amount withdrawn and subtract from the balance
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance - 10.00
            print("Insufficient funds")
        
    def print_balance(self):
        return self.balance
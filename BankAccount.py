
#First is initializing class
class BankAccount:
    def __init__(self):
        self.balance = 0
        #balance is zero, will add deposits to increase balance

    def deposit (self, amount) 
        #this function will take the amount put in as a deposit and will
        #add it to the current balance 
        #This is why we require both the self and amount parameters
        self.balance = self.balance + amount

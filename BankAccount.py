
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
        print(f"Amount Deposited: ${amount}"")

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
        var = self.account_number[-4:].rjust(len(self.account_number), '*')
        print(f"{self.full_name} \n Account NO.: {var} \n Routing NO.: {self.routing_number} \n Balance: ${self.balance})
        
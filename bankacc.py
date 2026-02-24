class BankAccount:

    
        
    def __init__(self, Name=None, Balance=0):
       self.Name = Name
       self.__Balance = Balance
    def deposit(self, amount):
        self.__Balance += amount
        print('Amount deposited: ', amount)
        print('Current __Balance: ', self.__Balance)

    def __del__(self):
        print('Bank account has been deleted')

    def deposit(self, amount):
        self.__Balance += amount
        print('Amount deposited: ', amount)
        print('Current __Balance: ', self.__Balance)

    def withdraw(self, amount):
        if self.__Balance >= amount:
            self.__Balance -= amount
            print('Amount withdrawn: ', amount)
            print('Current __Balance: ', self.__Balance)
        else:
            print('Insufficient __Balance')

    def view___Balance(self):
        print('Current __Balance: ', self.__Balance)

    def __eq__ (self, other):
        if self.Name == other.Name:
            return True
        else:
            return False


# --- Testing the BankAccount class --
# Create an account with an initial balance
account1 = BankAccount("ram prasad", 500)
# Test deposit method
account1.deposit(200)     # Expected: balance 

# Test withdraw method (valid withdrawal)
account1.withdraw(300)    # Expected: balance 

# Test withdraw method (invalid withdrawal)
account1.withdraw(1000)   # Expected: Insufficient 

account1._BankAccount__Balance = 100000
# Test view_balance method
account1.view___Balance()   # Expected: prints current 
# balance (400)
# Create another account to test multiple objects
account2 = BankAccount("Jane Smith", 1000)
account2.deposit(500)
account2.view___Balance()   # Expected: 1500
# Delete accounts to trigger destructor
del account1
del account2
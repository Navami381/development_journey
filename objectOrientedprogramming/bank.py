class Bank:
    acc_number:int
    balance:int
    ac_type:int
    custome_name:str

    def __init__(self,acc_number,balance,ac_type,customer_name):

        self.acc_number=acc_number
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name
        print("your account has been created...")

    def deposit(self,amount):
        
        self.balance+=amount
        print(f"your {self.acc_number} has been created with {amount} avilable balance id {self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            raise Exception("Insufficient balance")
        else:
            self.balance-=amount
            print(f"your {self.acc_number} has been debited with {amount} avilable balance id {self.balance}")

    def get_balance(self):
        print("your available balance is=",self.balance)

bank_instance1=Bank(1234,5000,"savings","navami")
bank_instance1.deposit(5000)
bank_instance1.withdraw(1000)
bank_instance1.get_balance()








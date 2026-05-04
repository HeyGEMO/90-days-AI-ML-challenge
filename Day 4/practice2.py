class Account:
    def __init__(self,balance,acc_no):
        self.bal=balance
        self.acc=acc_no
    def debit(self,amount):
        self.bal -= amount
        print("Rs.",amount,"was debited")
        print("total amount :", self.get_balance())
    def credit(self,amount):
        self.bal+= amount
        print("Rs.",amount,"was credted")
        print("total amount :", self.get_balance())
    def get_balance(self):
        return self.bal
acc1=Account(10000, 1234)
acc1.credit(500)
acc1.debit(1000)
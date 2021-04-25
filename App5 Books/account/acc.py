class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    """This class creates checking account objects"""

    type="checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee


jacks_checking=Checking("jack.txt",25)
jacks_checking.deposit(500)
print(jacks_checking.balance)
jacks_checking.commit()

johns_checking=Checking("john.txt",25)
johns_checking.transfer(200)
print(johns_checking.balance)
johns_checking.commit()

print(johns_checking.__doc__)

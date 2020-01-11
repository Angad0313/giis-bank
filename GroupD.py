class Account(object):
   
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.customerName = name
        self.balance = balance
    
    def __str__(x):
         return f' account details: Account number= {x.accountNumber}, name= {x.customerName}, balance={x.balance}'
     
        
    def deposit(self, amount, date):
        if amount>=0:
            self.balance += amount
            print(self)
        else:
            print(str(self)+"\n")
            
        print(str(self)+"\n")
        
    def withdraw(self, amount, date):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(str(self)+"\n")
            class TransactionReport(object):
     
 class TransactionReport(object):
    
     def __init__(self, date, account):
        self.account = account
        self.date= date 
        
     def __str__(y):
        rep = ''
        for a1 in y.translist:
            rep += str(a1)
        return "account={0}, translist{1}".format(y.account, rep)
        
class Bank(object):
    def __init__(self,branch,accounts):
        self.branch=branch
        self.accounts= accounts 
        
    def __str__(y):
        rep = ''
        for s1 in y.accounts:
            rep += str(s1)
        return "branch={0}, accounts{1}".format(y.branch, rep)
    
    def addaccount(self,acc):
        if acc not in self.accounts:
            self.accounts.append(acc)
        else:
            print ("account already exists")
            
    def removeaccount(self,acc):
        if acc in self.accounts:
            self.accounts.remove(acc)
        else:
            print ("account already got removed")
        
    def transfer(self, acc1, acc2, tamount, date):
        if tamount <= acc1.balance:
            print(acc1, acc2)
            print("\t\t " + str(acc1.customerName) + " transferring " + str(tamount) + " to " + str(acc2.customerName))
            acc2.deposit(tamount,date)
            acc1.withdraw(tamount,date)
        else:
            print("\t\t Insufficient Balance to transfer")
            
 

class Account(object):
   
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.customerName = name
        self.balance = balance
    
    def __str__(x):
         return f'\n account details: Account number= {x.accountNumber}, name= {x.customerName}, balance={x.balance}'
                  
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
            
 class Bank(object):
      
     def __init__(self,branches):
        self.branches=branches
        
    def __str__(b):
        rep = ''
        for branch in b.branches:
            rep += str(branch)
        return "\n branches of this bank:{0}".format(rep)
                 
 class Branch(object):
    
    def __init__(self,accounts):
        self.accounts=accounts

    def __str__(y):
        rep = ''
        for customer in y.accounts:
            rep += str(customer)
        return "\n accounts of this branch:{0}".format(rep)
   
  class Transaction(object):
    
    def __init__(self,account,amount,date):
        self.account=account
        self.amount=amount
        self.date=date
        
    def __str__(x):
        return f'\n {x.account}, Amount= {x.amount}, Date={x.date}\n'
    
    def deposit(self, account, amount, time):
        if amount > 0:
            print (f'{account}')
            
            account.balance += amount
            print (f'{account} // {self.amount} was deposited on {self.date} at {time}')
        else:
            print("error, deposit failed")

    def withdraw(self, account, amount, time):
        if account.balance >= amount:
            print (f'{account}')
            
            account.balance -= amount
            print( f'{account} // {self.amount} was withrawn on {self.date} at {time}')
           
        else:
            print("error, withdraw failed")
            
    class Transfer(object):
    
    def __init__(self,acc1,acc2,amount,date):
        self.acc1=acc1
        self.acc2=acc2
        self.amount=amount
        self.date=date
        
    def transferfunction(self, acc1,acc2, amount, time):
        transfer1= Transaction.deposit(self, acc1, amount, time)
        transfer2= Transaction.withdraw(self, acc2, amount, time)
      
        
  class Transactionreport(object):
    
    def __init__(self,transactionList):
        self.transactionList=transactionList
        
    def __str__(transactions):
        rep = ''
        for x in transactions.transactionList:
            rep += str(x)
        return "\n transactions:{0}".format(rep)
    
    def addtransaction(self,trans):
        if trans not in self.transactionList:
            self.transactionList.append(trans)
        else:
            print ("transaction already exists")

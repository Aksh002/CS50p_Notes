#                 Global
#global_variable-
''' 
balance=0
def main():
    print("Balance:",balance)
if __name__=="__main__":
    main()
#this will work fine. U can read the outside declared fxn deposite inside a fxn like main


balance=0
def main():
    print("Balance:",balance)
    deposit(100)
    withdraw(50)
    print("Balance: ",balance)
def deposit(n):
    balance += n
def withdraw(n):
    balance -= n
if __name__=="__main__":
    main()
#This will give the error -"UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value"
#This is bcs    #'if u want to change the fxn,it must be local to the variable'.
                #If u are trying to change a global variable through a def fxn, its not possible.U can only read it,not write to it
  
def main():
    balance=0
    print("Balance:",balance)
    deposit(100)
    withdraw(50)
    print("Balance: ",balance)
def deposit(n):
    balance += n
def withdraw(n):
    balance -= n
if __name__=="__main__":
    main()
#Again it will give error like this- "UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value"
#This time its bcs balance now is a local variable for main fxn, it doesnt exist for deposit and withdraw.
   
#To solve this problem we use the keyword "global",whereever we need to edit the global variable,we will define it as global in fxn
balance=0
def main():
    print("Balance:",balance)
    deposit(100)
    withdraw(50)
    print("Balance: ",balance)
def deposit(n):
    global balance 
    balance += n
def withdraw(n):
    global balance 
    balance-= n
if __name__=="__main__":
    main()

#Corner case- If we hv a local variable with same name as global variable, local one will shadow the global. U can use local without affecting global>Its not preffered though
#If we try to pass in balance as a argument in fxns and change them within the fxn, its only gonna change the local copy of that variable.
'''
#Using OOPs to solve this
class Account:
    def __init__(self):
        self._balance=0
        #we used _ bcs name of instance variable will collide with name of method
    @property
    def balance(self):
        return self._balance
    def deposit(self,n):
        self._balance += n
    def withdraw(self,n):
        self._balance -= n
def main():
    account=Account()
    print("Balance: ",account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ",account.balance)
if __name__=="__main__":
    main()


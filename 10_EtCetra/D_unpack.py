'''
#Basic unpacking
first,_ = input("ENter your name: ").split()
print("First: ",first)

#Doing smthing different 
def total(galleons,sickles,knuts):
    return (galleons*17+sickles)*29+knuts
coins=[100,50,25]
print(total(coins[0],coins[1],coins[2]),"knuts")

#What if we just wanna pass "coins" in the total fxn,it wont here obviously bcs we passing a lists to galleon but nothing to other to arg,they dont hv any value assigned.To gain that royalty
#Just like we previously inpacked the input string we can also unpack the list here
def total(galleons,sickles,knuts):
    return (galleons*17+sickles)*29+knuts
coins=[100,50,25]
print(total(*coins),"knuts")
#"*" here unpacks the list

#It doesnt work with set
#it will only take keys if we do this dict,thats why we use ** to input the obj
def total(galleons,sickles,knuts):
    return (galleons*17+sickles)*29+knuts
coins={"galleons":100,"sickles":50,"knuts":25}
print(total(**coins),"knuts")

#If we type - "def total(galleons=0,sickles=0,knuts=0):",it will pre assign arg as 0 and now we can pass less then 3 arg,code will run

#                         *args,**args
#"*/**" is also used for cases where fxns can take variable no. of arguments
def f(*args,**kwargs):
    print("positional: ",args,kwargs)
f(100,50,25)
#this code will show that clearly that args can accept a whole tupple with varied no. of elements,while kwargs will accept a dictionary.
'''
#we can support both variable no. of positional arguments and no. of named arguments
def f(*args,**kwargs):
    print("named: ",kwargs)
f(galleons=100,sickles=50,knuts=25)
#kwargs is itself a dictionary that contains all the arguments passsed into it
#OUTPUT : "named:  {'galleons': 100, 'sickles': 50, 'knuts': 25}"

#If we see the documentation of "print" fxn,which is -
def print(*objects,sep=" ",end="\n" , ... , ...):
    for object in objects:
        ... #this will make them to iterate over  those variable no. of objects and print each of them
#We can see clearly that print fxnality is based on the concept of *args, it also can take varied no. of objects 
        





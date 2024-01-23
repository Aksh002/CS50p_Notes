#           Constants
#some variable can be declared unchangable/constants in our code
'''
MEOW = 3
for i in range(MEOW):
    print("meow")
#Here MEOW ki value can be changed anytime. I can make it 4 later

class Cat:
    MEOWS=3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow")
cat= Cat()
cat.meow()

#                 type hints
#we can provide hints to python abt what type a variable should be
#and there exist a program that is used to check whether the code is adhering to our own given type hints. It is called "mypy"
#mypy - 
#source - mypy.readthedocs.io
def meow(n):
    for _ in range(n):
        print("Meow")
number=input("Number: ")
meow(number)
#This will give a TypeError bcs input is taken as a str

def meow(n:int):
#here what we are doing in the above line is we are making a type hint for pyhton, not casting n as int, out put here will still be same Error, but we can now apply mypy program to it,it will catch the hints<unlike u idiot>
    for _ in range(n):
        print("Meow")
number=input("Number: ")
meow(number)
#on prompting "mypy <file_name>", we will get the out put as 
    """
    C_meows.py:35: error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type]
    Found 1 error in 1 file (checked 1 source file)
    """

#this helps us to check for type error before deploying the code

#we can add type hints to our varuables too
def meow(n:int):
#here what we are doing in the above line is we are making a type hint for pyhton, not casting n as int, out put here will still be same Error, but we can now apply mypy program to it,it will catch the hints<unlike u idiot>
    for _ in range(n):
        print("Meow")
number:int =input("Number: ")
meow(number)
#Here the output detects error on line where input is taken,it will say we cant assign a variable str if it has to be int, even before the fxn is called, thats why only that one error is diplayed

#if we finally fix the prblm and run the code we will get succes message
def meow(n:int):
    for _ in range(n):
        print("Meow")
number:int =int(input("Number: "))
meow(number)
#output will be-  "Success: no issues found in 1 source file"

#Another instance-
def meow(n:int):
    for _ in range(n):
        print("Meow")
number:int =int(input("Number: "))
meo:str =meow(number)
print("cat: ",meo)
#Here the output on running will give None for last print fxn.This is bcs fxn is not returning any value

#If we do this-
def meow(n:int)->None:
    for _ in range(n):
        print("Meow")
number:int =int(input("Number: "))
meo:str =meow(number)
print("cat: ",meo)
#and pass mypy through it, it will catch the error that we aint retuning any value


#Improving this
def meow(n:int) ->str:
    return "meow \n"*n
    
number:int =int(input("Number: "))
meo:str =meow(number)
print("cat: ",meo,end="")
#now mypy will give succes

#                               DOCSTRING
#We can use """ ________ """ to formally document/write comments into the fxn, generally there are third party tools that u can then use to extract all of these docs/comments help in generating webpages n pdfs for the code
def meow(n:int) ->str:
    """
    Meow n times

    :param n: Number of times to n
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows,one per line
    :rtype: str
    """
    return "meow \n"*n
    
number:int =int(input("Number: "))
meo:str =meow(number)
print("cat: ",meo,end="")

'''
#To modify this program to take the input frm the command line itself
import sys
if len(sys.argv)==1:
    print("meow")
elif len(sys.argv)==3 and sys.argv[1]=="-n":
    # "-n" are called flags they r used as seperator to pass 2 different arguments and still stating they r still connected
    n=int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("Usage: C_meows.py")

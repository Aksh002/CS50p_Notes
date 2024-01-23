#Basics of if,else,elif
'''
#use of or and !=/==
x=float(input("x="))
y=float(input("y="))
if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")

x=float(input("x="))
y=float(input("y="))
if x!=y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#and
score=int(input("Score:-"))
if score>=90 and score<=100:
    print("Grade: A")
elif score>=80 and score<=90:
    print("Grade B")
elif score>=70 and score<=80:
    print ("Grade C")
elif score>=60 and score<=70:
    print("Grade D")
else:
    print("Grade F")

#better way
score=int(input("Score:-"))
if 90<=score<=100:
    print("Grade: A")
elif 80<=score<90:
    print("Grade B")

#another way
score=int(input("Score:-"))
if score>=90:
    print("Grade: A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print ("Grade C")
elif score>=60:
    print("Grade D")
else:
    print("Grade F")

#          MODULO

x=int(input("x="))
#"%" gives remainder 
if x%2==0:
    print("Even")
else:
    print("Odd")

#Better way
def main():
    x=int(input("x="))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
main()
#python has 4 datatypes- int,str,float,bool(boolian values-True,False)

#Better way X 2
def is_even(n):
    return True if n%2==0 else False

#Better way X 3
def is_even(n):
    return n%2==0 

#      MATCH
name=input("Whats your name?")
if name=="Harry" or name=="Harmonie" or name=="Ron":
    print ("Griffindor")
elif name=="Draco":
    print("Slytherin")
else:
    print("Who?")

#Another way using match
name=input("Whats your name?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("who?")
'''

#           RECURSIVE FUNCTION
n=int(input("Factorial of ?="))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(f"factorial of {n} is",factorial(n))
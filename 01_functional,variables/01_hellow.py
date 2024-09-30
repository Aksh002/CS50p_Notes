'''
#            STR

x=input("whats your name?")
print("hellow,",x)

#end
x=input("whats your name?")
print("hellow,",end=" ")
print(x)

#sep
x=input("whats your name?")
print("hellow,", x,sep="!!!")

#to print quotes 
print('"hellow,"')
print("hello, \"vro\"") 

#new way to print
x=input("whats your name?")
print(f"hellow, {x}")

#METHODS(functions used after dots)
#to capitalize and remove whitespaces or unwanted indentation provided through input from string
x=input("whats your name?")
#to remove white space
x=x.strip()
#we can use lstrip and rstrip to remove spaces from respective sides
#to capitalize
x=x.capitalize()
#to capitalize every word
x=x.title()
#to do all at one
x=x.strip().title()
print(f"hellow, {x}")
#shrtcut to do all functions together
x=input("whats your name?").strip().title()
print(f"hellow, {x}")

#split
x=input("whats your name?")
#split user's name into first name and last name
first,last=x.split(" ")
#fxn split objects about what u provide bw double coats
print(f"hellow, {first}")
print(f"hellow, {last}")

#            INT

#"%" sign is usd to find remender after division

#    Coversion of str to int
x=input("x=")
y=input("y=")
z=int(x)+int(y)
print(z)
#we use int(not just a type of data in python but valso a fxn) as fxn to convert str to int type so that 1+2 doesnt give 12 but 3
#shortcut
x=int(input("x="))
y=int(input("y="))
print(x+y)

#            FLOAT

#addition of decimal digits
x=float(input("x="))
y=float(input("y="))
print(x+y)

#    roundoff
#syntax for roundoff is 'round(number[,digits])'
x=float(input("x="))
y=float(input("y="))
z=round(x+y)
print(z)
#rounding off the division to 2 places
x=float(input("x="))
y=float(input("y="))
z=round(x/y,2)
print(z)
#f string approach to round off
x=float(input("x="))
y=float(input("y="))
z=x/y
print(f"{z:.2f}")

#to put coma bw int
x=float(input("x="))
y=float(input("y="))
z=round(x+y)
print(f"{z:,}")

#             DEF
#used to make our own fxn

#basic use
def hellow():
    print("hello")
name=input("Whats ur name?")
hellow()
print(name)

#better use
def hellow(to):
    print("hello,",to)
name=input("Whats ur name?")
hellow(name)
#name is passed as an argument in parenthesis,even though the variable is called Name here, when the function itself is called, the computer assumesthat same value is now called To.
#So Name is essentially copied to another variable called To so that in the context of Hello, I can say Hello to that variable instead.

#diff syntax assigning argument a value
def hellow(to="world"):
    print("hello,",to)
hellow()
#this will print hello world only, even if user input name
    
name=input("Whats ur name?")
hellow(name)

#to keep def fxn in downside of page or to use multiple fxn in combination
def main():
    name=input("Whats ur name?")
    hellow(name)
def hellow(to="world"):
    print("hello,",to)
#now to call fxn we use this
main()

#scope
def main():
    name=input("Whats ur name?")
    hellow()
def hellow():
    print("hello,",name)
main()
#this wont work bcs of a reason called scope.Scope of name is confined to its own def fxn only.So a different def fxn dont know of its existance 


#             RETURN

#
def main():
    x=int(input("What's x?"))
    print("x square is",square(x))
def square(n):
    return n*n #(we can use 'n**2' or 'pow(n,2)' to do the same here)
main()



#                 END   
x=input("whats your name?")
#split user's name into first name and last name
first,secound,last=x.split(" ")
#fxn split objects about what u provide bw double coats
print(first,"...",secound,"...",last)
'''
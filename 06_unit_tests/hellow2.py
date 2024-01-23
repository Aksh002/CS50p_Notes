def main():
    x=input("Whats your name?=")
    hello(x)

'''
def hello(to="World"):
    print("hello",to)

if __name__ == "__main__":
    main()
'''
#This program wont work as the def hello fxn of hellow.py does not return any value like power fxn does in calculator.py
#to fix this, we'll write this way-
def hello(to="world"):
    return f"hello {to}"

def main():
    x=input("Whats your name?=")
    print(hello(x))

if __name__ == "__main__":
    main()

#this version of code is more testable by assert statement,bcs what assert does is that it run an argument into that fxn and fetch the return value & compare it with the result we assigned afterr '=='.
#So basically, to be tested by the assert, fxn need to hand back the product, so that it can be compared
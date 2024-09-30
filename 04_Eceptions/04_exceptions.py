'''
#          Syntax Error
#error in the structure of the code, gotta find it and fix urself manually

#           Value Error
x=int(input("x="))
print(f"x is {x}")
#if the input is str(like cat), code will give value error

#to fix it/prevent it to happen we use 2 new keywords
#            TRY , EXCEPT
try:
    x=int(input("x="))
    print(f"x is {x}")
except ValueError:
    print("x is not an intiger, please try again")

#            Name error
try:
    x=int(input("x="))
except ValueError:
    print("x is not an intiger, please try again")
print(f"x is {x}")
#eroor will say x is not defined at line 23 bcs x doesnt get any value assigned bcs of error in input. even for wrong input,print command gets executed
# to fix this and use this format only we apply "ELSE"
#               ELSE
try:
    x=int(input("x="))
except ValueError:
    print("x is not an intiger, please try again")
else:
    print(f"x is {x}")
#if input is correct,line 27,28 execute, since 29,30 didnt executed, else statement gets executed.If input is wrong,line 29,30 gets executed, so else part(print section) doeant get executed

#                REPROMPTING
#To build a loop to ask correct input if input is wrong
while True:
    try:
        x=int(input("x="))
    except ValueError:
        print("x is not an intiger, please try again")
    else:
        break
print("x is ",x) 
#print(f"x is {x}") 

#                 GET_INT FXN
#Returning values
def get_int():
    while True:
        try:
            x=int(input("x="))
        except ValueError:
            print("x is not an intiger, please try again")
        else:
            break
    return x #(if we are using this as a fxn, we need to return value after the check completes)
def main():
    x=get_int()
    print ("x is",x)
main()
#Better way
def get_int():
    while True:
        try:
            x=int(input("x="))
        except ValueError:
            print("x is not an intiger, please try again")
        else:
            return x
#Better way#2
def get_int():
    while True:
        try:
             return int(input("x="))
        except ValueError:
            print("x is not an intiger, please try again")

#                  PASS(not imp)
#To handle exception,where you want to catch it, but wanna ignore it, or pass it
def get_int():
    while True:
        try:
            x=int(input("x="))
        except ValueError:
            pass
        else:
            break
    return x 
def main():
    x=get_int()
    print ("x is",x)
main()
#this method doesn't give any prompt to user when the input is wrong,its just ask for x in loop

#          FUNCTION ARGUMENTS
def get_int(Z):
    while True:
        try:
            x=int(input(Z))
        except ValueError:
            print("x is not an intiger, please try again")
        else:
            break
    return x 
def main():
    x=get_int("x=")
    print ("x is ",x)
main()
'''

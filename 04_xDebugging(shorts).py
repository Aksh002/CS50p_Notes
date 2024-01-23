def main():
    hieght=int(input("H="))
    pyramid(hieght)
def pyramid(n):
    for i in range (n):
        print("#"*i)
if __name__=="__main__":
    main()
#here the problem is 
#Breakpoints- its a marker on the left most side of of the line(behind the no. tally), its fxn is to pause the execution of code just before that line
#Run and Debug- its the fxn in vs code provided at the laet bar which helps us to debug code. like if u click on the run and debug option,it will show red line on the breakpoint line and some options on top of the screen
#Continue: breakpoint is gonna left behind and rest will be executed
#Step into: this would help us to step into the function and sttep by step walk through the code 
#Step over:This would run the code till the line with yellow pointer
#these can be used in collabration to step into a fxn, run it step by step and see that part of the code does and which part of code has the problem, see video for better understanding

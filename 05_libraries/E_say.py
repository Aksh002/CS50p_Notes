import sys
from sayings import hello
if len(sys.argv)==2:
    hello(sys.argv[1])
#THe output u will get  on typung "python say.py Akshit" will be -
        #Hello World
        #Goodbye World
        #Hello Akshit
#This is happening because whenever the file is getting loaded by python, main is gonna get called, even if u=im just importing one fxn of this file 

#To fix this we use __name__ wala statement in sayings.py
    
#Now type "python say.py akshit"
#Output will be-
    #Hello Akshit
 

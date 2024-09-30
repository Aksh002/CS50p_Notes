#Regular expression(Regex) is a pattern used to match whether the input given is of the required form or not.Like did they reallly typed the email, is it in correct form

# @?
email=input("Whats your email? :").strip()
if "@" in email:
    print("Valid")
else:
    print("Invalid")
#Only This wont work 

# . ?
email=input("Whats your email? :").strip()
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
#Only This wont work 

#More logical
email=input("Whats your email? :").strip()
username,domain=email.split("@")
if (username) and ("." in domain):   #These 2 r 2 different boolean expressions, dont get confused with english
    print("Valid")   #when username=True
else:
    print("Invalid")
#Only This wont work 
    
#More precise
email=input("Whats your email? :").strip()
username,domain=email.split("@")
if username and domain.endswith("edu"):   #These 2 r 2 different boolean expressions, dont get confused with english
    print("Valid")   #when username=True
else:
    print("Invalid")
#Only This wont work 


#             RE LIBTRARY
#re library is gonna let us difine some pattern like a pattern for email id, and used some builtin fxn to validate the input against that pattern,or use these patterns to change the input or extract partial info frm the input
#Source-docs.python.org/3/library/re.html
    
#          re.search(pattern,string,flags=0) Fxn

#pattern is the required pattern,string is the given input,flag is used to modify the behaviour of the fxn.
import re
email=input("Whats your email? :").strip()
if re.search("@",email):
    print("Valid")
else:
    print("Invalid")

#pattern here can take many special symbols like-



#    .  =  any charachter except new line
#    *  =  0 or more repitition
#    +  =  1 or more repition
#    ?  =  0 or 1 repitition
#    {m}  = m repition
#    {m,n}  =  m to n repitition



import re
email=input("Whats your enail?").strip()
if re.search(".*@.*",email):
    print("Valid")
else:
    print("Invalid")
#But this wont give what we want, as * involves 0 repition also

#Applicable method
import re
email=input("Whats your email?").strip()
if re.search(".+@.+",email):
    print("Valid")
else:
    print("Invalid")

#Another way
import re
email=input("Whats your email?").strip()
if re.search("..*@..*",email):
    print("Valid")
else:
    print("Invalid")


#To check string/email ends with .edu
import re
email=input("Whats your email?").strip()
if re.search(".+@.+.edu",email):
    print("Valid")
else:
    print("Invalid")
#this womt work as python would not read that"." before  .edu is specific, to improve this
  
#correct way-
#NOTE-an escape character is a backslash \ followed by a character that you want to represent. Escape sequences are used to include special characters in strings. For example, the \n escape sequence represents a newline character.
#this is used fix this issue, so that python wont read dot as it is, but "\.", these r called special sequences
#To not let python misinturpret \ as some start of special fxn like next line(\n), we need to specify python that we want regular expression string in raw form.We  do this by adding "r" before string. Its similar to adding f at the biggining of a format string which tells python tu plug in variables that r between curly brackets 
import re
email=input("Whats your email?").strip()
if re.search(r".+@.+\.edu",email):
    print("Valid")
else:
    print("Invalid")

#Another problem is if the input is "My email is akshit@manipal.edu.",the code validate this also,it will cause a problem if the mails r collected and transferred into gmail program, to fix this we use sm other symbol


#    ^   = matches the start of the string 
#    $   = matches the end of the string just before the new line at the end of the string



import re
email=input("Whats your email?").strip()  #We want to start the comparing with our desired form from the very first word of the input and till last letter of the input string
if re.search(r"^.+@.+\.edu$",email):
    print("Valid")
else:
    print("Invalid")

#Another prblm is that if the input has multiple @, code will validate that also
#To fix this we will use
    


#    []   =  set of charachters
#    [^]  =  complementing the set




#As we know that "." represents any charachter, and we want to not allow any charachter but certasin charachters,we use [<charachters to allow>] instead of ".",eg:- [asdfgh],here input could be of these words only
#[^<charachter>] meanes that the charachter inserted inside cant be entered,rest all the charachters r allowed  
import re
email=input("Whats your email?").strip()  
if re.search(r"^[^@]+@[^@]+\.edu$",email):     
    print("Valid")
else:
    print("Invalid")

#If we want a range of letters to be allowed
import re
email=input("Whats your email?").strip()  
if re.search(r"^[a-z]+@[^@]+\.edu$",email):     #do not need to erite all 26 letters
    print("Valid")
else:
    print("Invalid")

#To add more
import re
email=input("Whats your email?").strip()  
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):     #no spaces and commas required
    print("Valid")
else:
    print("Invalid")

# "\w" - Its a word charachter which is commanly known as alpha numeric symbol and underscore as well.It can replace [a-zA-Z0-9_] here
import re
email=input("Whats your email?").strip()  
if re.search(r"^\w+@\w+\.edu$",email):     #no spaces and commas required
    print("Valid")
else:
    print("Invalid")

#Some other commonly used patterns 
    
    #    \d    =  decimal digit
    #    \D    =  not a decimal digit
    #    \s    =  whitespace charachter
    #    \S    =  not a whitespace charachter
    #    \w    =  word charachter ..., as well as numbers and underscore
    #    \W    =  not a word charachter

#If we want to accept not just .edu but also .com and .gov and many more, we make a tuple of them with or bar "|" between them
    
    #    A|B   =  either A or B
    #    (...) =  a group
    #   (?:...)=  non capturing group

import re
email=input("Whats your email?").strip()  
if re.search(r"^\w+@\w+\.(edu|com|gov|in)$",email):     
    print("Valid")
else:

#to also allow whitespaces in the input
    import re
email=input("Whats your email?").strip()  
if re.search(r"^(\w|\s)+@\w+\.edu$",email):  
    print("Valid")
else:
    print("Invalid")

#Another error is with uppercase input like "AKSHIT@MANIPAL.EDU", we will get invalid becsuse we r asking edu in lower case in the code but the input is in uppercase
#We can solve this by "email=input("Whats your email?").strip().lower()"
#Or we can use the 3rd argument that can be passed in the search fxn that is FLAG.some flags r-
    #    re.IGNORECASE    =   
    #    re.MULTILINE  
    #    re.DOTALL     

import re
email=input("Whats your email?").strip()  
if re.search(r"^\w+@\w+\.edu$",email,re.IGNORECASE):     #no spaces and commas required
    print("Valid")
else:
    print("Invalid")

#Another issue remains that our code doesnt allow "." in oue mail except at .edu position
#WE could fix this by adding "\w+\." to the code"
import re
email=input("Whats your email?").strip()  
if re.search(r"^\w+@\w+\.\w+\.edu$",email):     
    print("Valid")
else:
    print("Invalid")
#But by this method a new problem arrises that our code will not work if the input is "akshit@manipal.edu"
#So this method CAN NOT BE APPLIED

#It can be fixed by using "?" as it meanes 0 or 1 repitition 
import re
email=input("Whats your email?").strip()  
if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email):     
    print("Valid")
else:
    print("Invalid")

#Another way
import re
email=input("Whats your email?").strip()  
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$",email):     
    print("Valid")
else:
    print("Invalid") 

#Better way to validate email is to use alr made library bcs manually can be tedious
    
#         re.match(pattern,string,flag=0)
    
#This is another fxn in re lib which does the work of "^" automatically,it will match the pattern from the very start of the input string

#         re.fullmatch(pattern,string,flag=0)
    
#It does the work of "^" and "$" automatically,it will match the pattern with the very first letter of the input string and check till very end letter of input string

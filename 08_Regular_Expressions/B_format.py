
#we will be formatting the data containing names taken as a input, where issue could be that input name is in revdersed form(gangwar,akshit)
name=input("Whatsa your name?=").strip() 
if "," in name:    #If there is a "," in name
    last,first=name.split(", ")
    name=f"{first} {last}"
print(f"hellow {name}")

#this wont work if the input doesnt hv the space after coma, to fix that we can use "()". "()" brackets are not only t ogrp things together but also to capture them. Until re.search was used only with if, it was returning True or False. but re.search can also return values if () is used in it. it will return whatever is in () in the form of groups.
#If we dont want to return to  the values- (?:...)  =  non capturing values

import re
name=input("Whats ur name?=").strip()
matches=re.search(r"^(.+), ?(.+)$",name)  #by adding ?, we states that either there is space exists or not
if matches:
    name=matches.group(2)+" "+matches.group(1)
print(f"hello {name}")

#tidious code
#  :=  -  walrus operator  -  it allows to assign a value and ask a boolean question about it 
import re
name=input("Whats ur name?=").strip()
if matches:=re.search(r"^(.+), ?(.+)$",name):  #by adding ?, we states that either there is space exists or not
    name=matches.group(2)+" "+matches.group(1)
print(f"hello {name}")


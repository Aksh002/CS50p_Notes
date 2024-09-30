'''
#              Command-line Arguments
#                SYS MODULE
#sys.argv(argument v)-argv is a pre existing variable, its a list of all of the words that a human typed in the prompt window before they hit enter  
import sys
print("hello,my name is ",sys.argv[1])
#then type "python 05_libraries.py akshit" in command prompt to execute the program
#here, sys.argv makes a list of all the material(including file name) typed in the command prompt,thus by fetching i=1 element(2nd element) from the list will give us name as the 2nd material provided in the command prompt is name
#its like getting output of printing name tag whenever user wants


#if you do not write your name in command promopt, it meanes you will not provide no value at the position i=1 in set, thus it will show index error as you are fetching something that doesnt exist
#One way We can handle this error by using concepts of try
import sys
try:
    print("hello,my name is ",sys.argv[1])
except IndexError:
    print("Insufficient no. of arguments")

#More refined way
import sys
if len(sys.argv)<2:
    print("Insufficient no. of values")
elif len(sys.argv)>2:
    print("Extra no. of values")
else:
    print("hello,my name is ",sys.argv[1])


#TO seperate out error checking and the body of the code
import sys
if len(sys.argv)<2:
    print("Insufficient no. of values")
elif len(sys.argv)>2:
    print("Extra no. of values")
print("hello,my name is ",sys.argv[1])
#But this will give error bcs print line will run regardless

#To fix this, we use fxn of sys module named-      sys.exit(...)
import sys
if len(sys.argv)<2:
    sys.exit("Insufficient no. of values")
elif len(sys.argv)>2:
    sys.exit("Extra no. of values")
print("hello,my name is ",sys.argv[1])
#Here the code will reach the print statement only if both if confition is false


#To support multiple value at the prompt

#We will use a fxn named -      slices         -to just take a slice of the list, this will left out the name of the file which could hv been printed otherwise
#its syntax is just [n:], where n is index value where u wanna slice, n: represents that code will cosider the list only from n index
import sys
if len(sys.argv)<2:
    sys.exit("Insufficient no. of values")
for arg in sys.argv[1:]:
    print("hello,my name is ",arg)
#now write "python B_note.py akshit suryansh vaibhav vishnesh" in command prompt for input

#we can slice smthing frm the end too
import sys
if len(sys.argv)<2:
    sys.exit("Insufficient no. of values")
for arg in sys.argv[1:-1]:
    print("hello,my name is ",arg)
#skips the last value

#                           PACKAGES    
#package - A module implemented in the folder.Generally , Its a third party library that can be downloaded
#We can get all the package frm - "PyPI" | Link: pypi.org
    
#cowsay library is used to print cow saying smthing on the screen
    

#                           PIP
#pip is a package manager in python that is used to install packages in python 
#command - "pip install <package_name>"
import sys
import cowsay
if len(sys.argv)==3:
    cowsay.cow("hellow "+ sys.argv[1])    #We gotta concatinate the strings here bcs cow fxn is not like our print fxn, thats why it cant accept comma seperated arguments
    cowsay.trex("hello Mr. "+ sys.argv[2])
'''

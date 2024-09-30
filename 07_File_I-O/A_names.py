
#list
names=[]
for _ in range(3):
    names.append(input("Whats ur name?="))
#To sort the list in alphabetic order, we use  SORTED  keyword
for name in sorted(names):
    print(f"hello {name}")

#but if we run this program,all the data collected is lost

#                OPEN
#Open- its fxn is to open a file programatically, so that the programmer can read info from it or write info to it   
#Resource- docs.python.org/3/library/functions.html#open
name=input("Whats ur name?=")
file=open("names.txt","w")
#open returns a "file handle", a special value that allows me to access that file subsiquently,thats why use will store in file variable
file.write(name)
file.close()
#type "python names.py" in terminal to run the code and the store the value,then type code "names.txt" in terminal to open the txt file u just created by running the program and giving the input data
#the letter in "" represents yhe mode file is opening in, if its r, file is opened in reading mode, if its w, it has opened in writting mode,a is for append mode

#                Append
#But this code will not store multiple names as whenever it runs,"w" not only create the file for you, it will recreate the file for you,u open the file and give a input,but when u open the file again and give the input,it will open the same file but will create a new version of it having new input only 
#To fix this and store multiple names in same file we use "a" keyword
name=input("Whats ur name?=")
file=open("names.txt","a")

file.write(f"{name}\n")

#We wrote thi code this way bcs we want all names in seperate lines,if we use code we used in last one, we'll end up with all names written in same line without any space or line break

file.close()

#               WITH
#to avoide using "file.close()", we can use keyword "WITH"
#It instruct python that in this context i want u to open and automtically close this file
name=input("Whats ur name?=")
with open("names.txt","a") as file:
    file.write(f"{name}\n")
#The line of code writting the name is in context with "with statement".So if i hv more code in this file down below no longer indented,the file wil be automatically be closed after running line 38

#             Read lines
#"r" is used to read lines
with open("names.txt","r") as file:
    lines=file.readlines()
#readlines is a fxn that read all the lines frm the file and return them as a list

for line in lines:
    print("Hello ",line)
#This code will give you extra line after every name because new line command is given twice,first while writting names in the file using "\n",secound time when we print,print always tends to create new line after printing the result of one loop
#To ocunter this we can type "end=" "" or we can use "rstrip" fxn
with open("names.txt","r") as file:
    lines=file.readlines()

for line in lines:
    print("Hello ",line.rstrip())
#we can also use "end=""" to prevent empty line 

#Efficient way
with open("names.txt","r") as file:
    for line in file:
        print("hello",line.rstrip)


#                 SORTING

names=[]
with open("names.txt") as file: #If u are opening a file to read it u dont need to specify "r"
    for line in file:
        names.append(line.strip()) #Appending to the list taken above and not the file
#Till here,in our code we stored all the names of the names.txt file to the list named names
for name in sorted(names):
    print(f"hello,{name}") 

#Efficient way
with open("names.txt") as file: #If u are opening a file to read it u dont need to specify "r"
    for line in sorted(file):
        print("hello",line.rstrip())
#in python documentation documentaion u will find the summarry for sort fxn sorted(iterable,/,*,Key=None,reverse=False). We can pass reverse=True to overwrite the default mode and perform reverse sorting 
with open("names.txt") as file: #If u are opening a file to read it u dont need to specify "r"
    for line in sorted(file,reverse=True):
        print("hello",line.rstrip())


#                                       Coursera

file=open("names.txt","a")
name=file.name              # Will fetch name

mode=file.mode

firstline=file[0]
secoundline=file[1]
# Lines are stored in a list
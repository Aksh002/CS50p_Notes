'''
students=[]
with open ("students.csv") as file:
    for line in file:
        name,home=line.rstrip().split(",")
        student={"name":name,"home":home}
        students.append(student)

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['home']}")
'''
#This program wont work because there are 2 commas in the first line of file. Thats why it will show  "Value error:to many values to unpack"
#To solve this, we use a lib named CSV 

#                CSV module
#Source- docs.python.org/3/library/csv.html

import csv
students=[]
with open("students2.csv") as file:
    reader=csv.reader(file)
#The fxn of reader fxn of csv lib is to read a csv file and detect potential corner cases like comma, quotes,etc and deal with them for you
    for row in reader:
        students.append({"name":row[0],"home":row[1]})
#reader for each line of the file return a row in the form of list ([ron,the burrow])

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")

#Better way 
import csv
students=[]
with open("students2.csv") as file:
    reader=csv.reader(file)
#The fxn of reader fxn of csv lib is to read a csv file and detect potential corner cases like comma, quotes,etc and deal with them for you
    for name,home in reader:
        students.append({"name":name,"home":home})
#reader for each line of the file return a row in the form of list ([ron,the burrow])

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")
#SO in summary,whats happining is ,we open a file,make csv.reader read  each line of the file return a row in the form of list ([[ron,the burrow],[Draco,malfoy manor]]),that whole list is stored in a variable called reader.
# Then we itterate for 2 variables name,home over reader, this signifies that all the 1st value of the lists r taken as name and 2nd values of list is taken as home.Under this loop, we will append a dictionaries consisting of 2 perameters/variables names and list,and assign them the values of name and home from reader respectively.
#Everry iteration creates a dictionary and append it in the list named students
#Next loop is run for the variable iterating over sorting fxn applied on students list where key is given by lambda fxn having perameter named student(could be anything tbh)returning the "name" part of every iteration ran by student.
#Under this loop, for every iteration,sorted output is printed 
    
#           
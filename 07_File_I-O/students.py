'''
with open("students.csv") as file:
    for line in file:
        row=line.rstrip().split(",") #each line in the csv file is taken as a row and each of the values seperated by commas is taken as coloumns
        print(f"{row[0]} is in {row[1]}")
#Effective Way 
with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",") #each line in the csv file is taken as a row and each of the values seperated by commas is taken as coloumns
        print(f"{name} is in {house}")

#to sort and print the data of the file
students=[]
with open ("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

#here we are not sorting by name,we r sorting by sentences.
#SO to sort by name-
students=[]
with open ("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
#here we create a local library to associate 2 values of students and house together
        student={} #this will have 2 keys
#Or can use student={"name":name,"house":house} instead of line 29,31,32
        student["name"]=name
        student["house"]=house
        students.append(student)
    
# for  student in students:
#     print(f"{student['name']} is in {student['house']}")  #single quotes are used for str index of the dictionary because double quotes were already used in line

#this wil simpley just print all the values
#we cant use the same method of sorting we used before,cant write sorted(students) as we cant sort a whole dictionary inside the list
#so to tell the sorting fxn to sort about certain specific key of the dictionary, we go like this
def get_name(student):
    return student["name"]

for student in sorted(students,key=get_name):  #while writting fxn as key,it is done without "()".
#python allows to pass fxns as argument into other fxns,we are passing the get_name fxn as an argument for the sorted fxn
    print(f"{student['name']} is in {student['house']}")

#to sort in reverse order
for student in sorted(students,key=get_name,reverse=True):
    print(f"{student['name']} is in {student['house']}")
#same can be sorted wrt house
#we are not using "()" with getname bcs we want sorted fxn to call getname
#as we are defining the fxn and immediately using it,but never needing it in the future,we can also use "lambda" fxn as a short replacement of that fxn,its implemented like this
'''
#                    LAMBDA Fxn
#its an annonomous fxn that tells pyhton,"hey python, there is this fxn, it has no name",that fxn takes a perimeter,here its student, bcs this fxn is called on every dictionary(named student) of that list,as we are sorting abt names if student, we will index in dictionary and access return names,which r gonna be the key here
students=[]
with open ("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student={"name":name,"house":house}
        students.append(student)

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['house']}")
#that student after lambda is a parameter, which could be anything, but called as a student  here bcs this fxn 
#that student in student["name"] refers to that variable/pointer student which will iterate over the library present in the list name students. that "name" signifies that it will take name part of the dictionary
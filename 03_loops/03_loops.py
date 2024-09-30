'''
#           WHILE LOOP

#ifinite loop
i=3
while i!=0:
    print ("meow")
#basically just put always true statement after while

#basic loop
i=3
while i!=0:
    print ("Meow")
    i=i-1

#ascending way
i=1
while i<=3:
    print ("Meow")
    i=i+1

#another way
i=0
while i<3:
    print ("meow")
    i+=1

#            FOR LOOP
#LIST- its another datatype which is a way of containing multiple values all in the same varieble
for i in [0,1,2]:
    print("meow")
#this isnt applicable for large cases, when we hv to print more then 3 times

#better way
for _ in range(3):   #we cane use "_" instead of "i" as we arent using it later
    print("meow")

#another way 
print("meow\n"*3,end="")
#\n= creates new line after every operation
#end=""= makes sure that end is not \n, its a blank spacwe, this stops creation of vacant line at the end

#list function
friends =["akki","2",4]
x=[1,2,3]
friends.extend(x)
print(friends)

friends.append("sunny")# to add element to the list,at the end
friends.insert(1,"kellx")#to add element in the middle of the list
friends.remove("kellx")
friends.clear()
friends.pop()
print(friends.index(4))
print(friends.count(4))
friends.sort()
friends.reverse()

#TUPPLE- Its a type of a data structure that is immutable, data in it cannot be modified unlike list

#infinite loop to get the input from the user that match the desired expextation u have
while True:
    n=int(input("n="))
    if n<0:
        continue
    else:
        break

for _ in range(n):
    print("meow")

#another way
while True:
    n=int(input("n="))
    if n>0:
        break
for _ in range(n):
    print("meow")


#Better/complex way
def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("n="))
        if n>0:
            break
    return n
#   ''another way
#   while True:
#       n=int(input("n="))
#       if n<0:
#   return n"
    ''
#we hv to return n after we break the while loop fxn bcs we took the input value from user in that fxn only, if the fxn breaks, we hv to return n to the get_number fxn
def meow(n):
    for _ in range(n):
        print("meow")

main()


#to print a perticular item in the list by its position

students=["Hermione","Harry","Ron"]
#list of three strings
print(students[0])
print(students[1])
print(students[2])

#better method
students=["Hermione","Harry","Ron"]
for student in students:
    print(student)

#LEN
#len- tells the length of the list
students=["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(students[i])
#loop will run the number of times = len of set

#To assign number to each 
students=["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(i+1,students[i])


#                 DICT(dictionary)
students={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}
print(students["Hermione"])
#basically dictionary uses strings as keys instead of intigers (like list does)
for student in students:
    print(student)
#But when you use a for loop in Python to iterate over a dictionary, by design,it iterates over all of the keys.
for student in students:
    print(student,students[student],sep=" - ")

#                 Lists of dictionaries
#to associate multiple things with students
students=[
    {"name":"Hermoine","house":"Griffindor","patronus":"otter"},
    {"name":"Harry","house":"Griffindor","patronus":"stag"},
    {"name":"Ron","house":"Griffindor","patronus":"Jack"},
    {"name":"Draco","house":"Slytherin","patronus":None}#keyword none in python represent the absence of a value
]
#[] brackets represent its a list 
#{} brackets represent its a dictionary
#so hermoine dictionary has 3 keys-name,house,patronus. And it has 3 values/defination which are-hermoine,gryffindor,otter
for student in students:
    print(student["name"],student["house"],student["patronus"],sep=" - ")
#1st version associated students names their houses,in the next version,we standardize the names of our keys to be name,house,patronus,and the values of those keys is our data like....

# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

#                NESTED LOOPS
def main():
    print_coloumn(3)
def print_coloumn(hieght):
    for _ in range(hieght):
        print("SEX")
main()

def main():
    print_row(4)
def print_row(width):
    print("Fuck"*width)
main()

#
def main():
    print_square(3)
def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#",end="")
        #as we dont need a new line after  every brick,we need a new line after end of every row.As the inner loop completes, this empty print fxn helps us to switch the line  
        print()
main()

#Another way
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#"* size)
main()

#Another way2
for i in range(3):
        print("#"* 3)


#                   Extra stuff
x= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for i in x:
    for z in i:
        print(z)
'''
#abs is used to print positive part of negative no.
#fabs is used to print positive part of negative float number

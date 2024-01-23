#OOPs is basically a way to solve large problems
'''
def main():
    name=get_name()
    house=get_house()
    print(f"{name} from {house}")

def get_name():
    return input("name; ")
def get_house():
    return input("house: " )

if __name__=="__main__":
    main()


#We can optimise by taking all inputs in one go, under same dif fxn
def main():
    name,house=get_student()  #upacking the values coming frm the fxn
    print(f"{name} from {house}")

def get_student():
    name=input("name: ")
    house=input("house: ")
#one of going frm here is making a dictionary of both of them
#another way
    return name,house 
if __name__=="__main__":
    main()

#here we uase tuple
#tuple- its another type of data that is a collection of values.Its similar to list only diff is dat list is mutable and tuple is immutable(cant be changed)
#List is a data str in python of which u can change the values of. If you hv no intention of changing the values, u can use tupple
#basically get_studnet aint returning 2 values, its returning 1 value which is a tupple containing 2 values,so actually we dont need to unpack the values, we can just name the whole tupple "student"
def main():
    student=get_student()  #upacking the values coming frm the fxn
    print(f"{student[0]} from {student[1]}")
#fxn(0) means calling that value

def get_student():
    name=input("name: ")
    house=input("house: ")
#one of going frm here is making a dictionary of both of them
#another way
    return name,house 
if __name__=="__main__":
    main()

#a example showing immutabilty of tupples 
def main():
    student=get_student()
    if student[0]=="Padma":
        student[1]="ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name=input("name: ")
    house=input("house: ")
    return name,house 
if __name__=="__main__":
    main()
#This will give typeError saying that tupple obj doesnt support item assignment.
#If we convert the datatype into list,it will work
def main():
    student=get_student()
    if student[0]=="Padma":
        student[1]="ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name=input("name: ")
    house=input("house: ")
    return [name,house]   #now its a list
if __name__=="__main__":
    main()

#[]= list       ()=tuple

#NOw solving this by using dictionary
def main():
    student=get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    student={}
    student["name"]=input("name: ")
    student["house"]=input("house:")
    return student   
if __name__=="__main__":
    main()
#another way
def main():
    student=get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    student={}
    name=input("name: ")
    house=input("house:")
    return {"name":name,"house":house}   
if __name__=="__main__":
    main()

#In dict,we can make changes
def main():
    student=get_student()
    if student[0]=="Padma":
        student[1]="ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    student={}
    name=input("name: ")
    house=input("house:")
    return {"name":name,"house":house}   
if __name__=="__main__":
    main()

#                  classes
#its a general purpose tool which helps us to create our own dataTypes and give them name
#its kind of mould that can define and give a name
#source- docs.python.org/3/tutorial/classes.html
class Student:    #This is enough to create a datatype
    ...                    #... is a placeholder that indicates that ill come back to it later
def main():
    student=get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student=Student()   #here,we r creating an object of that class,student is an obj #By just defining a class, u get fxn whose name is identical to the class name
#classes has attributes,properties of sorts that allows to specify values inside, its syntex is dot,it helps in inserting smthing inside of smthing 
#class is the diffination of new datatype, the object is the incarnation or instaniation of class
    student.name= input("Name: ")
    student.house=input("House: ")
    return student
#here, we difined our own class,which is basically our datatype,then we store attributes into it using dot,then we will acces those attributes using code  we did in the line 127 
if __name__=="__main__":
    main()

#these class datatypes are mutable but can be made immutable too
#attributes(here were house and name ) can also be called instance variables as they r nothing but variables inside of an object whose type is student
#atrributes variables can store values of any datatype

 
#In classes,unlike in dict,we can specify/standardise what those attributes can be and what kind values u can set them to

class Student:
#there r not just Attributes/instance-variable that can be put inside in the class, u can also add methods.Methods are fxns in classes that behave in a special way.Thses methods allow you to determine behaviour of contents object in the standard way
    def __init__(self,name,house):  #it is called of automatically by the python
    #  __init__ = instance method  -  it is defined to initiallise the contents of an object from a class
        self.name=name
        #here we are crating a new atrribute/instance variable to store the name and house passed init. we can also write "self.n=name".Its like installing name and house into the empty obj which was is created and storing them in attributes/instance variables in the object  
        self.house=house
    #this fxn helps to put in the values in the empty object created at line 163

def main():
    student=get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name=input("Name: ")
    house=input("House: ")
#   student=Student(name,house)
#here we are passing name,house as an argument in the fxn.Passing these variables ar argument in Student class empower us to check if the input is valid,if the user hasnt done bakchodi by passing space or smthing else in the input
#whats on lime on 163 is called a  constructor call,this is the line of the code that will construct a student object  for me. it will do this by using Student class a template/mould so that evry student is structured the same(name,house).we can customise the contents of that object
#a student blueprint is always gonna hv a name and house,bcs of molding by classes but we can pass any name and any house,thats customizable
#"self" in innit fxn is used to store the name and house that is passed into the fxn,we cant use "__init__(name,house)" only bcs what we gonna do with them by passing them in the fxn.If we want to remember name and house, we gotta store them somewhere,to store them we passes 3rd argument named self(can be anytrhing but is self by convention).Self is a reference to argument,it reference the object that is just constructed
    return Student(name,house)

if __name__=="__main__":
    main()

#To validate users input,to check if theres not just space in place of 
class Student:
    def __init__(self,name,house):
        if not name:     #we can also use 'if name==" "'
            #print("missing name") - we can not just print missing name and let rest of the code go through
            #import sys|sys.exit("Missing name") - exiting the whole code just bcs one wrong input is harsh
            #return None - we cant do this as its not true,we cant say student doesnt exist bcs later in code student is created in the momery
            raise ValueError("Missing name")  #
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
           raise ValueError("Invalid house")
        self.name=name
        self.house=house
def main():
    student=get_student()
    print(f"{student.name} is from {student.house}")
def get_student():
    name=input("name: ")
    house=input("House: ")
    #instead of just returning we can do like-
    
    #try:
    #    return Student(name,house)
    #except ValueError:
    #    ...   #u can handle the error the way u want frm here

    return Student(name,house) 
#this is the reason why Class is better then Dictionary,in dictionary,if we add some key, it going in no matter what,but if u add some attribute to a Class, u can controle what can be stored 
if __name__=="__main__":
    main()

#If in the place of "print(f"{student.name} is from {student.house}")" we type "print(student)" then we will get the output like "<__main__.Student object at 0x00000225D7D76510>".This is the representaion of where the object is stored in the memory of the computer 
#To overwrite this-


#  __str__  -
#If u difine this special method in ur class,python will automatically call this fxn whenever any other fxn(print here) wants to see ur object as a string        
#Its like another way writting the above code
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house

    #def __str__(self):
    #    return "a student"
    # if the above code is used inplace of below one, we will get the output "a student"
    
    def __str__(self):
        return f"{self.name} is from {self.house}"  
def main():
    student=get_student()
    print(student)   #here,print hopes of getting a stringfrom the object,object calls __str__ fxn/method stored in his pocket,with passing the reference to the object thats to be printed so that we can do as above
    #print(f"{student.name} is from {student.house}")
def get_student():
    name=input("name: ")
    house=input("House: ")
    return Student(name,house)
if __name__=="__main__":
    main()

#Making our own methods
class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
        self.patronus=patronus
    def __str__(self):
        return f"{self.name} is from {self.house}"
    #to provide all the students to cast charm,we will create our own method/fxn to do so
    def charm(self):
        #we will basically return an emoji for every student
        match self.patronus:
            case "stag":
                return "🐴"    
            case "Otter":
                return "🃏"
            case "Jack russel terrier":
                return "🐶"
            case _:
                return "🪄"
            
def main():
    student=get_student()
    print("madarchod patronum!!!!")
    print(student.charm())    
def get_student():
    name=input("name: ")
    house=input("House: ")
    patronus=input("Patronus: ")
    return Student(name,house,patronus)
if __name__=="__main__":
    main()
'''
#              PROPERTIES
#an attribute to hv more control
#decorators-these r fxn used to modify the fxn of other fxns
class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house    
        #this(above line) is also gonna call setter method, so it will be called whne an obj is created,with init fxn,and when programmer try to circumvent the init method and change the value of this attribute 
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    #Getter- Its a fxn for a class that get some attributes 
    @property
    def house(self):
        return self._house
    
    #Setter-Its a fxn is class that set some values
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house=house
    #so basically as we have attribute named self.house in init fxn, we casnt take a fxn in same class named house for getter and setter,so to fix that we store input in self._house to differentiate a little,now our attribute is _house and property house.We cannot change to _house in init fxn bcs python recognise the pattern "self.house=" to automatically call the setter
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self_name=name

def main():
    student=get_student()
    #we can still acces those instance variables using this dot notation,so any input given by the user will overwrite by this
    student.house="Number four,privet drive"  
    #so doesnt matter what input give to the code for house, it will provide the same result as passed above,that innit fxn falls apart
    #We r trying to prevent programers to circumventng our error checking that we put in place for name and house.We do this by aquiring that,in order to acess the attribute,we go through a fxn,in order to set a fxn,u go through  a fxn (Getter and setter fxns) 
    #So basically what is happening is when we type "student.house=",python instead of returning self.house instance variable,it automatically runs the getter fxn,where the check for valid house is present
    print(student)    
def get_student():
    name=input("name: ")
    house=input("House: ")
    return Student(name,house)
if __name__=="__main__":
    main()
#So on running this code, we should get "Value error" instead of getting incorrect output, "Number four,pivet drive" will get caught by the if loop this time. 

#but if we change "student.house="Number four,privet drive"" to "student._house",the defense mechanism we deployed fails again, we will again get the wrong input,not the valueError.So only way to fix this now is to not use the name of variable which is of instance variable alr
    
#                           INT 
    
#constructor call     class int(x,base=10)
    #base for iteger is 10 and for binary is 2

#source-docs.python.org/3/library/functions.html#int
    
#int is itself a class,evrytime we hv converted a string to an int we r just making a obj of type int


#string is also a class
#list,dict,etc all are classes and fxns performed on them are methods
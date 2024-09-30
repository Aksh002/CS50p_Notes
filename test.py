'''
x=int(input("x="))
z=x.isnumeric()
print(z)

x=float(input("x="))
y=float(input("y="))
z=x/y
print(f"{z:.2f}")

name=input("Whats your name?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("who?")

while True:
    n=int(input("n="))
    if n<0:
        continue
    else:
        break
print(n)
for _ in range(n):
    print("meow")

print(pow(3,2))
def main():
    x=int(input("X="))
    y=int(input("Whats the power?="))
    print(f"X with power {y} is =",square(x,y))

def square(n,z):
    return pow(n,z),#n*n can be used if only squared is wanted
main()

def hellow(to="world"):
    print("hello,",to)

name=input("Whats ur name?")
hellow(name)

data = {'C':20, 'C++':15, 'Java':30, 
        'Python':35}
courses = list(data.keys())
values = list(data.values())
print(courses)
'''

class Wizzard:
    def __init__(self,name):       #initialisation method getting initialise with name only
            if not name:
                raise ValueError("Missing name")
            self.name=name

#To tell the file that a student is a wizard and a proffesor is a wizzard,we do this
class Student(Wizzard):
#A student inherits frm or a subclass of wizard.wizard is basically superclass of the student class.It will inherit the charachteristics of wizard
    def __init__(self,name,house):
        #since both classes hv init method that r gonna called,to use the fxnality in the wizard class' init method
        super().__init__(name)
        #super is used for accessing current class's parent class 
        self.house=house

class Professor(Wizzard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
#whats nice is that wizard as a class is now taking care of all the assignment of wizard's name
#student is inheriting and using all that fxnality by calling superclass's own init method,also additionally taking house


wizzard=Wizzard("Albus")
student=Student("Harry","Gryffindor")
professor=Professor("Severus","Defense against the dark arts")

print(wizzard.name,"\n",student.name,"\n",professor.name)    

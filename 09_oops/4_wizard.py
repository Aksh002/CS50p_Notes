#                  INHERITANCE
# By oops,we hv opportunity to design our classes in a hierarchichal fashion,where u can hv one class inherit frm or borrow sttributes that is methods or variables frm another class if they all hv those in comman.
'''
class Student:
    def __init__(self,name,house):
        if not name:
                raise ValueError("Missing name")
        self.name=name
        self.house=house
    ...

class Professor:
    def __init__(self,name,subject):
        if not name:
                raise ValueError("Missing name")
        self.name=name
        self.subject=subject

#this way of writting multiple classes repeating same shit is pretty ineffientNot to mention if we add error checking to it.
    #Solution to this provided by oops as inheritance,where u can define multiple classes that somehow relate to one another.They dont even need to be parallel like they r here.There could be some hierarchy b/w them.
    #Since both students and professor are wizards in harry potter world,we can introduce a Class named wizard where we can hv any of the common attributes b/w students and professor  

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
'''
#We can hv multi level inheritance also

#ValueError we hv studied so far has a superclass named Exception,which also has super super Class named Base exception,all the errors under Exception are all different but hold a common fxnality with parent "Exception".So u can basically handle Parrent error(Exception) also with try-except method u do for Valueeror
'''
    BaseException
    +-- KeyboardInterrupt
    +-- Exception
        +-- ArithmeticError
            +-- ZeroDivisionError
        +-- AssertionError
        +-- AttributeError
        +-- EOFError
        +-- ImportError
            +-- ModuleNotFoundError
        +-- LookupError
            +-- KeyError
        +-- NameError
        +-- SyntaxError
            +-- IndentationError
        +-- ValueError

'''

#             CLASS METHODS
#sometimes its not necessary to associate a fxn with the objects of the class but rather the class itself.An object or instance variable of a class is a very specific incarnation of that class 
#sometimes u hv functionality related  to each of the obj that isnt distinct or uniquie for any of the obj,that fxnality is gonna be exactly same no matter the obj in question.U want that fxnality for whole Class itself
# @classmethod-  its another decorator/fxn which is used to specify that this method is not by default an instance method that has the acess to self, the obj itself,this is a class method thats not gonna have access to self but it does know what class its inside.

import random
class Hat:
    def __init__(self):
        self.houses=["gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    def sort(self,name):
        print(name,"is in",random.choice(self.houses))

hat=Hat()
#istentiating hat object
hat.sort("Harry")
#hat.sort(input("name:"))

#Class should be used to rerepresent a real life object like a student or a hat.

#Class is like a blueprint/template/mould that allows you to create one or more obj

#instance_methods = writting fxns inside of classes that are automatically passed a refrence to self(the current obj)

#Not every time there needs to be a obj for which class has to exist,smtimes there might be no object
#To use Class as a container of data and functionality that are conceptually related.
#   @classmethods- its a decorator/fxn allows us to do the above

import random
class Hat:
    #basically we dont need init fxn for sm reason idk,maybe bcs we are not gonna instentiate multiple houses, init is meant to initiallize dspecific object frm the blueprint # I think the reason we dont use init here bcs,there aint any object, no obj means no attributes to be declared, so we just gonna take  local variable which serves the purpose
    houses=["gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    #Class variables- They exist in the class itself,there is only one copy of this variable that is shared by all the object,be it a int a str,int or list
    @classmethod
    def sort(cls,name):
        #class is used to refrence the object, while "cls" is used to refrence the class into the fxn,we cant use class as that would conflict with keyword class 
        print(name,"is in",random.choice(cls.houses))
        #houses is not an istance variable,its a class variable, thats why we use cls.houses here

Hat.sort("Harry")
#istentiating hat object is not req here,here i am just accessing a class method inside a Hat class.Thias is how clas methods works
#Python is going to automatically pass some variable via which you can refer to that class in that fxn that you hv implemented inside that class,so that we can do this.Its not that i want a variable called houses locally in this fxn,i want the variable called classes thats associated with this current class 


#to check the type of a class
'''
print(type(50))
#this will give class type int

print(type("Sex"))
#this will give str 

print(type([]))
print(type(list()))
#this will give list

print(type({}))
#this will give dict
'''
#till now we hv studied abt instance variable and instance methods.There r other types too

#             CLASS METHODS
#sometimes its not necessary to associate a fxn with the objects of the class but the class itself.
#sometimes u hv functionality related  to each of the obj that isnt distinct or uniquie for any of the obj,that fxnality is gonna be exactly same no matter the obj in question.U want that fxnality for whole Class itself
# @classmethod-  its another decorator/fxn which is used to specify that this method is not by default an instance method that has the acess to self, the obj itself,this is a class method thats not gonna have access to self but it does know what class its inside.

#        OPERATOR OVERLOADING
#"+" was not just used to add intiger,it was also used for concatination, to join 2 strings,for adding to a list in python
#similarly we can use simple operators for different operations

#In potterworld money that exit are coins called gallions,sickels and knuts
class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.gal=galleons
        self.sick=sickles
        self.knuts=knuts
    #as we know, its a method to define to myself how vault has to be printed
    def __str__(self):
        return f"{self.gal} Galleons, {self.sick} Sickels, {self.knuts} Knuts"
potter=Vault(100,50,25)
print(potter)    

weasley=Vault(25,50,100)
print(weasley)

galleons= potter.gal + weasley.gal
sickles= potter.sick + weasley.sick
knuts= potter.knuts + weasley.knuts

total= Vault(galleons,sickles,knuts)
print(total)

#now we can use overloading the operator + to add two basically objects potter and weasley.If we do it casuallly/normally, it will show "TypeError:unsupported opperand types for 'vault' and 'vault'" 
#To execute this we use special method     -      object.__add__(self,other)
#Source - docs.python.org/3/reference/datamodel.html#special-method-names

class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.gal=galleons
        self.sick=sickles
        self.knuts=knuts
    #as we know, its a method to define to myself how vault has to be printed
    def __str__(self):
        return f"{self.gal} Galleons, {self.sick} Sickels, {self.knuts} Knuts"
    def __add__(self,other):
        galleons=self.gal + other.gal
        sickles=self.sick + other.sick
        knuts=self.knuts + other.knuts
        #Now if this fxn is running, it need to give a fresh output object, a bigger vault that contains all of the contents together,as we ultimately assign that bigger vault obj to "total"
        return Vault(galleons,sickles,knuts)  #By this we are calling my Vault fxn into which we rpassing this no. of coins, so it will give output after running def __str__ through it.
potter=Vault(100,50,25)
print("potter: ",potter)    

weasley=Vault(25,50,100)
print("wealey: ",weasley)

#In python when we do overload an operator like + in bottom line,python sees that and call __add__ method, its gonna pass into the method 2 arguments,whatever the operand is on left of + (potter here) is passed as self and whatever operand is on right of the +(weasley here) gets passed in as other
total=potter + weasley
print("total: ",total)

#Python uses similar way to add lists behind the scenes
'''
    Eg-
    a=[1,2,4]
    b=["sex","what","no"]
    c= a + b
    print(c)
'''
#All the operators that can be overloaded are-
#source- docs.python.org/3/reference/datamodel.html#special-method-names
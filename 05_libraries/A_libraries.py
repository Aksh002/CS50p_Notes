'''
#           MODULES
#When you download python , many libraries are downloaded with it. These modules has fxns you cant access directly like u do to print,etc.Some fxns are tucked away in such modules,so to use them u gotta loadv them in the computer's memory

#           IMPORT Keyword
#import keyword helps us to import fxns from the modules/libraries in python
#            RANDOM MODULE
#random.choice(seq) - choice is a fxn that exist in 'the random module'. it is called using this code. Seq here defines a list/listlike

#Flipping coin
import random
coin=random.choice(["heads","tails","coin not found"])
print(coin)

#Better way to import a fxn frm module
from random import choice
#this basically loads the fxn choice to the scope of the file im working in,so now a fxn named choice gains existance here also, so no need to specify frm where it came frm as its now alocal
coin=choice(["heads","tails","coin not found"])
print(coin)
#prev method of importing can be useful if we also already have a variable named choice in the file, typing random.choice will execute choice fxn frm random and help us differentiate it from the variable choice

#random.randint(a,b) - get a random no. b/w and b
import random
number = random.randint(1,20)
print(number)

#random.shuffle(x) -                
import random
cards = ("jack","queen","king")
random.shuffle(cards)
for card in cards:
    print(card)


#           STATISTICS MODULE/LIBRARY
#to find avg,mean,median,etc

#mean-
import statistics
print(statistics.mean([100,90]))
'''


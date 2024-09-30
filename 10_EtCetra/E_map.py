'''
def main():
    yell("This is Cs50")
def yell(phrase):
    print(phrase.upper())
if __name__=="__main__":
    main()

#Fcking around
def main():
    yell(["This","is","Cs50"])
def yell(phrase):
    for word in phrase:
        print(word.upper(),end=" ")
        #OUTPUT : "THIS IS CS50"
    print()
    for word in phrase:
        print(*word.upper(),end=" ")
        #OUTPUT : "T H I S I S C S 5 0"
        #This happened bcs of the unpacking action of *,it will unpack evry iterated word into words
if __name__=="__main__":as
    main()

#What if we wanna warry the no. of phrases we wanna print
def main():
    yell(["This","is","Cs50"])
def yell(phrase):
    uppercase=[]
    for word in phrase:
        uppercase.append(word.upper())
    print(uppercase)
    #OUTPUT - "['THIS', 'IS', 'CS50']"
    print(*uppercase)
    #OUTPUT - "THIS IS CS50"
if __name__=="__main__":
    main()

#Well we can add more flexibility to it by removing the need for list here, then we can pass as many args as we can pass 
def main():
    yell("This","is","Cs50")
def yell(*phrase ): #*args   #this * will allow it to acceept multiple arguments, now yell will act like print fxn,can pass ass many value as you want
    uppercase=[]
    for word in phrase:
        uppercase.append(word.upper())
    print(uppercase)
    #OUTPUT - "['THIS', 'IS', 'CS50']"
    print(*uppercase)
    #OUTPUT - "THIS IS CS50"
if __name__=="__main__":
    main()

#               MAP
#map is a fxn that used to apply some fxn to evry element of a sequence like list
#map(function,iterable,...)

def main():
    yell("This","is","Cs50")
def yell(*phrase):  
    uppercase=map(str.upper,phrase)
    #map here take 2 arguments, first is the fxn we wanna pass on the every word of the seq,from oops we know that in a class named upper, there is a fxn called upper,we r passing this fxn as str.upper,w/o using () bcs we r passing it into map fxn, not calling it.Secound argument will be phrase here, a tupple containg all the passed i nwords
    print(*uppercase)
if __name__=="__main__":
    main()

#              LIST COMPREHENSION
#making a list without using any loop or append fxn
def main():
    yell("This","is","Cs50")
def yell(*phrase):  
    uppercase=[word.upper() for word in phrase]
    print(*uppercase)
if __name__=="__main__":
    main()

#To add comditional ot it also-
students=[
    {"name":"Hermoine","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"draco","house":"slytherin"}
]
gryffindors=[
    student["name"] for student in students if student["house"]=="Gryffindor"
]
#here we are doin functionality of loops as well as conditionals in one line
for gryffindor in sorted(gryffindors):
    print(gryffindor)

#                FILTER
#There are two ways to solve the above problem 
    #First is by using list configuration and using conditional with it
    #Secound is by using the functional approach where we use filter fxn
#Filter fxn is similar to map in principle, we r gonna pass a fxn init thats gonna be applied to each of the elements in sequence.But map return will return one value for each element in the sequence, thats how we forced all of the words to upper case,but if i wanna conditionally include a student in my rewsulting list,filter can be used
#Filter doesnt expect its first argument to be smthing like str.upper, but a fxn that returns True/False
students=[
    {"name":"Hermoine","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"draco","house":"slytherin"}
]
def is_gryffindor(s):
    return s["house"]=="Gryffindor"   #This will return either true or false

gryffindors=filter(is_gryffindor,students)
#its like it asks whether i should include the current student or not

#for gryffindor in gryffindors:
for gryffindor in sorted(gryffindors,key=lambda s:s["name"]):
    print(gryffindor["name"])

#Actually this Can be done in more concise fashion 
students=[
    {"name":"Hermoine","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"draco","house":"slytherin"}
]

gryffindors=filter(lambda s:s["house"]=="Gryffindor",students)

for gryffindor in sorted(gryffindors,key=lambda s:s["name"]):
    print(gryffindor["name"])


#               DICTIONARY COMPREHENSION
#Its basically a short way to create a dictionary with keys and values without doing that old school process of creating an empty dict and iterating over it to append all the keys and values
students=["Hermoine","Harry","Ron"]
gryffindors=[]
for student in students:
    gryffindors.append({"name":student,"house":"Gryffindor"})
print(gryffindors)

#now by using list comprehension
students=["Hermoine","Harry","Ron"]
gryffindors=[{"name":student,"house":"Gryffindor"} for student in students]
print(gryffindors)
#This will give output as a list of 3 dictionaries

#To get the output as a big dictionary of all the values, we will now use Dictioanry comprehension
students=["Hermoine","Harry","Ron"]
gryffindors={student:"Gryffindor" for student in students}
print(gryffindors)
'''

#               ENUMERATE 
#It solves the problem of indexing by returning both the value and the index one at a time when its being iterated over some sequence
students=["Hermoine","Harry","Ron"]
for i,student in enumerate(students):
    print(i+1,student)



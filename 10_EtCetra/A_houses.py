#                SET
#Its a datatype similar to list only difference is that set doesnt allow repitition of items 
#Sources- docs.python.org/3/libraray/stdtypes.html#set
'''
students=[
    {"name": "Hermoine" , "house": "Grffindor"},
    {"name": "Harry" , "house": "Grffindor"},
    {"name": "Ron" , "house": "Grffindor"},
    {"name": "Draco" , "house": "Slytherin"},
    {"name": "Padma" , "house": "Ravenclaw"}
]
houses= list()  #[]
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
for house in sorted(houses):
    print(house)

#all this can be done easily using set
students=[
    {"name": "Hermoine" , "house": "Grffindor"},
    {"name": "Harry" , "house": "Grffindor"},
    {"name": "Ron" , "house": "Grffindor"},
    {"name": "Draco" , "house": "Slytherin"},
    {"name": "Padma" , "house": "Ravenclaw"}
]
houses= set()
for student in students:
    houses.add(student["house"])
    #add is used for set()

for house in sorted(houses):
    print(house)
'''

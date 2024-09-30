'''
cc=input("camelCase: ")
sc=""
for i in cc:
    if i.isupper():
        sc+="_"+i.lower()
    else:
        sc+=i
print("snake_case: ",sc)
'''
#another way-
cc=input("camelCase: ")
sc=[cc[0].lower()]
for i in cc[1:]:
    if i.isupper():    #if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        


        

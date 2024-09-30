names=[]
while True:
    try:
        name=input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)
if len(names)>1:
    x=names.pop()
s="Adieu, adieu, to "
if names:
    s+=",".join(names)
    if x:   
for i in names:
    s=s+i+","
s=s[:-1]
if len(names)>1:
    print("\n",s+" and "+x)
else:
    print("\n",s)
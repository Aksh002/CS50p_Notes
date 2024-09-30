due=50
while due>0:
    print("Amount due: ",due)
    coins=int(input("Insert coins: "))
    if coins==25 or coins==10 or coins==5:
        due=due-coins
    else:
        continue
else:
    print("Change owed: ",abs(due))




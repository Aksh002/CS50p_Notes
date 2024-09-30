list=[]
while True:
    try:
        x=input()
    except EOFError:
        break

    else:
        for i in list:
            if i["item"]==x:
                item["count"]+=1
            else:
                item={"name":x,"count":1}
                list.append(item)

for i in list:
    print(i['count'],i['item'],sep=" ")

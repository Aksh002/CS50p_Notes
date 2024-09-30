import random
while True:
    try:
        lv=int(input("Level: "))
    except ValueError or (lv<0):
        continue
    else:
        break

x=random.randint(lv)
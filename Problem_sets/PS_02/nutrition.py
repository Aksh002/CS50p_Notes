fruits={
    "apple":130,
    "Avocado":50,
    "Banana":110,
    "Cantaloupe":50,
    "Grape fruit":60,
    "Grapes":90,
    "HoneydewMelon":50,
    "Kiwifruit":90,
    "Lemon":15,
    "Lime":20,
    "Nectarine":60,
    "Orange":80,
    "Peach":60,
    "pear":100,
    "Pineapple":50,
    "Plums":70,
    "Strawberries":50,
    "Sweet Cherries":100,
    "Tangerine":50,
    "Watermelon":80,
}
item=input("Item: ")
for i in fruits:
    if i==item:
        print("Calories:",fruits[i])
    else:
        continue

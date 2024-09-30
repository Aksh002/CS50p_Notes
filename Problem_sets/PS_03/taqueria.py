menu={
    "Baja Taco":4.25,
    "burrito":7.50,
    "bowl":8.50,
    "nachos":11.00,
    "Quesadilla":8.50,
    "Super burrito":8.50,
    "Super quesadilla":9.50,
    "taco":3.00,
    "tortilla salad":8.00
}
total=0.00
while True:
    try:
        item=input("Item:")
    except EOFError:
        break
    else:
        for i in menu:
            if i==item:
                total=total+menu[i]
                if i=="Baja Taco":
                    print("$",total)
                else:
                    print("$",total,0,sep="")
            else:
                continue

        

    
        
    
    


import csv
name=input("Whats your name?")
home=input("Wheres your home?")
with open("students4.csv","a") as file:
    writer=csv.writer(file)
    writer.writerow([name,home])
  
#there is an another way to write names in file without the restriction of keeping an order of writting names first and home 2nd.We can use dictionary to keep track of whats name and whats home
import csv
name=input("Whats your name?")
home=input("Wheres your home?")
with open("students4.csv","a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})

#Doubt- fieldnames were not required while using Dictreader while its used in dictwriter,aisa kyu?


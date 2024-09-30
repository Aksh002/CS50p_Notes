

'''students=[]
with open ("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''
import re
email=input("Whats your email?").strip()  
if re.search(r"^\w+@\w+\.\w+\.edu$",email):     
    print("Valid")
else:
    print("Invalid")
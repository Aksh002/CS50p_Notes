#              DICT READER
#If we use a csv.DictReader instead of reader only, it will iterate over the file loading in each line not as a list of coloumns but as a dictionary of colounms.
#DictReader will infer from the first row of csv file abt what those colounms are called.we dont hv to store data in list first then create a dict and transfer data into it and then append that dict in list.
#That first row works as a title of the whole colounm  
#This code works even if the colounms are interchanged in file,in prev code,it would hv break,this is its advantage
import csv
students=[]
with open("students3.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"home":row["home"]}) #these names like name and home r assigned from row 1 of file

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")

#As dictreader returns 1 dictionary at a time,so when u loop over reader,each row is alr gonna be a dictionary so no need to make another dictionary while appending, just append row itself

import csv
students=[]
with open("students3.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")

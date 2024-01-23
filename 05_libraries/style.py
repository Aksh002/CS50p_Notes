#               PEP8
#Detailed source- peps.python.org/pep-0008/

#Readability counts-
'''
A style guide is about consistency. Consistency with this style guide is important.
Consistency within a project is more important. Consistency within one module or
function is the most important
'''
#read the style guide for more info

#               pylint
'''
- its a program that stastically analyse the full code and try to find out if there are potential mistakes or inconsistencies
- download link = pycodestyle.pycqa.org
- This program is little bit noisy for large codes,overwhelming you with no. of errors u did stylistically, even if u wrote ur best code
- Can be installed by "pip instal pylint" 
- Source- pycodestyle.pycqa.org
'''

#             pycodestyle(pep8)
#source-pycodestyle.pycqqa.org
#pip instal pipcodestyle

#             black
#source- black.readthedocs.io
#its quite a opinionated style tool which pre decides most of the style for u

'''
students={"Hermione":"Gryffindor","Harry":"Gryffindor","Ron":"Gryffindor","Draco":"Slytherin"}
for student in students:
    print (student)
'''
#If u run "black <file name>" in terminal, tool will convert ur code to this-
'''
students={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}
for student in students:
    print (student)
'''
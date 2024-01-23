'''
x=int(input("x="))
z=x.isnumeric()
print(z)

x=float(input("x="))
y=float(input("y="))
z=x/y
print(f"{z:.2f}")

name=input("Whats your name?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("who?")

while True:
    n=int(input("n="))
    if n<0:
        continue
    else:
        break
print(n)
for _ in range(n):
    print("meow")

print(pow(3,2))
def main():
    x=int(input("X="))
    y=int(input("Whats the power?="))
    print(f"X with power {y} is =",square(x,y))

def square(n,z):
    return pow(n,z),#n*n can be used if only squared is wanted
main()

def hellow(to="world"):
    print("hello,",to)

name=input("Whats ur name?")
hellow(name)

data = {'C':20, 'C++':15, 'Java':30, 
        'Python':35}
courses = list(data.keys())
values = list(data.values())
print(courses)
'''


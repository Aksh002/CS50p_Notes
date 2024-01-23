def main():
    x=int(input("X="))
    y=int(input("Whats the power?="))
    a=power(x,y)
    print(f"X with power {y} is =",a)
#mod

def power(n,z):
    p=pow(n,z),#n*n can be used if only squared is wanted
    return p
#main()

#use code given below to make sure that when i import a square named fxn from another library(file treated as a library),i wanna make sure that main is not atomatically  called itself

if __name__=="__main__":
    main() 
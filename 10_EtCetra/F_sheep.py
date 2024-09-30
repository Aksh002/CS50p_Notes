#               GENERATORS

'''
def main():
    n=int(input("Enter no. of sheeps: "))
    for s in sheep(n):
        print(s)
def sheep(n):
    flock=[]
    for i in range(n):
        flock.append("🐑"*i)
    return flock
if __name__=="__main__":
    main()
'''
# If the input is 1000000, it will show "MemoryError",
#To solve this we use generators,we can define a fxn as a generator whereby it can still generate a massive amount of data for your users,but you can have it return just a little bit of data at a time
#Source - docs.python.org/3/howto/functional.html#generators

#Fact- Do not use return keyword in the middle of  for loop bcs it will return the value for the ifrst iteration only and will terminate
    
#               YIELD
#Through using yield instead of return, you can yield python to effictively return just one value at a time from this loop,the for loop will keep working and i will keep counting from 0 to 1 million but each time, the fxn is gonna hand us back just a little piece of info.Its gonna generate that little pice of data, not all of them at once.Before we were storing 1 million rows which was not possible to store at once
def main():
    n=int(input("Enter no. of sheeps: "))
    for s in sheep(n):
        print(s)
def sheep(n):
    for i in range(n):
        yield "🐑"*i
if __name__=="__main__":
    main()
#now this code will instantly start printing without the delay that was happening to store that whole chunk of data
#WE can use "CTRL + C" to terminate this foreEver running program

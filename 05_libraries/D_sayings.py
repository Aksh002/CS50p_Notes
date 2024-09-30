'''
#To bundle up the code that i keep reusing, we make our own Pyhton Module or Package.We can keep it local on my pc, or make it open scource and putting on pypi
def main():
    hello("World")
    goodbye("World")
def hello(name):
    print(f"Hello {name}")
def goodbye(name):
    print(f"Goodbye {name}")
main()
'''
#THe output u will get  on typung "python say.py Akshit" will be -
        #Hello World
        #Goodbye World
        #Hello Akshit
#This is happening because whenever the file is getting loaded/readed by python for importing hello fxn to say.py, main is gonna get read and called, even if u=im just importing one fxn of this file 

#To fix this we use __name__ wala statement in sayings.py
#                                           __name__
#This is a special variable whose value is automatically assigned by python to be main when u run a file from command line, if its being run bcs of loading of file due to a call
def main():
    hello("World")
    goodbye("World")
def hello(name):
    print(f"Hello {name}")
def goodbye(name):
    print(f"Goodbye {name}")
if __name__=="__main__":
    main()



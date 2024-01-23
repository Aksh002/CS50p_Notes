from hellow2 import hello


def test_default():
    assert hello("Akki")=="hello Akki"

def test_argument():
    assert hello()=="hello world"

#we can also use loops to pass multiple values 
def test_argument():
    for name in ["Hermione","Harry","Ron"]:
        assert hello(name)==f"hello {name}"


#We can also organise our testing,we can store all the testing files at one place.Make a directory named test using mkdir, make a file named test_hello2.py and write all the code, then make another file in the dir named "__init__",this file will tell python to treat that directory/folder,not just a module but as a PACKAGE
#PACKAGE - Package are multiple python module organised in a folder
#We can add more test to files subjected to different python files in this directory/package
#We can just type "pytest <dir name>" and all the test will run.
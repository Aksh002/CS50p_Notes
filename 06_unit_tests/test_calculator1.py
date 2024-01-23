from calculator1 import power 
'''
def main():
    test_power()

def test_power():
    if power(2,2) != (4,):
        print("2 squared was not 4")
    if power(3,2) != (9,):
        print("3 squared was not 9")
    else:
        print("OH BHAIA,AAAAAALL IIIIIS WEEEEEEL!!!!!")
if __name__=="__main__":
    main()
'''

#                ASSERT KEYWORD
#It simply assert that this stament is true for the code, if that statement is actually true u r gonna see nothin happining, but if its not Assertion error comes up
'''
def test_power():
    assert power(2,2) == (4,)
    assert power(3,2) == (9,)

if __name__=="__main__":
    main()

#to fix this Assertion error, we use our own try me method
def test_power():
    try:
        assert power(2,2) == (4,)
    except AssertionError:
        print("2 Squared was not 4")
    try:
        assert power(3,2) == (9,)
    except AssertionError:
        print("3 squared was not 9")
if __name__=="__main__":
    main()

#lets add some more test
def test_power():
    try:
        assert power(2,2) == (4,)
    except AssertionError:
        print("2 Squared was not 4")
    try:
        assert power(3,2) == (9,)
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert power(-2,2) == (4,)
    except AssertionError:
        print("-2 squared was not 9")
    try:
        assert power(-3,2) == (9,)
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert power(0,2) == (0,)
    except AssertionError:
        print("0 squared was not 9")
    
if __name__=="__main__":
    main()
#to make this long and tidious task of testing easy,we use a library pytest
'''
#               PYTEST LIBRARY
#resources- docs.pytest.prg
def test_power():
    assert power(2,3)==4
    assert power(3,2)==9
    assert power(-2,2)==4
    assert power(-3,2)==9
    assert power(0,2)==9
#writting "pytest test_calculator.py" in terminal will give a detailed report on where n which assert term is facing assertion failures, if no issues it will show test passed

#using this method, errror will be showen for first failed assertion fxn only, the rest assertion wont even get run/get tested, to fix that
def test_positive():
    assert power(2,3)==4
    assert power(3,2)==9

def test_negative():
    assert power(-2,2)==4
    assert power(-3,2)==9

def test_zero():
    assert power(0,2)==9

#RANDOM NOTE- Make a sapparate file to "try test" the user input by importing the fxn(just like we did here), it makes code look clean
#Q-- What is the diif between pip installing the library and importing a library?
#Ans-- Pip install is used to instal yhe library in the system , while import keyword imports the library to be used in the current file. A library can not be imported if its not installed already.

#If the calculator.py code doesnt have int written before asking for input frm the user and the user inputs a string, then the code will show Type error, to check that we will provide a str test for it too
import pytest

def test_str():
    with pytest.raises(TypeError):
        power("cat")
import pytest
from functions import *

#import file test cases
def test_openFile_correct():
    assert openFile("test.txt") == None

def test_openFile_data():
    assert openFile(4) == None

def test_openFile_not():
    assert openFile("rest.txt") == None

#dist test cases
def test_dist_correct():
    assert dist(2.0, -3.0, 5.0, 1.0) == 5.0

def test_dist_round():
    assert dist(-3.0, 4.0, 2.0, 1.0) == 6.0

#meant to fail
def test_dist_incorrect():
    assert dist(9.0, 4.0, 3.0, 1.0) == 51.0

#meant to fail
def test_dist_data():
    assert dist("two", 3.0, 6.0, 5.0) == 10.0


## pytest testing function 1: testing correct input

def test_numbers():

    assert numbers(6,2) == 3

## purposefully FAILING numbers function

def test_numbers_fail():

    assert numbers(8,4) == 5

## test numbers with dividing with remainders

#purposely failing test case
def test_numbers_fix():

    assert numbers(5,2) == 2.5
    
 # isPalindrome test cases
@pytest.mark.parametrize("temp,palindrome",[("madam",True),("racecar",True),("bob",True),("peanut",False),("A5B8C10",False),(10101,False)])
def test_isPalindrome(temp,palindrome):
    assert isPalindrome(temp) == palindrome

#divide test cases
##multiple inputs

def geninputs():

    inputs = ["6","3"]

    for item in inputs:

        yield item

##sets our inputs

GEN = geninputs()



##test 1 for divide where it works

def test_divide(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: next(GEN))



    assert divide() == None



##multiple inputs test 2

def wronginputs():

    inputs = ["8","4"]



    for item in inputs:

        yield item

## set up inputs

WRO = wronginputs()



##test 2 for divide where it FAILS

def test_divide_fail(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: next(WRO))



    assert divide() == 3.0

## test output for dividing with remainders

def fixinputs():

    inputs = ["5","2"]



    for item in inputs:

        yield item

## set up inputs

FIX = fixinputs()



##test 3 for divide: fixed code so remainders are allowed

def test_divide_fix(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: next(FIX))



    assert divide() == None

    
# test cases for sq
@pytest.mark.parametrize("num, sqr", [(25,5),(49,7),(-30,None),("abc",None)])

def test_sq(num,sqr):
    assert sq(num) == sqr

 

#Tests for greetUser function
def test_greetUser_specialChars():
    assert greetUser('i', '\n', '\t') == None

def test_greetUser_strs():
    assert greetUser("Sally", "sold", "shells") == None

def test_greetUser():
    assert greetUser(True, 5.0, None) == None

#tests for displayItem function
def test_displayItem():
    assert displayItem([], 5) == None

def test_displayItem_inRange():
    assert displayItem([1, 2, 3, 4, 5, 6], 5) == None

def test_displayItem_nullInput():
    assert displayItem(None, 5) == None

#test negative indexing
def test_displayItem_negIn():
    assert displayItem([1, 2, 3, 4, 5, 6], -5) == None

def test_displayItem_negOut():
    assert displayItem([1, 2, 3, 4, 5, 6], -10) == None

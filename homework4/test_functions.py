import pytest
from functions import *

#import file test cases
def test_openFile_correct():
    assert open("test.txt")

def test_openFile_data():
    assert open(4)

def test_openFile_not():
    assert open("rest.txt")

#dist test cases
def test_dist_correct():
    assert dist(2.0, -3.0, 5.0, 1.0) == 5.0

def test_dist_round():
    assert dist(-3.0, 4.0, 2.0, 1.0) == 6.0

def test_dist_incorrect():
    assert dist(9.0, 4.0, 3.0, 1.0) == 51.0

def test_dist_data():
    assert dist("two", 3.0, 6.0, 5.0) == 10.0


## pytest testing function 1: testing correct input

def test_numbers():

    assert numbers(6,2) == 3

## purposefully failing numbers function

def test_numbers_fail():

    assert numbers(8,4) == 5

## test numbers with dividing with remainders

#purposely failing test case
def test_numbers_fix():

    assert numbers(5,2) == 2.5

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

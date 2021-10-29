import pytest
from functions import *

## pytest testing function 1: testing correct input

def test_numbers():

    assert numbers(6,2) == 3

## purposefully failing numbers function

def test_numbers_fail():

    assert numbers(8,4) == 5

## test numbers with dividing with remainders

def test_numbers_fix():

    assert numbers(5,2)== 2.5

#Tests for greetUser function
def test_greetUser_specialChars():
    assert greetUser('i', '\n', '\t') == None

def test_greetUser_strs():
    assert greetUser("Sally", "sold", "shells") == None

def test_greetUser():
    assert greetUser(True, 5.0, None) == None

#tests for greetUser function
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

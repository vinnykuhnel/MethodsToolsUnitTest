import pytest
from functions import *

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
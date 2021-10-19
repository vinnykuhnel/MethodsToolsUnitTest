import pytest
from functions import *

def test_greetUser():
    assert greetUser("Sally", "sold", "shells") == None

def test_displayItem():
    assert displayItem(None, 5) == None
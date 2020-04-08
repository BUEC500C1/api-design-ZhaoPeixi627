import pytest
from Assigment2 import *

def test_ttt():
    assert predict(123) == "Wrong Input"
    assert predict("Shanghai") == "Wrong Input"
    assert predict('Chengdu Shuangliu International Airport') != None
    assert predict('Boston Aerodrome') != None
    assert predict('Beijing Capital International Airport') != None
    assert predict('John F Kennedy International Airport') != None
    assert predict('xyz') == "Wrong Input"
    

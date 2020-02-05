from assigment2 import ttt

def test_ttt():
    assert ttt('Chengdu Shuangliu International Airport') == 'Chengdu'
    assert ttt('Boston Aerodrome') == 'Boston'
    assert ttt('Beijing Capital International Airport') == 'Beijing'
    assert ttt('John F Kennedy International Airport') == 'New York'
    assert ttt('Los Angeles International Airport') == 'Los Angeles'
    
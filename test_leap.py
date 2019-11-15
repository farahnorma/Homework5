#Norma
#test_leap.py

def is_leap(y):
    if y%4 ==0:
        if y%100 ==0:
            if y%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def test_1():
    assert True == is_leap(2016)

def test_2():
    assert True == is_leap(1904)

def test_3():
    assert False == is_leap(1900)

def test_4():
    assert False == is_leap(2003)

def test_5():
    assert True == is_leap(1600)

def test_6():
    assert True == is_leap(83740)

def test_7():
    assert False == is_leap(100)

def test_8():
    assert True == is_leap(16)

def test_9():
    assert False == is_leap(-1300)

def test_10():
    assert True == is_leap(-1600)
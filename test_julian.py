def julian(month, day, y):
    daynum = 31 * (month - 1) + day
    if month > 2:
        if is_leap(y) is True:
            daynum = daynum - (4 * month + 23) // 10
            daynum = daynum + 1
            return daynum
        else:
            daynum = daynum - (4 * month + 23) // 10
            return daynum
    else:
        return daynum


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
    assert julian(3,1, 2001) == 60
def test_3():
    assert julian(1,1, 2001) == 1
def test_2():
    assert julian(12,31, 2001) == 365
def test_4():
    assert julian(3,28, 2001) == 87


def test_5():
    assert julian(1,1, 2000) == 1
def test_6():
    assert julian(12,31, 2000) == 366
def test_7():
    assert julian(2,29, 2000) == 60

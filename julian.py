#Norma
#julian.py

def valid(month, day, y):
    if y <0:
        print("Invalid date")
    else:
        if month<1 or month>12:
            print("Invalid date")
            return False
        elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if day<1 or day >31:
                print("Invalid date")
                return False
            else:
                return True
        elif month == 4 or 6 or 9 or 11:
            if day<1 or day>30:
                print("Invalid date")
                return False
            else:
                return True
        elif month == 2:
            if is_leap(y) is True:
                if day<1 or day >29:
                    print("Invalid date")
                    return False
                else:
                    return True
            else:
                if day<1 or day>28:
                    print("Invalid date")
                    return False
                else:
                    return True


def julian(month, day, y):
    is_leap(y)
    valid(month, day, y)
    if valid(month, day, y) is True:
        daynum = 31*(month-1)+day
        if month >2:
            if is_leap(y) is True:
                daynum = daynum - (4 * month + 23) // 10
                daynum = daynum+1
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


def main():
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    y = int(input("Enter year: "))
    julian(month, day, y)
    result =julian(month, day, y)
    print('Your julian date is: ', result)


main()
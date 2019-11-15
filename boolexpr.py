#Norma
#boolexpr.py



def is_in_semester(month,day):
    if month < 5 or month >7: #True when month/day between May 28 2019-July 18 2019
        return False
    elif month >5 and month < 7:
        if day !=0:
            return True
        else:
            return False
    elif month == 5:
        if day < 28:
            return False
        else:
            return True
    elif month ==7:
        if day >18:
            return False
        elif day ==0:
            return False
        else:
            return True



def main():
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    is_in_semester(month, day)

    if is_in_semester(month, day) == True:
        print('month/day is in Summer Semester')
    else:
        print('month/day is NOT in Summer Semester')

main()
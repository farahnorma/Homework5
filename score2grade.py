#Norma
#score2grade.py

def grade(score):
    letter = ''
    if score >=0 and score <= 100:
        if score >= 90:
            letter = 'A'
            return letter
        elif score >= 80:
            letter = 'B'
            return letter
        elif score >=70:
            letter = 'C'
            return letter
        elif score >=60:
            letter='D'
            return letter
        else:
            letter = 'F'
            return letter
    else:
        letter ='Bad input'
        return letter


def main():
    score = int(input('Score from 0 to 100: '))
    grade(score)
    answer = grade(score)
    print('Letter grade is: ', answer)

main()

#Norma
#speeding.py


def speeding(speed_limit, measured_speed):
    fine = 0.0
    if speed_limit >= measured_speed:
        return fine
    else:
        if speed_limit <90 and measured_speed >90:
            dif = measured_speed - speed_limit
            fine = dif*5 +50+200
            return fine
        else:
            dif = measured_speed- speed_limit
            fine = dif*5+50
            return fine


def main():
    speed_limit = float(input('Speed Limit: '))
    measured_speed = float(input('Measured Speed: '))
    speeding(speed_limit, measured_speed)
    f = speeding(speed_limit, measured_speed)
    if speed_limit >= measured_speed:
        print('Speed is legal')
    else:
        print('Illegal speed, fine is $', f)


main()


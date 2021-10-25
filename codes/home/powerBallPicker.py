# genereate 5 number 1-65 no duplicate

import secrets

powerballnums = []
powerball = []

while len(powerballnums) < 5:

    pbnum = secrets.randbelow(70)

    if pbnum > 0:
        if pbnum not in powerballnums:
            powerballnums.append(pbnum)

while len(powerball) == 0:
    luckyBall = secrets.randbelow(27)

    if luckyBall > 0:
        powerball.append(luckyBall)

powerballnums.sort()

print('Powerball numbers are: %s Powrball is %s' % (powerballnums, powerball))

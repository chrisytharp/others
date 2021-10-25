#otp 'One Time Pad' random 55 .upper() alpha letters

import secrets
'''
secrets.randbelow(10)       #will return a random number between 0 to up to # of arg ...ie 10

secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')        #will return random choice in the STRING or LIST given

x = 'whale'
secrets.choice(['cat', 10, 'dog', x])
'''

otp = ''

for i in range(55):
    otp += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # otp = otp + secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

print(otp)

#Two Time Pad = is a otp encrypting 2 seperate messages

# Crypto Math Module

#   import cryptoMath
#   cryptoMath.gcd(24, 32)
# >>> 8
#   cryptoMath.gcd(37, 41)
# >>> 1
# cryptoMath.findModInverse(7, 26)
# >>> 15
#cryptoMath.findModInverse(8953851, 26)
# >>> 17

# EUclid's Algo for finding greatest common denominator aka GCD

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#print(gcd())

#Euclid's extended algo to find the modular inverse of a numbers

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None   #no mod inverse if a & m are NOT relatively prime (co-prime)
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3    #NOTE that // is the int division operator "floor division"
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

#is there a function finding realitively prime numbers 'coprime numbers'
# gcd(a, b) == 1

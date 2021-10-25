# HOW TO USE in IDLE
# import primeNum
#
# primeNum.generateLargePrime()     # output is Large Prime #
# primeNum.isPrime(22)              # output False
# primeNum.isPrime(21)              # output True
#
# isPrimeTrialDiv() = trial division algorith, to return TRUE if the # passed to it is prime: FALSE if # is not Prime
#
# primeSieve() = uses Sieve of Erathosthenes algo to generate prime numbers ! use to check prime #'s in small range of #'s!
#
# rabinMiller() = !!Use this to check if a LARGE number is prime!! ALSO this Test Likely hood!!! false positive may occur but do happen!!
#                   ses Rabin-Miller algo to check if # passed to it is a PRIME #. this algo (unlike isPrimeTrialDiv) can work
#                 quickly on Very Large numbers. This func is not called directly but by "isPrime()"
#
# isPrime() = called to determine if a number is Prime or Not
#
# generateLargePrime() = returns Large Prime # that is hundreds of digits long. Will be used in makeOublicPrivateKey.py

# Meant to be imported!!!

import math, random


def isPrimeTrialDiv(num):
    # Returns True if Prime numbe, otherwise False
    # Uses trial division algo for testing Primality

    # All numbers less than 2 are not Prime:
    if num < 2:
        return False

    # See if num is divisible by any number up to the square root of num:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primeSieve(sieveSize):
    # Return a list of prime numbers calculated using the Sieve of Eratosthenes algorithm:
    sieve = [True] * sieveSize
    sieve[0] = False    #Zero and one are Not Prime Numbers
    sieve[1] = False

    # Create the sieve:
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i    # pointer = pointer + 1

            # Compile the list of Primes:
            primes = []
            for i in range(sieveSize):
                if sieve[i] == True:
                    primes.append(i)
            return primes

def rabinMiller(num):
    # Returns True if num is Prime #:
    if num % 2 == 0 or num < 2:
        return False    # Rabin-Miller doesnt work on even integers
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving 's' until it is odd & use 't' to count how many times we halve 's':
        s = s // 2
        t += 1  # t = t + 1
    for trials in range(5):     # Try to falsify num's primality 5 times:
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:          # This test does Not apply if 'v' is '1'
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1  # i = i + 1
                    v = (v ** 2) % num
    return True

# most of the time we can quickly determine if a num is not prime by dividing by the first few dozen Prime Numbers.
# this is quicker than rabinMiller() but does not detect all composites!!

LOW_PRIMES = primeSieve(100)    # this is a list of all prime numbers that are less than 100-
                                # NOTE: we use the primeSieve(0 to get the LIST

def isPrime(num):
    # Return True if # is prime #.
    # Faster prime # check than rabinMiller()
    if (num < 2):
        return False    # zero(0), one (1) & negative numbers are Not Prim

    for prime in LOW_PRIMES:
        if num == prime:
            return True
        if num % prime == 0:
            return False
    # If all else fails, call rabinMiller() to determine if 'num' is Prime:
    return rabinMiller(num)

def generateLargePrime(keysize=1024):       #defaultKeysize is 1024
    # Return a Random Prime Number that is keysize bits in size:
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

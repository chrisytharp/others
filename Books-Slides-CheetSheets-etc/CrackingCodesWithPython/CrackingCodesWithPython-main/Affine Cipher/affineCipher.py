# Affine Cipher has 1320 possible keys ad is a weak cipher

import sys, pyperclip, cryptoMath, random
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
    #myMessage = input("""enter in message you want to encrypt \n >   """)
    myMessage = """a computer would deserve to be called intelligent if it could deceive a human into believing that it was human - Alan Turing"""
    #myKey = int(input('enter encryption key \n >  '))
    #myKey = 2894
# creating keys can be difficult so we can use getRandomKeys()
    myKey = getRandomKey()         # this func() returns A INT of the product of keyA * len(SYMBOLS) + keyB
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed test:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard' % (myMode))


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) -1:
        sys.ext('Key A must be greater than 0 and Key B must be between 0  and %s.' % (len(SYMBOLS) - 1))
    if cryptoMath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Kay A (%s) and the symbol set size (%s) are not relative prime numbers (aka co-prime) Choose a different Key' % (keyA, len(SYMBOLS)))


def encryptMessage(key, mesasge):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in mesasge:
        if symbol in SYMBOLS:
            # Encrypt the symbol
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]   #ciphertext = ciphertext + SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)] | ciphertext ='h
        else:
            ciphertext += symbol    #Append the symbol without encrypting 'ciphertext = ciphertext + symbol
    return ciphertext


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInveerseOfKeyA = cryptoMath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInveerseOfKeyA % len(SYMBOLS)]  #plaintext = plaintext + SYMBOLS[(symbolIndex - keyB) * modInveerseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol #  Append symbol without decrypting
    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

#If affineCipher.py is run (instead imported as a module), call the main function:
if __name__ == '__main__':
    main()

# Simple Substitution Cipher

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    #myKey = getRandomKey()
    myMode = 'encrypt'  # Set to 'encrypt' or 'decrypt'

    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is :' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard')

def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()

    return keyList == lettersList

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        #For decrypting we can use the same code as encrypting. We just
        #  need to swap where the 'key' and 'LETTERS' strings are used
        charsA, charsB = charsB, charsA

    # Loop through each symbol in message
    for symbol in message:
        if symbol.upper() in charsA:
            #  Encrypt or Decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated +=charsB[symIndex].upper()   # translated = translated + charsB[symIndex].upper()
            else:
                translated +=charsB[symIndex].lower()   # translated = translated + charsB[symIndex].lower()
        else:
            #symbol is NOT in LETTERS; just add it
            translated += symbol                        # translated = translated + symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()

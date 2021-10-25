#otp 'One Time Pad'

import pyperclip, secrets

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #myMessage = input('''Enter in message: \n> ''')
    myMessage = """ a Dell CPi notebook computer, serial # VLQLW, was found abandoned along with a wireless PCMCIA card and an external homemade 802.11b antennae. It is suspected that this computer was used for hacking purposes, although cannot be tied to a hacking suspect, Greg Schardt. Schardt also goes by the online nickname of “Mr. Evil” and some of his associates have said that he would park his vehicle within range of Wireless Access Points (like Starbucks and other T-Mobile Hotspots) where he would then intercept internet traffic, attempting to get credit card numbers, usernames & passwords."""

    myKeyLength = str(len(myMessage))
    keyLength = len(myMessage)
    myKey = ''

    for i in range(keyLength):
        myKey += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # otp = otp + secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    myMode = 'encrypt'  # 'encrypt' or 'decrypt'
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print(""" \n Encryption Key Length is (%s) Characters. \n\n Encryption Key is: %s \n\n %sed message:\n %s""" % (myKeyLength, myKey, myMode.title(), translated))
    pyperclip.copy(translated)
    print('\nThe message has been copied to the clipboard')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []         #stores the emcrypted | decrypted message

    keyIndex = 0
    key = key.upper()

    for symbol in message:     #Loop through ea symbol (char) in message
        num = LETTERS.find(symbol.upper())
        if num != -1:      #  -1 means symbol.upper() was not found in LETTERS (can i use 'if num not in LETTERS)
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # ADD if encrypting# ADD if encrypting \\the keyIndex var keeps track of which subkey to use & is always what key[keyIndex] eva;luates to
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])  # Subtract if decrypting

            num %= len(LETTERS)   #Handle wrap around

            # ADD the encrypted\decrypted symbol to the end of transalted
            if symbol.upper():
                translated.append(LETTERS[num])
            elif symbol.lower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # Move to the next letter in the key
            if keyIndex == len(key):    # if the end of the key is reached we need to reset index back to the beginning of key
                keyIndex = 0
        else:
            # Append the symbol without encrypting | decrypting
            translated.append(symbol)

    return ''.join(translated)

# if script is run call main function
if __name__ == '__main__':
    main()

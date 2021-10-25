# Vigenere Cipher is like the Caser cipher but has more keys: subkeys
#Brute-force proof
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = """ Alan mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    #myMessage = input('Enter in cipher: \n > ')
    myKey = 'ASIMOV'
    myMode = 'encrypt' # 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('The message has been copied to the clipboard')

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

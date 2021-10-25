# Affine Cipher Hacker

import pyperclip, affineCipher, detectEnglish, cryptoMath

SILENT_MODE = False   #True or False

def main():
    myMessage = """1QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RQ-Q5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        #plaintext displayed on screen for user convenience
        print('Copying Hacked Message To Clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed o hack encryption')

def hackAffine(message):
    print('Hacking...')
    print('(Press Ctrl+C or Ctrl+D to quit at anytime.)')

    #Brute-Forcing by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue                    #if keyA & symbol set total is not relatively prime(coprime) return to for statement to try new key(w\ the new iteration key)
        decryptedText = affineCipher.decryptMessage(key, message)   # if key is valid take (key, message) & decrypt
        if not SILENT_MODE:
            print('Tried key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            #check with user if the decrypted kay has been found
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for donce, or just press Enter to continue hacking:')
            response = input('>  ')

            if response.strip().upper().startswith('D'):
                return decryptedText
            else:
                continue
    return None
#if ran (instead of imported as module), call this main( 0function
if __name__ == '__main__':
    main()

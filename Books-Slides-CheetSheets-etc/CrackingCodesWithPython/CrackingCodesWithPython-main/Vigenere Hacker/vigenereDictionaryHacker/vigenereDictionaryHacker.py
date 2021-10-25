# Vigenere Dictionary Hacker

import detectEnglish, vigenereCipher, pyperclip


def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print("Copying hacked message to clipboard:")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack')

def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt', 'r')        #default 'r'
    words = fo.readlines()                   # readlines() - 'YOUTHFULLY\n', 'YOUTHFULNESS\n',  #read() - ZULU, ZULUS, ZURICH
    fo.close()

    for word in words:
        word = word.strip()     #Remove the newline \n at the end
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage = 40):
            #check with USER to see if the decrypted key has been found:
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ':' + decryptedText[:100])
            print('\n' + 'Enter D for done, or just press ENTER to continue breaking:')
            response = input('> \n')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()

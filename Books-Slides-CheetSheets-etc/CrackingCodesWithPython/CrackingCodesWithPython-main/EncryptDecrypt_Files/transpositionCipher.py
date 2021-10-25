#Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = input("Enter in clear text to convert to cipher text: \n")
    #myMessage = 'Common sense is not common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    #print cipher text w/ | after to ensure there isnt any spaces after text
    print(ciphertext + '|')

    #copy to clipboard
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    #ea string in ciphertext represents a column
    ciphertext = [''] * key

    #loop through ea column in ciphertext
    for column in range(key):
        currentIndex = column

        #keep looping until currentIndex goes past message length:
        while currentIndex < len(message):
            #place ea char at currentindex in message at the end of the current
            # column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            #move currenIndex over
            currentIndex += key

    #conver the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)

#if transpositioncipher.py is run (instead of imported as a module) call
#  the main(0 function:

if __name__ == '__main__':
    main()

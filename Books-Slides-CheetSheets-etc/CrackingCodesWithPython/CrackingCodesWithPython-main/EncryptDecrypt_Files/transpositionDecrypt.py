#Transposition Cipher Decryption

import math, pyperclip

def main():
    #myMessage = input('message to decrypt:\n')
    #myKey = input('encrypt\decrypt key')
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    #print with a "pipe" char after it. in case
    #there are spaces at the end of the decrypted msg
    print(plaintext, '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    #transposition decrypt func will simulate the "columns" &
    # "rows" of the grid that the plaintext is written on by
    # by using a list of string. First, we need to calc...

    #The # of "columns" in our transposition gris:
    numOfColumns = int(math.ceil(len(message) / float(key)))   #math.ceiling rounds up

    #The # of "rows" in our grid
    numOfRows = key

    #The # of shaded boxes in the last column
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Ea string inplaintext reps a column in the grid:
    plaintext = [''] * numOfColumns

    # The column and row vars point to where in the grid the next
    # char in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1         #point to next column

        # If there are no more columns OR we're at shaded box, go
        #  back to 1st column next row
        if (column == numOfColumns) or (column == numOfColumns -1 and row >=
            numOfRows - numOfShadedBoxes):
                column = 0
                row += 1
    return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported as a module),
#   call the main(0 function:
if __name__ == '__main__':
    main()

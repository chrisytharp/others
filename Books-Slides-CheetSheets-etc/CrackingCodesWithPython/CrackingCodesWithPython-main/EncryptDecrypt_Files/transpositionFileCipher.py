#Transposition Cipher Encrypt/Decrypt Files

import time, os, sys, transpositionCipher, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'

    #If file with the same 'outputFilename' exists it will override it
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'decrypt'  # Set to 'encrypt' OR 'decrypt'


    #If filename does not exist Program should terminate
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename)) # or ...% (inputFilename))
        sys.exit()

    #If the outputFilename already exists: give user chance to quit:
    if os.path.exists(outputFilename):
        print('this will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('>')
        if not response.lower().startswith('c'):
            sys.exit()

    #Read in the message from the file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    #Measure how long Encrypion/ Decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionCipher.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))
    #Vars 'content' and 'translated' now exist

    #Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')           #create new file
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

#If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function
if __name__ == '__main__':
    main()

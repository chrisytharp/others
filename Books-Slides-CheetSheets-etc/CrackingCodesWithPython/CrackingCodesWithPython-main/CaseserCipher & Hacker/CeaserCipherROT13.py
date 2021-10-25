#Caeser Cipher

import pyperclip

# The string to be encrypted/decrypted:

message = input("enter in text: \n")
#message = "this is a rot13 encryption of the message"

# This is the encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts
mode = "encrypt"        #set to either 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted: ?can i use regex?
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# store the encrypted/ decrypted form of message:
translated =""

for symbol in message:
    #NOTE: only symbol in the SYMBOLS string can be encrypted\decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #perform encryption/decryption
        if mode == "encrypt":
            translatedIndex = symbolIndex + key
        elif mode == "decrypt":
            translatedIndex = symbolIndex - key

        # Handles wrap around (if needed):
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #Append the symbol without encrypting/ decrypting
        translated = translated + symbol

# Output the translated string
print(translated)
pyperclip.copy(translated)

# Transposition Cipher Hacker

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    myMessage = input("""enter in transposition cipher text and press ENTER:\n>  """)

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print("failed to hack encryption...")
    else:
        print("copy hacked message to clipboard:")
        print("hacked message")
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print("hacking...")

    #Python programs can be stopped anytime by pressin Ctrl+C (Windows) Ctrl+D (*nix & Mac)
    print("press Ctrl+C (on Windows) or Ctrl+D (on Mac and Linux) to QUIT anytime")

    # Breute-Forcing by looping through every possible key:
    for key in range(1, len(message)):
        print("Trying key #%s..." % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            #ask user if this is the correct decryption:
            print()
            print("Possible encryption hack:")
            print("Key %s: %s" % (key, decryptedText[: 100]))
            print()
            print("Enter D if done, anything else to continue hacking:")
            respone = input("> ")

            if respone.strip().upper().startswith("D"):
                return decryptedText

    return None

if __name__ == "__main__":
    main()

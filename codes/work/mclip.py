#! python3
#mclip.py - A multi-clipboard program
#stores multiple phrases to paste in repetitive tasks

TEXT = {'agree': """yes, i agree. That sounds good to me!""",
        'busy': """Sorry, can we do this later in the week or next week""",
        'upsell': """ Would you consider making this a monthly donation?"""}

import sys, pyperclip

if len(sys.argv) <2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    #print(sys.argv[0])
    #1st argument(indexes to b zero) is the python script
    sys.exit()

#first command line arg (indexed at second position 1, in zero based indexed) is the keyphrase
keyphrase = sys.argv[1]
#could use sys.argv[1] everytime but storing it as keyphrase makes it easier to use in program

#now if keyphrase (aka ARG 2) matches any of the keys in the dictionary, you want to copy the keys' value with pyperclip.copy()
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for" + keyphrase + "copied to clipboard")
else:
    print("there is no text for" + keyphrase)

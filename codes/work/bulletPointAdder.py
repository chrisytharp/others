#paste text from clipboard, do something to it & copy the new text to clipboard

#! python3
#this script adds wikipedia bullet points to the start of ea line of text on the clipboard

import pyperclip

text = pyperclip.paste()

#could write a program that searches for all \n char's but will be easier to use split()
#seperate lines and add stars

#take in 'text' var and find '\n' char' and split them
lines = text.split('\n')

for i in range(len(lines)):        #loop through all indexes in the "line" list
    lines[i] = '*' + lines[i]        #add a star to each string in "lines list"

#.copy() is expecting a single string value NOT a list of string values
#to make this list a single string value we use .join() to get single string
newText = '\n'.join(lines)
pyperclip.copy(newText)

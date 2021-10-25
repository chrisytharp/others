text = input()

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    print(text + " is a phone number")

print(isPhoneNumber(text))


for in range(len(text)):
    chunk = text[i:i+12]         #on each iteration of the for loop a new chunk of 12 chars from text is assigne to the chunk var. EX on 1st iteration i=0 and text[0:12] 
    if isPhoneNumber(chunk):     # NEXT iteration i=1 and chunk is assigned text[1:13]  THEN IS PASSED to function to see if its a phone number
        print('found phone number' + chunk)

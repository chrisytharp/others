import re

phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}')  # create REGEX onject

x = input("enter chars and a phone # \n")

y = phoneNum.search(x)  # use search() to find regex obj in string

if phoneNum.search(x) == None:
    print("number not found")
else:
    print(y.group())            # IF regex object is found search() returns a matched Object
                            #that the group() method returns the match text

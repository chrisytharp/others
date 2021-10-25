
"""
age = input("what's your age?")
print(type(age))

age = int(age)
print(type(age))

print(age)
"""
"""
spam = 0

if spam < 5:
    spam = spam + 1
    print(spam)

print(spam)
"""
"""
name = ""

while name != "your name":
    name = input("please type your name")
print("thank you")
"""
"""
while True:
    print("who are you?")
    name = input()
    if name != "chris":
        continue
    print("hello chris, what is your password?")
    password = input()
    if password == "password":
        break
print("welcome")
"""
"""
total = 0

for num in range(101):
    print(num)
    #num is the counter var in the for loop
    total = total + num
    print(total)
print(total)
"""
"""
text = "this is a readable string"
#this will print the text in reverse order
print(text[::-1])
"""
"""
import random

for i in range(5):
    print(random.randint(1,10))
"""
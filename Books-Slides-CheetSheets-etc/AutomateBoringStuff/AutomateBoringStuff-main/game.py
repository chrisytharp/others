#This is a guess the number game
import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

#Ask the player for to guess a number 6 times
for guessesTaken in range(1,7):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break               #this is ran if the guess is right

if guess == secretNumber:
    print("Good Job, my number was " + str(secretNumber) + " , you guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope, the number i was thinkg was " + str(secretNumber) + " sorry")
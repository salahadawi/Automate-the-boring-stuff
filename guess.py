#! /usr/bin/python3

import random
import sys
print("I'm thinking of a number between 1 and 20.")
randomNum = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess:")
    try:
        guess = int(input())
    except:
        print("That is not a number!")
        continue
    if guess == randomNum:
        print("That is correct!")
        sys.exit()
    elif guess < randomNum:
        print("Your guess is too low.")
    elif guess > randomNum:
        print("Your guess is too high.")
print("You've guessed incorrect too many times.")
print("I was thinking of " + str(randomNum))
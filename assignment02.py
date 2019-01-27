"""
Michael Ribaudo CIS156 5:20 Tue

Second Program: Guess a Number using if/else and while

This program generates a random variable within the range 1 to 100. This sets the game's winning value.
It then sets a starting value for the number of tries the player begins the game with and reduces each
time the player enters a number that isn't the winning value. There is also a counter that increments each time the
player enters a number that isn't the winning value as long as they are not out of tries. The player is then asked to
guess a number, with error checking for non-numeric values. If the player guesses the randomly generated value then
a congratulations message is printed and the loop breaks. If the player does not guess correctly, the number of tries
decreases with each incorrect guess until zero at which point a lost message is printed and the loop breaks.
"""

import random

magic_number = random.randint(1,100)

tries = 7
counter = 0

print("Guess a number from 1 to 100. ")

# print(magic_number)

while True:
    try:
        user_input = int(input("You have {0} tries left:".format(tries)))
    except (ValueError, TypeError):
        print("Not an Integer! Try again.")
    else:
        if user_input != magic_number:
            counter += 1
            tries -= 1
        if tries > 0 and user_input < magic_number:
            print("You are too low. Try again.")
        elif tries > 0 and user_input > magic_number:
            print("You are too high. Try again.")
        elif tries == 0:
            print("You are out of tries and have lost")
            break
        elif user_input == magic_number:
            #tries = 0
            print("Congratulations! You won in {0} tries!".format(counter + 1))
            break

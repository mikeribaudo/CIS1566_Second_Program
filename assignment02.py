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

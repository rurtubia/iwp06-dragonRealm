import random
import time

world_number = 1
validInput = False

# Starts the game
def gameintro():
    print("Welcome to the world of dragons.")
    time.sleep(.5)
    print("Can you survive the five worlds and get home without being killed by the dragons?")
    time.sleep(.5)
    print("You will select one out of three caves each time and either:")
    print("Find food to help you level up")
    print("or")
    print("Fight a dragon, if your level is higher than the dragon's, you survive...")
    print("... if the dragon's level is higher than yours... you will die!")


# Calls the main functions in the game, in order.
def gameloop():
    time.sleep(.5)
    print("welcome to World number", world_number)
    time.sleep(.3)
    caveChoose()


# Lets the player choose a cave
def caveChoose():
    print("choose a cave: 1 or 2")
    foodCave = random.randint(1, 2)
    while validateInput() == -1:
        chosenCave = validateInput()
    print('Your choice is', str(chosenCave))
        # continuar


def validateInput():
    try:
        print("Write either 1 or 2")
        one_or_two = input()
        one_or_two = int(one_or_two)
        if not ((one_or_two == 1) or (one_or_two == 2)):
            print('Error: Write only either \'1\' or \'2\'')
            return -1
        else:
            return one_or_two
    except ValueError:
        print("Write only either '1' or '2'")
        return -1

# validateInput()
caveChoose()

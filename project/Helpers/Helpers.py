import sys
import random
import os
import platform
from project import Hero


# Starts character creator
def start_creator():
    while True:
        try:
            start_creator_input = input("Would you like to get started? y/n \n"
                                        "> ")
            start_response = start_creator_input.lower()
            if start_response == "y":
                random_or_make_input = input("Do you want a random character or do you want to create one? "
                                             "random/create \n"
                                             "> ")
                if random_or_make_input.lower() == "random":
                    Hero.create_random_character()
                    sys.exit()
                if random_or_make_input.lower() == "create":
                    break
                else:
                    print("Invalid Response")
                    continue
            if start_response == "n":
                print("Maybe next time.")
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid Answer. y/n only.")
            continue


# Dice roll simulator
def dice_roll(min_num, max_num):
    int(min_num)
    int(max_num)
    return random.randint(min_num, max_num)


# Clears console after asking questions
def _clear_console():
    operating_system_clear = ''
    if platform.system() == 'Windows':
        operating_system_clear = 'cls'
    elif platform.system() == 'Linux':
        operating_system_clear = 'clear'
    clear = lambda: os.system(operating_system_clear)
    clear()

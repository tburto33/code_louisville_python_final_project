# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
import sys
import Races
import Class
import Stats


def start_creator():
    while True:
        try:
            start = input("Would you like to get started? y/n \n"
                          "> ")
            start_response = start.lower()
            if start_response == "y":
                break
            if start_response == "n":
                print("Maybe next time.")
                sys.exit()
            else:
                raise TypeError
        except TypeError:
            print("Invalid Answer. y/n only.")
            continue


def select_sex():
    while True:
        try:
            sex_selection = input("Would you like a male or female character? \n"
                                  "> ")
            sex_selection_input = sex_selection.lower()
            if sex_selection_input == "male" or sex_selection_input == "female":
                return sex_selection
            else:
                raise TypeError
        except TypeError:
            print("Invalid Answer: Type male or female only.")
            continue


def name_character():
    while True:
        try:
            char_name = input("What do you want to name your character? \n"
                              "> ")
            validate_char_name = input("Are you sure you want to name your character {}? y/n \n"
                                       "> ".format(char_name))
            if validate_char_name.lower() == "y":
                return char_name
            elif validate_char_name.lower() == "n":
                print("No problem, let's try another name.")
                continue
            else:
                raise TypeError
        except TypeError:
            print("Invalid response, y/n only.")
            continue


def select_race():
    while True:
        try:
            print("--------------")
            print("RACE SELECTION")
            print("--------------")
            print("\n".join(Races.char_race))

            choose_race = input("What race would you like to be? \n"
                                "> ")
            if choose_race.lower() in Races.races:
                print(Races.races[choose_race.lower()])
                validate_race_selection(choose_race)
                break
            else:
                raise TypeError
        except TypeError:
            print("Invalid Response, check spelling and try again.")
            continue


def validate_race_selection(chosen_race):
    while True:
        try:
            verify_race = input("Is {} the race you want to be? y/n \n"
                                "> ".format(chosen_race))
            if verify_race.lower() == "y":
                return chosen_race.upper()
            elif verify_race.lower() == "n":
                print("Let's find you another race.")
                select_race()
                break
            else:
                raise TypeError
        except TypeError:
            print("Invalid Response, y/n only")
            continue

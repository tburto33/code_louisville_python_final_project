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


def select_character_sex():
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
            validate_char_name = input(f"Are you sure you want to name your character {char_name}? y/n \n"
                                       "> ")
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


def select_character_race():
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
                verify_race = input(f"Is {choose_race} the race you want to be? y/n \n"
                                    f"> ")
                if verify_race.lower() == "y":
                    return choose_race
                elif verify_race.lower() == "n":
                    print("Let's find you another race.")
                    continue
                else:
                    raise TypeError
            else:
                raise TypeError
        except TypeError:
            print("Invalid Response.")
            continue


def select_character_clss():
    while True:
        try:
            print("---------------")
            print("CLASS SELECTION")
            print("---------------")
            print("\n".join(Class.char_class))

            choose_clss = input("What class would you like to play? \n"
                                "> ")
            if choose_clss.lower() in Class.classes:
                print(Class.classes[choose_clss.lower()])
                verify_clss = input(f"Is {choose_clss} the class you want to play? y/n \n"
                                    f"> ")
                if verify_clss.lower() == "y":
                    return choose_clss
                elif verify_clss.lower() == "n":
                    print("Let's find you another class.")
                    continue
                else:
                    raise TypeError
            else:
                raise TypeError
        except TypeError:
            print("Invalid Response")
            continue


def character_ablility_rolls(char_race):
    strength_roll = Stats.strength(char_race)
    dexterity_roll = Stats.dexterity(char_race)
    constitution_roll = Stats.constitution(char_race)
    intelligence_roll = Stats.intelligence(char_race)
    wisdom_roll = Stats.wisdom(char_race)
    charisma_roll = Stats.charisma(char_race)

    return strength_roll, dexterity_roll, constitution_roll, intelligence_roll, wisdom_roll, charisma_roll

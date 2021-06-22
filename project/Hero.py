from project.Data import CharClass, CharRaces


class Character:
    def __init__(self, sex, name, race, clss, hp):
        self.sex = sex
        self.name = name
        self.race = race
        self.clss = clss
        self.hp = hp

    def print_character(self):
        print(f"""
    Name: {self.name}
    Sex: {self.sex}
    Race: {self.race}
    Class: {self.clss}
    Starting HP: {self.hp}
    """)


# accepts/validates user input for sex
def select_character_sex():
    while True:
        try:
            sex_selection_input = input("Would you like a male or female character? \n"
                                        "> ")
            sex_selection_input = sex_selection_input.lower()
            if sex_selection_input == "male" or sex_selection_input == "female":
                return sex_selection_input
            else:
                raise ValueError
        except ValueError:
            print("Invalid Answer: Type male or female only.")
            continue


# accepts/validates user input for name
def select_character_name():
    while True:
        try:
            char_name_input = input("What do you want to name your character? \n"
                                    "> ")
            validate_char_name_input = input(f"Are you sure you want to name your character {char_name_input}? y/n \n"
                                             "> ")
            if validate_char_name_input.lower() == "y":
                return char_name_input
            elif validate_char_name_input.lower() == "n":
                print("No problem, let's try another name.")
                continue
            else:
                raise ValueError
        except ValueError:
            print("Invalid response, y/n only.")
            continue


# Lists races to pick from, lists description of race, accepts/validates user input
def select_character_race():
    while True:
        try:
            print("--------------")
            print("RACE SELECTION")
            print("--------------")
            print("\n".join(CharRaces.char_race))

            select_race_input = input("What race would you like to be? \n"
                                      "> ")
            if select_race_input.lower() in CharRaces.races:
                print(CharRaces.races[select_race_input.lower()])
                verify_race_input = input(f"Is {select_race_input} the race you want to be? y/n \n"
                                          f"> ")
                if verify_race_input.lower() == "y":
                    return select_race_input
                elif verify_race_input.lower() == "n":
                    print("Let's find you another race.")
                    continue
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Invalid Response.")
            continue


# Lists classes to pick from, lists description of class, accepts/validates user input
def select_character_clss():
    while True:
        try:
            print("---------------")
            print("CLASS SELECTION")
            print("---------------")
            print("\n".join(CharClass.char_class))

            selected_clss_input = input("What class would you like to play? \n"
                                        "> ")
            if selected_clss_input.lower() in CharClass.classes:
                print(CharClass.classes[selected_clss_input.lower()])
                verify_clss_input = input(f"Is {selected_clss_input} the class you want to play? y/n \n"
                                          f"> ")
                if verify_clss_input.lower() == "y":
                    return selected_clss_input
                elif verify_clss_input.lower() == "n":
                    print("Let's find you another class.")
                    continue
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Invalid Response")
            continue

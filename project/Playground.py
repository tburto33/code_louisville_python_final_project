# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
import sys


class Questions:

    def start_creator(self):
        while True:
            try:
                start = input("Would you like to get started? y/n \n"
                              "> ")
                self = start.lower()
                if self == "y":
                    break
                if self == "n":
                    print("Maybe next time.")
                    sys.exit()
                else:
                    raise err
            except TypeError as err:
                print("Invalid answer")
                continue


class CharacterSex:

    @classmethod
    def select_sex(cls):
        while True:
            try:
                sex_selection = input("Would you like a male or female character? \n"
                                      "> ")
                if sex_selection.lower() == "male" or sex_selection.lower() == "female":
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid Answer: Type male or female only.")
                continue
        return sex_selection


questions = Questions()
char_sex = CharacterSex()

questions.start_creator()
selected_sex = char_sex.select_sex()
print("You have chosen a {} character.".format(selected_sex))

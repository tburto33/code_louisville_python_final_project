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
                if self.lower() == "y":
                    break
                if self.lower() == "n":
                    print("Maybe next time.")
                    sys.exit()
                else:
                    raise TypeError
            except TypeError:
                print("Invalid answer")
                continue

    def character_sex(self):
        while True:
            try:
                sex = input("Would you like a male or female character? \n"
                            "> ")
                self = sex.lower()
                if self == "male" or self == "female":
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid Answer. Type male or female only.")
                continue


question = Questions()
question.start_creator()
question.character_sex()
print("You have chosen a {} character".format(question.character_sex()))

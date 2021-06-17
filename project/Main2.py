import Playground
import Races
import os

print("Welcome to my DnD Character Generator!")
Playground.start_creator()
char_sex = Playground.select_sex()
char_name = Playground.name_character()
char_race = Playground.select_race()
print("You are playing a {} character, named {}. They are a {}!".format(char_sex, char_name, char_race))

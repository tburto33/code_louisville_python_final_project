import Playground
import Races
import os

print("Welcome to my DnD Character Generator!")
Playground.start_creator()
char_sex = Playground.select_character_sex()
char_name = Playground.name_character()
char_race = Playground.select_character_race()
char_clss = Playground.select_character_clss()
ability_roll = Playground.character_ablility_rolls(char_race.lower())

print(f"You are playing a {char_sex} character, named {char_name}. They are a {char_race} {char_clss}!")
print(Playground.char_ability_dict)
print(Playground.char_modifier_dict)
Playground.print_abilities_and_skills()
print("Your starting hp is {}.".format(Playground.starting_hp(char_clss)))

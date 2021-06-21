import Playground
import Races
import os

print("Welcome to my DnD Character Generator!")
Playground.start_creator()
char_sex = Playground.select_sex()
char_name = Playground.name_character()
char_race = Playground.select_race()
char_clss = Playground.select_clss()

print(f"You are playing a {char_sex} character, named {char_name}. They are a {char_race} {char_clss}!")

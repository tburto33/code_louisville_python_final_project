import stats
import character
from project.Helpers import helpers

print("Welcome to my DnD Character Generator!")
helpers.start_creator()
char_sex = character.select_character_sex()
char_name = character.select_character_name()
char_race = character.select_character_race()
char_clss = character.select_character_clss()
stats.set_ability_rolls(char_clss)
stats.set_ability_modifiers()
if char_race == "half-elf":
    stats.half_elf_racial()
char_hp = stats.set_starting_hp(char_clss)
user_char = character.Character(char_sex.upper(),
                                char_name.upper(),
                                char_race.upper(),
                                char_clss.upper(),
                                char_hp)
user_char.print_character()
stats.print_abilities_and_mods()
stats.print_skills()

# race = character.select_character_race()
# clss = "barbarian"
# stats.set_ability_rolls(clss)
# stats.character_modifiers()
# print(stats.char_abilities)
# print(stats.char_modifiers)
# if race.lower() == "half-elf":
#     stats.half_elf_racial()
#     stats.character_modifiers()
# print(stats.char_abilities)
# print(stats.char_modifiers)
# print("HP: {}".format(stats.set_starting_hp(clss)))
# helpers.start_creator()
# char_sex = character.select_character_sex()
# char_name = character.select_character_name()
# char_race = character.select_character_race()
# char_clss = character.select_character_clss()
# stats.character_ability_rolls(char_clss)
# stats.character_modifiers()
# char_hp = stats.starting_hp(char_clss)
# user_char = character.Character(char_sex.upper(),
#                                 char_name.upper(),
#                                 char_race.upper(),
#                                 char_clss.upper(),
#                                 char_hp)
# user_char.print_character()
# stats.print_abilities_and_mods()
# stats.print_skills()

# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
from project import character
from project.Data import char_races, char_class
import random
from project import stats


def create_random_character():
    char_name = character.select_character_name()
    sexes = ["male", "female"]
    char_sex = random.choice(sexes)
    char_race = random.choice(char_races.char_race)
    char_clss = random.choice(char_class.char_class)
    stats.character_ability_rolls(char_clss)
    stats.set_ability_modifiers()
    char_hp = stats.starting_hp(char_clss)
    random_char = character.Character(char_sex.upper(),
                                      char_name.upper(),
                                      char_race.upper(),
                                      char_clss.upper(),
                                      char_hp)
    random_char.print_character()
    stats.print_abilities_and_mods()
    stats.print_skills()


# Calculates starting HP based on class and constitution modifier
# def starting_hp(char_class):
#     cons_mod = char_modifier_dict["cons_mod"]
#     hit_points = None
#
#     if char_class.lower() == "barbarian":
#         hit_points = 12
#     if char_class.lower() == "fighter" or char_class == "paladin" or char_class == "ranger":
#         hit_points = 10
#     if char_class.lower() == "bard" or char_class == "cleric" or char_class == "druid" or char_class == "monk" or char_class == "rogue" or char_class == "warlock":
#         hit_points = 8
#     if char_class.lower() == "sorcerer" or char_class == "wizard":
#         hit_points = 6
#     return hit_points + cons_mod


# def character_ability_rolls(char_race):
#     # Calculates ability rolls with racial passives
#     strength_roll = strength(char_race)
#     dexterity_roll = dexterity(char_race)
#     constitution_roll = constitution(char_race)
#     intelligence_roll = intelligence(char_race)
#     wisdom_roll = wisdom(char_race)
#     charisma_roll = charisma(char_race)
#     # Stores ability rolls into char_ability_dict
#     char_ability_dict.update({"str": strength_roll})
#     char_ability_dict.update({"dex": dexterity_roll})
#     char_ability_dict.update({"cons": constitution_roll})
#     char_ability_dict.update({"int": intelligence_roll})
#     char_ability_dict.update({"wis": wisdom_roll})
#     char_ability_dict.update({"char": charisma_roll})

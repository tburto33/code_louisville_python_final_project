# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
from project import Hero
from project.Data import CharRaces, CharClass
import random
from project import Stats


def create_random_character():
    char_name = Hero.select_character_name()
    sexes = ["male", "female"]
    char_sex = random.choice(sexes)
    char_race = random.choice(CharRaces.char_race)
    char_clss = random.choice(CharClass.char_class)
    Stats.character_ability_rolls(char_clss)
    Stats.character_modifiers()
    char_hp = Stats.starting_hp(char_clss)
    random_char = Hero.Character(char_sex.upper(),
                                 char_name.upper(),
                                 char_race.upper(),
                                 char_clss.upper(),
                                 char_hp)
    random_char.print_character()
    Stats.print_abilities_and_mods()
    Stats.print_skills()

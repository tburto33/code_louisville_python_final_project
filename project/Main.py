import Stats
import Hero
from project.Helpers import Helpers

print("Welcome to my DnD Character Generator!")
Helpers.start_creator()
char_sex = Hero.select_character_sex()
char_name = Hero.select_character_name()
char_race = Hero.select_character_race()
char_clss = Hero.select_character_clss()
Stats.character_ability_rolls(char_clss)
Stats.character_modifiers()
char_hp = Stats.starting_hp(char_clss)
user_char = Hero.Character(char_sex.upper(),
                           char_name.upper(),
                           char_race.upper(),
                           char_clss.upper(),
                           char_hp)
user_char.print_character()
Stats.print_abilities_and_mods()
Stats.print_skills()

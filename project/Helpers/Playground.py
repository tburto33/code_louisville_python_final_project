# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
from project.Data import CharRaces, CharClass
# import Stats


# class Character:
#     def __init__(self, sex, name, race, clss):
#         self.sex = sex
#         self.name = name
#         self.race = race
#         self.clss = clss
#
#     def print_character(self):
#         print(f"""
#         Name: {self.name}
#         Sex: {self.sex}
#         Race: {self.race}
#         Class: {self.clss}
#         """)
#
#
# def select_character_sex():
#     while True:
#         try:
#             sex_selection_input = input("Would you like a male or female character? \n"
#                                         "> ")
#             sex_selection_input = sex_selection_input.lower()
#             if sex_selection_input == "male" or sex_selection_input == "female":
#                 return sex_selection_input
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Invalid Answer: Type male or female only.")
#             continue
#
#
# def select_character_name():
#     while True:
#         try:
#             char_name_input = input("What do you want to name your character? \n"
#                                     "> ")
#             validate_char_name_input = input(f"Are you sure you want to name your character {char_name_input}? y/n \n"
#                                              "> ")
#             if validate_char_name_input.lower() == "y":
#                 return char_name_input
#             elif validate_char_name_input.lower() == "n":
#                 print("No problem, let's try another name.")
#                 continue
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Invalid response, y/n only.")
#             continue
#
#
# def select_character_race():
#     while True:
#         try:
#             print("--------------")
#             print("RACE SELECTION")
#             print("--------------")
#             print("\n".join(Races.char_race))
#
#             select_race_input = input("What race would you like to be? \n"
#                                       "> ")
#             if select_race_input.lower() in Races.races:
#                 print(Races.races[select_race_input.lower()])
#                 verify_race_input = input(f"Is {select_race_input} the race you want to be? y/n \n"
#                                           f"> ")
#                 if verify_race_input.lower() == "y":
#                     return select_race_input
#                 elif verify_race_input.lower() == "n":
#                     print("Let's find you another race.")
#                     continue
#                 else:
#                     raise ValueError
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Invalid Response.")
#             continue
#
#
# def select_character_clss():
#     while True:
#         try:
#             print("---------------")
#             print("CLASS SELECTION")
#             print("---------------")
#             print("\n".join(Class.char_class))
#
#             selected_clss_input = input("What class would you like to play? \n"
#                                         "> ")
#             if selected_clss_input.lower() in Class.classes:
#                 print(Class.classes[selected_clss_input.lower()])
#                 verify_clss_input = input(f"Is {selected_clss_input} the class you want to play? y/n \n"
#                                           f"> ")
#                 if verify_clss_input.lower() == "y":
#                     return selected_clss_input
#                 elif verify_clss_input.lower() == "n":
#                     print("Let's find you another class.")
#                     continue
#                 else:
#                     raise ValueError
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Invalid Response")
#             continue


# def character_ablility_rolls(char_race):
#     # Calculates ability rolls with racial passives
#     strength_roll = Stats.strength(char_race)
#     dexterity_roll = Stats.dexterity(char_race)
#     constitution_roll = Stats.constitution(char_race)
#     intelligence_roll = Stats.intelligence(char_race)
#     wisdom_roll = Stats.wisdom(char_race)
#     charisma_roll = Stats.charisma(char_race)
#     # Stores ability rolls into char_ability_dict
#     char_ability_dict.update({"str": strength_roll})
#     char_ability_dict.update({"dex": dexterity_roll})
#     char_ability_dict.update({"cons": constitution_roll})
#     char_ability_dict.update({"int": intelligence_roll})
#     char_ability_dict.update({"wis": wisdom_roll})
#     char_ability_dict.update({"char": charisma_roll})
#
#
# def character_modifiers():
#     # Calculates modifiers and then stores them into char_modifier_dict
#     char_modifier_dict.update({"str_mod": ability_modifier(char_ability_dict["str"])})
#     char_modifier_dict.update({"dex_mod": ability_modifier(char_ability_dict["dex"])})
#     char_modifier_dict.update({"cons_mod": ability_modifier(char_ability_dict["cons"])})
#     char_modifier_dict.update({"int_mod": ability_modifier(char_ability_dict["int"])})
#     char_modifier_dict.update({"wis_mod": ability_modifier(char_ability_dict["wis"])})
#     char_modifier_dict.update({"char_mod": ability_modifier(char_ability_dict["char"])})


# def starting_hp(char_class):
#     cons_mod = char_modifier_dict["cons_mod"]
#     hit_points = 0
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


# def ability_modifier(ability):
#     modifier = 0
#
#     if ability == 1:
#         modifier = -5
#     if ability == 2 or ability == 3:
#         modifier = -4
#     if ability == 4 or ability == 5:
#         modifier = -3
#     if ability == 6 or ability == 7:
#         modifier = -2
#     if ability == 8 or ability == 9:
#         modifier = -1
#     if ability == 10 or ability == 11:
#         modifier = 0
#     if ability == 12 or ability == 13:
#         modifier = 1
#     if ability == 14 or ability == 15:
#         modifier = 2
#     if ability == 16 or ability == 17:
#         modifier = 3
#     if ability == 18 or ability == 19:
#         modifier = 4
#     if ability == 20:
#         modifier = 5
#     return modifier


# char_ability_dict = {
#     "str": 0,
#     "dex": 0,
#     "cons": 0,
#     "int": 0,
#     "wis": 0,
#     "char": 0,
# }
#
# char_modifier_dict = {
#     "str_mod": 0,
#     "dex_mod": 0,
#     "cons_mod": 0,
#     "int_mod": 0,
#     "wis_mod": 0,
#     "char_mod": 0,
# }


# def print_abilities_and_mods():
#     print(f"""
#     Strength: {char_ability_dict["str"]}  Mod = {char_modifier_dict["str_mod"]}
#     Dexterity: {char_ability_dict["dex"]}  Mod = {char_modifier_dict["dex_mod"]}
#     Constitution: {char_ability_dict["cons"]}  Mod = {char_modifier_dict["cons_mod"]}
#     Intelligence: {char_ability_dict["int"]}  Mod = {char_modifier_dict["int_mod"]}
#     Wisdom: {char_ability_dict["wis"]}  Mod = {char_modifier_dict["wis_mod"]}
#     Charisma: {char_ability_dict["char"]}  Mod = {char_modifier_dict["char_mod"]}
#     """)
#
#
# def print_skills():
#     print(f"""
#     Your character has the following skill stats:
#
#     Acrobatics: {char_modifier_dict["dex_mod"]}
#     Animal Handling: {char_modifier_dict["wis_mod"]}
#     Arcana: {char_modifier_dict["int_mod"]}
#     Athletics: {char_modifier_dict["str_mod"]}
#     Deception: {char_modifier_dict["char_mod"]}
#     History: {char_modifier_dict["int_mod"]}
#     Insight: {char_modifier_dict["wis_mod"]}
#     Intimidation: {char_modifier_dict["char_mod"]}
#     Investigation: {char_modifier_dict["int_mod"]}
#     Medicine: {char_modifier_dict["wis_mod"]}
#     Nature: {char_modifier_dict["int_mod"]}
#     Perception: {char_modifier_dict["wis_mod"]}
#     Performance: {char_modifier_dict["char_mod"]}
#     Persuasion: {char_modifier_dict["char_mod"]}
#     Religion: {char_modifier_dict["int_mod"]}
#     Sleight of Hand: {char_modifier_dict["dex_mod"]}
#     Stealth: {char_modifier_dict["dex_mod"]}
#     Survival: {char_modifier_dict["wis_mod"]}
#     """)

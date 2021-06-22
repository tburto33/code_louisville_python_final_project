from project.Helpers import Helpers

helpers = Helpers


# Calculates abilities before passives
def ability_roll():
    total = []
    # Simulates rolling 4 1d6 dice
    roll_one = helpers.dice_roll(1, 6)
    roll_two = helpers.dice_roll(1, 6)
    roll_three = helpers.dice_roll(1, 6)
    roll_four = helpers.dice_roll(1, 6)
    # Places 4 rolls in list and removes lowest before totaling
    total.append(roll_one)
    total.append(roll_two)
    total.append(roll_three)
    total.append(roll_four)
    total.remove(min(total))

    return sum(total)


# Determines modifiers based on ability rolls
def ability_modifier(ability):
    modifier = 0

    if ability == 1:
        modifier = -5
    if ability == 2 or ability == 3:
        modifier = -4
    if ability == 4 or ability == 5:
        modifier = -3
    if ability == 6 or ability == 7:
        modifier = -2
    if ability == 8 or ability == 9:
        modifier = -1
    if ability == 10 or ability == 11:
        modifier = 0
    if ability == 12 or ability == 13:
        modifier = 1
    if ability == 14 or ability == 15:
        modifier = 2
    if ability == 16 or ability == 17:
        modifier = 3
    if ability == 18 or ability == 19:
        modifier = 4
    if ability == 20:
        modifier = 5
    return modifier


def character_ability_rolls(char_race):
    # Calculates ability rolls with racial passives
    strength_roll = strength(char_race)
    dexterity_roll = dexterity(char_race)
    constitution_roll = constitution(char_race)
    intelligence_roll = intelligence(char_race)
    wisdom_roll = wisdom(char_race)
    charisma_roll = charisma(char_race)
    # Stores ability rolls into char_ability_dict
    char_ability_dict.update({"str": strength_roll})
    char_ability_dict.update({"dex": dexterity_roll})
    char_ability_dict.update({"cons": constitution_roll})
    char_ability_dict.update({"int": intelligence_roll})
    char_ability_dict.update({"wis": wisdom_roll})
    char_ability_dict.update({"char": charisma_roll})


def character_modifiers():
    # Calculates modifiers from ability rolls and then stores them into char_modifier_dict
    char_modifier_dict.update({"str_mod": ability_modifier(char_ability_dict["str"])})
    char_modifier_dict.update({"dex_mod": ability_modifier(char_ability_dict["dex"])})
    char_modifier_dict.update({"cons_mod": ability_modifier(char_ability_dict["cons"])})
    char_modifier_dict.update({"int_mod": ability_modifier(char_ability_dict["int"])})
    char_modifier_dict.update({"wis_mod": ability_modifier(char_ability_dict["wis"])})
    char_modifier_dict.update({"char_mod": ability_modifier(char_ability_dict["char"])})


# Stores character ability rolls
char_ability_dict = {
    "str": 0,
    "dex": 0,
    "cons": 0,
    "int": 0,
    "wis": 0,
    "char": 0,
}

# Stores character modifiers
char_modifier_dict = {
    "str_mod": 0,
    "dex_mod": 0,
    "cons_mod": 0,
    "int_mod": 0,
    "wis_mod": 0,
    "char_mod": 0,
}


# Calculates starting HP based on class and constitution modifier
def starting_hp(char_class):
    cons_mod = char_modifier_dict["cons_mod"]
    hit_points = 0

    if char_class.lower() == "barbarian":
        hit_points = 12
    if char_class.lower() == "fighter" or char_class == "paladin" or char_class == "ranger":
        hit_points = 10
    if char_class.lower() == "bard" or char_class == "cleric" or char_class == "druid" or char_class == "monk" or char_class == "rogue" or char_class == "warlock":
        hit_points = 8
    if char_class.lower() == "sorcerer" or char_class == "wizard":
        hit_points = 6
    return hit_points + cons_mod


# The following functions add racial passives into ability rolls
def strength(race):
    if race == "dragonborn" or race == "half-orc":
        str_total = ability_roll() + 2
    elif race == "human":
        str_total = ability_roll() + 1
    else:
        str_total = ability_roll()
    return str_total


def dexterity(race):
    if race == "elf" or race == "human" or race == "halfling":
        dex_total = ability_roll() + 2
    elif race == "human":
        dex_total = ability_roll() + 1
    else:
        dex_total = ability_roll()
    return dex_total


def constitution(race):
    if race == "dwarf":
        cons_total = ability_roll() + 2
    elif race == "human" or race == "half-orc":
        cons_total = ability_roll() + 1
    else:
        cons_total = ability_roll()
    return cons_total


def intelligence(race):
    if race == "gnome":
        int_total = ability_roll() + 2
    elif race == "human" or race == "tiefling":
        int_total = ability_roll() + 1
    else:
        int_total = ability_roll()
    return int_total


def wisdom(race):
    if race == "human":
        wis_total = ability_roll() + 1
    else:
        wis_total = ability_roll()
    return wis_total


def charisma(race):
    if race == "half-elf" or race == "tiefling":
        char_total = ability_roll() + 2
    elif race == "human" or race == "dragonborn":
        char_total = ability_roll() + 1
    else:
        char_total = ability_roll()
    return char_total


# Prints ability and modifiers to console
def print_abilities_and_mods():
    print(f""" Your character has the following abilities:
    
    Strength: {char_ability_dict["str"]}  Mod = {char_modifier_dict["str_mod"]}
    Dexterity: {char_ability_dict["dex"]}  Mod = {char_modifier_dict["dex_mod"]}
    Constitution: {char_ability_dict["cons"]}  Mod = {char_modifier_dict["cons_mod"]}
    Intelligence: {char_ability_dict["int"]}  Mod = {char_modifier_dict["int_mod"]}
    Wisdom: {char_ability_dict["wis"]}  Mod = {char_modifier_dict["wis_mod"]}
    Charisma: {char_ability_dict["char"]}  Mod = {char_modifier_dict["char_mod"]}
    """)


# Prints skills list to console
def print_skills():
    print(f""" Your character has the following skills:

    Acrobatics: {char_modifier_dict["dex_mod"]}
    Animal Handling: {char_modifier_dict["wis_mod"]}
    Arcana: {char_modifier_dict["int_mod"]}
    Athletics: {char_modifier_dict["str_mod"]}
    Deception: {char_modifier_dict["char_mod"]}
    History: {char_modifier_dict["int_mod"]}
    Insight: {char_modifier_dict["wis_mod"]}
    Intimidation: {char_modifier_dict["char_mod"]}
    Investigation: {char_modifier_dict["int_mod"]}
    Medicine: {char_modifier_dict["wis_mod"]}
    Nature: {char_modifier_dict["int_mod"]}
    Perception: {char_modifier_dict["wis_mod"]}
    Performance: {char_modifier_dict["char_mod"]}
    Persuasion: {char_modifier_dict["char_mod"]}
    Religion: {char_modifier_dict["int_mod"]}
    Sleight of Hand: {char_modifier_dict["dex_mod"]}
    Stealth: {char_modifier_dict["dex_mod"]}
    Survival: {char_modifier_dict["wis_mod"]}    
    """)

# Selecting two abilities for Half-Elf racial passive
# def half_elf_racial_ability():
#     half_elf_ability_one = input("Pick first ability for +1: \n"
#                                  "Strength, Dexterity, Constitution, Intelligence, Wisdom, or Charisma \n"
#                                  "> ")
#     half_elf_ability_two = input("Pick second ability for +1: \n"
#                                  "Strength, Dexterity, Constitution, Intelligence, Wisdom, or Charisma \n"
#                                  "> ")
#     if half_elf_ability_one.lower() == "strength" or half_elf_ability_two.lower() == "strength":
#         new_ability_score = Main.strength_roll + 1
#     if half_elf_ability_one.lower() == "dexterity" or half_elf_ability_two.lower() == "dexterity":
#         new_ability_score = Main.dexterity_roll + 1
#     if half_elf_ability_one.lower() == "constitution" or half_elf_ability_two.lower() == "constitution":
#         new_ability_score = Main.constitution_roll + 1
#     if half_elf_ability_one.lower() == "intelligence" or half_elf_ability_two.lower() == "intelligence":
#         new_ability_score = Main.intelligence_roll + 1
#     if half_elf_ability_one.lower() == "wisdom" or half_elf_ability_two.lower() == "wisdom":
#         new_ability_score = Main.wisdom_roll + 1
#     if half_elf_ability_one.lower() == "charisma" or half_elf_ability_two.lower() == "charisma":
#         new_ability_score = Main.charisma_roll + 1
#     return new_ability_score

# TODO: This is for leveling up a char's hp in future
# def hp_roll(char_class):
#     if char_class.lower() == "barbarian":
#         hit_points = dice_type(1, 12)
#     if char_class.lower() == "fighter" or char_class == "paladin" or char_class == "ranger":
#         hit_points = dice_type(1, 10)
#     if char_class.lower() == "bard" or char_class == "cleric" or char_class == "druid" or char_class == "monk" or char_class == "rogue" or char_class == "warlock":
#         hit_points = dice_type(1, 8)
#     if char_class.lower() == "sorcerer" or char_class == "wizard":
#         hit_points = dice_type(1, 6)
#
#     return hit_points

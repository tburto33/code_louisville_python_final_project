import random


# Dice roll simulator
def dice_type(min, max):
    int(min)
    int(max)
    return random.randint(min, max)


# Calculates abilities before passives
def ability_roll():
    total = []
    # Simulates rolling 4 1d6 dice
    roll_one = dice_type(1, 6)
    roll_two = dice_type(1, 6)
    roll_three = dice_type(1, 6)
    roll_four = dice_type(1, 6)
    # Places 4 rolls in list and removes lowest before totaling
    total.append(roll_one)
    total.append(roll_two)
    total.append(roll_three)
    total.append(roll_four)
    total.remove(min(total))

    return sum(total)


# Determines modifiers based on ability rolls
def ability_modifier(ability):
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


# Calculates starting HP based on class and constitution modifier
def starting_hp(char_class, cons_mod):
    if char_class.lower() == "barbarian":
        hit_points = 12
    if char_class.lower() == "fighter" or char_class == "paladin" or char_class == "ranger":
        hit_points = 10
    if char_class.lower() == "bard" or char_class == "cleric" or char_class == "druid" or char_class == "monk" or char_class == "rogue" or char_class == "warlock":
        hit_points = 8
    if char_class.lower() == "sorcerer" or char_class == "wizard":
        hit_points = 6
    return hit_points + cons_mod


# The following functions add racial passives into rolls
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

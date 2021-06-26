from project.Helpers import helpers


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


# Rolls for each ability, adds racial passives if needed.
def set_ability_rolls(char_race):
    char_abilities.update({"str": strength(char_race)})
    char_abilities.update({"dex": dexterity(char_race)})
    char_abilities.update({"cons": constitution(char_race)})
    char_abilities.update({"int": intelligence(char_race)})
    char_abilities.update({"wis": wisdom(char_race)})
    char_abilities.update({"char": charisma(char_race)})


# Calculates modifiers from ability rolls and then stores them into char_modifier_dict
def set_ability_modifiers():
    char_modifiers.update({"str": ability_modifier(char_abilities["str"])})
    char_modifiers.update({"dex": ability_modifier(char_abilities["dex"])})
    char_modifiers.update({"cons": ability_modifier(char_abilities["cons"])})
    char_modifiers.update({"int": ability_modifier(char_abilities["int"])})
    char_modifiers.update({"wis": ability_modifier(char_abilities["wis"])})
    char_modifiers.update({"char": ability_modifier(char_abilities["char"])})


# Stores character ability rolls
char_abilities = {
    "str": 0,
    "dex": 0,
    "cons": 0,
    "int": 0,
    "wis": 0,
    "char": 0,
}

# Stores character modifiers
char_modifiers = {
    "str": 0,
    "dex": 0,
    "cons": 0,
    "int": 0,
    "wis": 0,
    "char": 0,
}


# Calculates starting HP based on class and constitution modifier
def set_starting_hp(char_class):
    cons_mod = char_modifiers["cons"]
    hit_points = {
        "barbarian": 12,
        "fighter": 10,
        "paladin": 10,
        "ranger": 10,
        "bard": 8,
        "cleric": 8,
        "druid": 8,
        "monk": 8,
        "rogue": 8,
        "warlock": 8,
        "sorcerer": 6,
        "wizard": 6,
    }
    return hit_points[char_class] + cons_mod


def half_elf_racial():
    print("Half-Elf racial ability requires you pick 2 abilities to add +1:")
    print("\n".join(helpers.half_elf_ability))
    while True:
        try:
            ability_one_input = input("Pick first ability for +1: \n"
                                      "(Enter Abbreviation)> ")
            ability_one = ability_one_input.lower()
            if ability_one in char_abilities:
                char_abilities[ability_one] += 1
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Response")
            continue
    while True:
        try:
            ability_two_input = input("Pick second ability for +1: \n"
                                      "(Enter Abbreviation)> ")
            ability_two = ability_two_input.lower()
            if ability_two in char_abilities:
                char_abilities[ability_two] += 1
                set_ability_modifiers()
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Response")
            continue


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
    
    Strength: {char_abilities["str"]}  Mod = {char_modifiers["str"]}
    Dexterity: {char_abilities["dex"]}  Mod = {char_modifiers["dex"]}
    Constitution: {char_abilities["cons"]}  Mod = {char_modifiers["cons"]}
    Intelligence: {char_abilities["int"]}  Mod = {char_modifiers["int"]}
    Wisdom: {char_abilities["wis"]}  Mod = {char_modifiers["wis"]}
    Charisma: {char_abilities["char"]}  Mod = {char_modifiers["char"]}
    """)


# Prints skills list to console
def print_skills():
    print(f""" Your character has the following skills:

    Acrobatics: {char_modifiers["dex"]}
    Animal Handling: {char_modifiers["wis"]}
    Arcana: {char_modifiers["int"]}
    Athletics: {char_modifiers["str"]}
    Deception: {char_modifiers["char"]}
    History: {char_modifiers["int"]}
    Insight: {char_modifiers["wis"]}
    Intimidation: {char_modifiers["char"]}
    Investigation: {char_modifiers["int"]}
    Medicine: {char_modifiers["wis"]}
    Nature: {char_modifiers["int"]}
    Perception: {char_modifiers["wis"]}
    Performance: {char_modifiers["char"]}
    Persuasion: {char_modifiers["char"]}
    Religion: {char_modifiers["int"]}
    Sleight of Hand: {char_modifiers["dex"]}
    Stealth: {char_modifiers["dex"]}
    Survival: {char_modifiers["wis"]}    
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

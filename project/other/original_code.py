from project import stats
from project.Data import char_races, char_class
import sys

# THIS WAS MY ORIGINAL CODE WHEN STARTING THIS PROJECT FOR CODE LOUISVILLE PYTHON FINAL
# LEFT IT TO SHOW HOW MY CODE HAS EVOLVED IN PYTHON

print("Welcome to my DnD Character Creator!")
start = input("Ready to get started? y/n \n"
              "> ")
while True:
    if start.lower() == "y":
        sex = input("Would you like a male or female character? \n"
                    "> ")
        break
    if start.lower() == "n":
        print("Maybe next time")
        sys.exit()
    else:
        print("Invalid response")
print()
while True:
    print("--------------")
    print("RACE SELECTION")
    print("--------------")
    print("\n".join(char_races.char_race))
    race_selection = input("Which race would you like to be? \n"
                           "> ")
    print(char_races.races[race_selection.lower()])
    verify_race = input("Is this the race you want to be? y/n \n"
                        "> ")
    if verify_race.lower() == "y":
        break
    if verify_race.lower() == "n":
        print("Let's try something else.")
    else:
        print("Invalid response")
print()
while True:
    print("---------------")
    print("CLASS SELECTION")
    print("---------------")
    print("\n".join(char_class.char_class))
    class_selection = input("What class would you like to play? \n"
                            "> ")
    print(char_class.classes[class_selection.lower()])
    verify_class = input("Is this the class you want to be? y/n \n"
                         "> ")
    if verify_class.lower() == "y":
        break
    if verify_class.lower() == "n":
        print("Not for you? That's okay.")
    else:
        print("Invalid response")

# ability rolls
strength_roll = stats.strength(race_selection.lower())
dexterity_roll = stats.dexterity(race_selection.lower())
constitution_roll = stats.constitution(race_selection.lower())
intelligence_roll = stats.intelligence(race_selection.lower())
wisdom_roll = stats.wisdom(race_selection.lower())
charisma_roll = stats.charisma(race_selection.lower())

# TODO: Test for successful implementation of function
# This is if user selects Half-Elf for racial passive.
# if class_selection.lower() == "half-elf":
#     Stats.half_elf_racial_ability()


print()
print("You are playing a {} {} {}".format(sex.upper(), race_selection.upper(), class_selection.upper()))
print()
print("Your HP is: {}".format(stats.starting_hp(class_selection.lower(), stats.ability_modifier(constitution_roll))))
print()
print("Your character has the following ability stats: \n"
      "(**Racial Passives are added in. Except Half-Elf's \n"
      "+1 to two chosen ability scores. Must be added on own.**)")
print("Strength: {}  Mod = {}".format(strength_roll, stats.ability_modifier(strength_roll)))
print("Dexterity: {}  Mod = {}".format(dexterity_roll, stats.ability_modifier(dexterity_roll)))
print("Constitution: {}  Mod = {}".format(constitution_roll, stats.ability_modifier(constitution_roll)))
print("Intelligence: {}  Mod = {}".format(intelligence_roll, stats.ability_modifier(intelligence_roll)))
print("Wisdom: {}  Mod = {}".format(wisdom_roll, stats.ability_modifier(wisdom_roll)))
print("Charisma: {}  Mod = {}".format(charisma_roll, stats.ability_modifier(charisma_roll)))
print()
print("Your character has the following skill stats:")
print("Acrobatics: {}".format(stats.ability_modifier(dexterity_roll)))
print("Animal Handling: {}".format(stats.ability_modifier(wisdom_roll)))
print("Arcana: {}".format(stats.ability_modifier(intelligence_roll)))
print("Athletics: {}".format(stats.ability_modifier(strength_roll)))
print("Deception: {}".format(stats.ability_modifier(charisma_roll)))
print("History: {}".format(stats.ability_modifier(intelligence_roll)))
print("Insight: {}".format(stats.ability_modifier(wisdom_roll)))
print("Intimidation: {}".format(stats.ability_modifier(charisma_roll)))
print("Investigation: {}".format(stats.ability_modifier(intelligence_roll)))
print("Medicine: {}".format(stats.ability_modifier(wisdom_roll)))
print("Nature: {}".format(stats.ability_modifier(intelligence_roll)))
print("Perception: {}".format(stats.ability_modifier(wisdom_roll)))
print("Performance: {}".format(stats.ability_modifier(charisma_roll)))
print("Persuasion: {}".format(stats.ability_modifier(charisma_roll)))
print("Religion: {}".format(stats.ability_modifier(intelligence_roll)))
print("Sleight of Hand: {}".format(stats.ability_modifier(dexterity_roll)))
print("Stealth: {}".format(stats.ability_modifier(dexterity_roll)))
print("Survival: {}".format(stats.ability_modifier(wisdom_roll)))

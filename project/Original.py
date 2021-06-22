import Stats
from project.Data import CharRaces, CharClass
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
    print("\n".join(CharRaces.char_race))
    race_selection = input("Which race would you like to be? \n"
                           "> ")
    print(CharRaces.races[race_selection.lower()])
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
    print("\n".join(CharClass.char_class))
    class_selection = input("What class would you like to play? \n"
                            "> ")
    print(CharClass.classes[class_selection.lower()])
    verify_class = input("Is this the class you want to be? y/n \n"
                         "> ")
    if verify_class.lower() == "y":
        break
    if verify_class.lower() == "n":
        print("Not for you? That's okay.")
    else:
        print("Invalid response")

# ability rolls
strength_roll = Stats.strength(race_selection.lower())
dexterity_roll = Stats.dexterity(race_selection.lower())
constitution_roll = Stats.constitution(race_selection.lower())
intelligence_roll = Stats.intelligence(race_selection.lower())
wisdom_roll = Stats.wisdom(race_selection.lower())
charisma_roll = Stats.charisma(race_selection.lower())

# TODO: Test for successful implementation of function
# This is if user selects Half-Elf for racial passive.
# if class_selection.lower() == "half-elf":
#     Stats.half_elf_racial_ability()


print()
print("You are playing a {} {} {}".format(sex.upper(), race_selection.upper(), class_selection.upper()))
print()
print("Your HP is: {}".format(Stats.starting_hp(class_selection.lower(), Stats.ability_modifier(constitution_roll))))
print()
print("Your character has the following ability stats: \n"
      "(**Racial Passives are added in. Except Half-Elf's \n"
      "+1 to two chosen ability scores. Must be added on own.**)")
print("Strength: {}  Mod = {}".format(strength_roll, Stats.ability_modifier(strength_roll)))
print("Dexterity: {}  Mod = {}".format(dexterity_roll, Stats.ability_modifier(dexterity_roll)))
print("Constitution: {}  Mod = {}".format(constitution_roll, Stats.ability_modifier(constitution_roll)))
print("Intelligence: {}  Mod = {}".format(intelligence_roll, Stats.ability_modifier(intelligence_roll)))
print("Wisdom: {}  Mod = {}".format(wisdom_roll, Stats.ability_modifier(wisdom_roll)))
print("Charisma: {}  Mod = {}".format(charisma_roll, Stats.ability_modifier(charisma_roll)))
print()
print("Your character has the following skill stats:")
print("Acrobatics: {}".format(Stats.ability_modifier(dexterity_roll)))
print("Animal Handling: {}".format(Stats.ability_modifier(wisdom_roll)))
print("Arcana: {}".format(Stats.ability_modifier(intelligence_roll)))
print("Athletics: {}".format(Stats.ability_modifier(strength_roll)))
print("Deception: {}".format(Stats.ability_modifier(charisma_roll)))
print("History: {}".format(Stats.ability_modifier(intelligence_roll)))
print("Insight: {}".format(Stats.ability_modifier(wisdom_roll)))
print("Intimidation: {}".format(Stats.ability_modifier(charisma_roll)))
print("Investigation: {}".format(Stats.ability_modifier(intelligence_roll)))
print("Medicine: {}".format(Stats.ability_modifier(wisdom_roll)))
print("Nature: {}".format(Stats.ability_modifier(intelligence_roll)))
print("Perception: {}".format(Stats.ability_modifier(wisdom_roll)))
print("Performance: {}".format(Stats.ability_modifier(charisma_roll)))
print("Persuasion: {}".format(Stats.ability_modifier(charisma_roll)))
print("Religion: {}".format(Stats.ability_modifier(intelligence_roll)))
print("Sleight of Hand: {}".format(Stats.ability_modifier(dexterity_roll)))
print("Stealth: {}".format(Stats.ability_modifier(dexterity_roll)))
print("Survival: {}".format(Stats.ability_modifier(wisdom_roll)))

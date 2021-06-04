import Stats
import Class
import Races
import sys

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
    print("\n".join(Races.char_race))
    race_selection = input("Which race would you like to be? \n"
                           "> ")
    print(Races.races[race_selection.lower()])
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
    print("\n".join(Class.char_class))
    class_selection = input("What class would you like to play? \n"
                            "> ")
    print(Class.classes[class_selection.lower()])
    verify_class = input("Is this the class you want to be? y/n \n"
                         "> ")
    if verify_class.lower() == "y":
        break
    if verify_class.lower() == "n":
        print("Not for you? That's okay.")
    else:
        print("Invalid response")

print()
print("You are playing a {} {} {}".format(sex.upper(), race_selection.upper(), class_selection.upper()))
print()
print("Your HP is: {}".format(Stats.hp_roll(class_selection)))
print()
print("Your character has the following ability stats: \n"
      "(**Racial Passives are added in. Except Half-Elf's \n"
      "+1 to two chosen ability scores. Must be added on own.**)")
print("Strength: {}".format(Stats.strength(race_selection.lower())))
print("Dexterity: {}".format(Stats.dexterity(race_selection.lower())))
print("Constitution: {}".format(Stats.constitution(race_selection.lower())))
print("Intelligence: {}".format(Stats.intelligence(race_selection.lower())))
print("Wisdom: {}".format(Stats.wisdom(race_selection.lower())))
print("Charisma: {}".format(Stats.charisma(race_selection.lower())))

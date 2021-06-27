import sys
import random
import os
import platform
from fpdf import FPDF
from project.main import character, stats


# Starts character creator
def start_creator():
    while True:
        try:
            start_creator_input = input("Would you like to get started? y/n \n"
                                        "> ")
            start_response = start_creator_input.lower()
            if start_response == "y":
                random_or_make_input = input("Do you want a random character or do you want to create one? "
                                             "random/create \n"
                                             "> ")
                if random_or_make_input.lower() == "random":
                    character.create_random_character()
                    sys.exit()
                if random_or_make_input.lower() == "create":
                    break
                else:
                    print("Invalid Response")
                    continue
            if start_response == "n":
                print("Maybe next time.")
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid Answer. y/n only.")
            continue


# Dice roll simulator
def dice_roll(min_num, max_num):
    int(min_num)
    int(max_num)
    return random.randint(min_num, max_num)


# List for half_elf_passive in stats
half_elf_ability = [
    "Strength(str)",
    "Dexterity(dex)",
    "Constitution(cons)",
    "Intelligence(int)",
    "Wisdom(wis)",
    "Charisma(char)",
]


# Clears console after asking questions
def _clear_console():
    operating_system_clear = ''
    if platform.system() == 'Windows':
        operating_system_clear = 'cls'
    elif platform.system() == 'Linux':
        operating_system_clear = 'clear'
    clear = lambda: os.system(operating_system_clear)
    clear()


def export_to_pdf(char_name, char_sex, char_race, char_class, hit_points):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    while True:
        try:
            create_pdf_input = input("Would you like to save your character as a pdf? y/n\n"
                                     "> ")
            create_pdf_response = create_pdf_input.lower()
            if create_pdf_response == "y":
                pdf.multi_cell(200, 10,
                               txt=f"DnD(5e) Character Sheet\n"
                                   f""
                                   f"Name: {char_name}   Sex: {char_sex}   Race: {char_race}   Class: {char_class}\n"
                                   f"HP: {hit_points}\n"
                                   f"ABILITIES/MODIFIERS:\n"
                                   f"STR: {stats.char_abilities['str']} / {stats.char_modifiers['str']}\n"
                                   f"DEX: {stats.char_abilities['dex']} / {stats.char_modifiers['dex']}\n"
                                   f"CONS: {stats.char_abilities['cons']} / {stats.char_modifiers['cons']}\n"
                                   f"INT: {stats.char_abilities['int']} / {stats.char_modifiers['int']}\n"
                                   f"WIS: {stats.char_abilities['wis']} / {stats.char_modifiers['wis']}\n"
                                   f"CHAR: {stats.char_abilities['char']} / {stats.char_modifiers['char']}\n",
                               align='L')
                pdf.multi_cell(200, 8,
                               txt=f"SKILLS:\n"
                                   f"Acrobatics: {stats.char_modifiers['dex']}\n"
                                   f"Animal Handling: {stats.char_modifiers['wis']}\n"
                                   f"Arcana: {stats.char_modifiers['int']}\n"
                                   f"Athletics: {stats.char_modifiers['str']}\n"
                                   f"Deception: {stats.char_modifiers['char']}\n"
                                   f"History: {stats.char_modifiers['int']}\n"
                                   f"Insight: {stats.char_modifiers['wis']}\n"
                                   f"Intimidation: {stats.char_modifiers['char']}\n"
                                   f"Investigation: {stats.char_modifiers['int']}\n"
                                   f"Medicine: {stats.char_modifiers['wis']}\n"
                                   f"Nature: {stats.char_modifiers['int']}\n"
                                   f"Perception: {stats.char_modifiers['wis']}\n"
                                   f"Performance: {stats.char_modifiers['char']}\n"
                                   f"Persuasion: {stats.char_modifiers['char']}\n"
                                   f"Religion: {stats.char_modifiers['int']}\n"
                                   f"Sleight of Hand: {stats.char_modifiers['dex']}\n"
                                   f"Stealth: {stats.char_modifiers['dex']}\n"
                                   f"Survival: {stats.char_modifiers['wis']}\n"
                                   f"Character created using DnD generator by Alex Burton"
                                   f"https://github.com/tburto33/",
                               align='L')
                pdf.output("character_sheet.pdf", dest='F')
                break
            if create_pdf_response == "n":
                print("Paper and pencil, old school I like it.")
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid response")
            continue

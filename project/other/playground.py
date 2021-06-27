# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
import sys
from fpdf import FPDF
from project import stats


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

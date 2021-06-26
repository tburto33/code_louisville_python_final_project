# THIS IS A PLAY AROUND AREA FOR CREATING FUNCTIONS AND THINGS BEFORE IMPLEMENTATION
# WILL NOT BE IN FINAL PROJECT
from project import character
from project.data import char_races, char_class
import random
import sys
from fpdf import FPDF
from project import stats


def export_to_pdf(char_name, char_sex, char_race, char_class, hit_points):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    while True:
        try:
            create_pdf_input = input("Would you like to save your character as a pdf? y/n\n"
                                     "> ")
            create_pdf_response = create_pdf_input.lower()
            if create_pdf_response == "y":
                pdf.multi_cell(200, 10, txt=f"DnD(5e) Character Sheet\n"
                                            f"\n"
                                            f"Name: {char_name}\n"
                                            f"Sex: {char_sex} \n"
                                            f"Race: {char_race} \n"
                                            f"Class: {char_class}\n"
                                            f"Hit Points: {hit_points}\n"
                                            f"\n"
                                            f"Abilities:\n"
                                            f"Strength: {stats.char_abilities['str']}\n"
                                            f"Mod: {stats.char_modifiers['str']}\n"
                                            f"Dexterity: {stats.char_abilities['dex']}\n"
                                            f"Mod: {stats.char_modifiers['dex']}\n"
                                            f"Constitution: {stats.char_abilities['cons']}\n"
                                            f"Mod: {stats.char_modifiers['cons']}\n"
                                            f"Intelligence: {stats.char_abilities['int']}\n"
                                            f"Mod: {stats.char_modifiers['int']}\n"
                                            f"Wisdom: {stats.char_abilities['wis']}\n"
                                            f"Mod: {stats.char_modifiers['wis']}\n"
                                            f"Charisma: {stats.char_abilities['char']}\n"
                                            f"Mod: {stats.char_modifiers['char']}\n"
                                            f"\n"
                                            f"Skills:\n"
                                            f"",
                               align='L')
                pdf.multi_cell(200, 8, txt=f"Acrobatics: {stats.char_modifiers['dex']}\n"
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
                                           f"\n"
                                           f"Character created using DnD generator by Alex Burton",
                               align='L')
                pdf.output("character_sheet.pdf")
                break
            if create_pdf_response == "n":
                print("Paper and pencil, old school I like it.")
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid response")
            continue


export_to_pdf("Alex", "Male", "Human", "Monk", 12)

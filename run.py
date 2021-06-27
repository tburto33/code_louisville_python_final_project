from project.main import stats, character, helpers

print("Welcome to my DnD Character Generator!")
helpers.start_creator()
char_sex = character.select_character_sex()
char_name = character.select_character_name()
char_race = character.select_character_race()
char_clss = character.select_character_clss()
stats.set_ability_rolls(char_clss)
stats.set_ability_modifiers()
if char_race == "half-elf":
    stats.half_elf_racial()
char_hp = stats.set_starting_hp(char_clss)
user_char = character.Character(char_sex.upper(),
                                char_name.upper(),
                                char_race.upper(),
                                char_clss.upper(),
                                char_hp)
user_char.print_character()
stats.print_abilities_and_mods()
stats.print_skills()
helpers.export_to_pdf(char_name.upper(),
                      char_sex.upper(),
                      char_race.upper(),
                      char_clss.upper(),
                      char_hp)

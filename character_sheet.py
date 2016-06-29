from character_classes import *
from collections import namedtuple


ABILITIES = ("str", "dex", "con", "int", "wis", "cha")


InitialCharacterData = namedtuple(
    "InitialCharacterData",
    [
        "name",
        "character_class",
        "ability_scores",
        "experience_points",
        "skill_profs"
    ]
)


CharacterData = namedtuple(
    "CharacterData",
    [
        "name",
        "character_class",
        "ability_scores",
        "experience_points",
        "skill_profs",
        "level",
        "proficiency_bonus",
        "ability_modifiers",
        "saving_throws",
        "skills"
    ]
)


AbilityScores = namedtuple(
    "AbilityScores",
    ABILITIES
)


AbilityModifiers = namedtuple(
    "AbilityModifiers",
    ABILITIES
)


SavingThrows = namedtuple(
    "SavingThrows",
    ABILITIES
)


SkillScores = namedtuple(
    "SkillScores",
    [
        "acrobatics",
        "animal_handling",
        "arcana",
        "athletics",
        "deception",
        "history",
        "insight",
        "intimidation",
        "investigation",
        "medicine",
        "nature",
        "perception",
        "performance",
        "persuasion",
        "religion",
        "sleight_of_hand",
        "stealth",
        "survival"
    ]
)


def calc_level(xp: int) -> int:
    leveling_points = (
        0, 300, 900, 2700, 6500,
        14000, 23000, 34000, 48000, 64000,
        85000, 100000, 120000, 140000, 165000,
        195000, 225000, 265000, 305000, 355000
    )
    leveling_info = [1 if xp >= lp else 0 for lp in leveling_points]
    return sum(leveling_info)


def calc_prof_bonus(level: int) -> int:
    initial_prof = 2
    prof_gaining_levels = (5, 9, 13, 17)
    prof_gaining_info = [1 if level >= pgl else 0 for pgl in prof_gaining_levels]
    return initial_prof + sum(prof_gaining_info)


def calc_ability_modifier(ability_scores: AbilityScores) -> AbilityModifiers:
    def calc_mod(ability_score: int) -> int:
        return (ability_score - 10) // 2
    return AbilityModifiers(
        str=calc_mod(ability_scores.str),
        dex=calc_mod(ability_scores.dex),
        con=calc_mod(ability_scores.con),
        int=calc_mod(ability_scores.int),
        wis=calc_mod(ability_scores.wis),
        cha=calc_mod(ability_scores.cha)
    )


def calc_saving_throws(
    ability_mods: AbilityModifiers,
    char_class: CharacterClass,
    prof_bonus: int
) -> SavingThrows:
    saving_throws = char_class.saving_throw_bonuses

    def calc_saving_throw(ability_mod: int, ability: str):
        if ability in saving_throws:
            return ability_mod + prof_bonus
        else:
            return ability_mod

    return SavingThrows(
        str=calc_saving_throw(ability_mods.str, "str"),
        dex=calc_saving_throw(ability_mods.dex, "dex"),
        con=calc_saving_throw(ability_mods.con, "con"),
        int=calc_saving_throw(ability_mods.int, "int"),
        wis=calc_saving_throw(ability_mods.wis, "wis"),
        cha=calc_saving_throw(ability_mods.cha, "cha"),
    )


def calc_skills(
    ability_mods: AbilityModifiers,
    skill_profs: tuple,
    prof_bonus: int
) -> SkillScores:

    def calc_skill(ability_mod: int, skill: str):
        if skill in skill_profs:
            return ability_mod + prof_bonus
        else:
            return ability_mod

    return SkillScores(
        acrobatics=calc_skill(ability_mods.dex, "acrobatics"),
        animal_handling=calc_skill(ability_mods.wis, "animal_handling"),
        arcana=calc_skill(ability_mods.int, "arcana"),
        athletics=calc_skill(ability_mods.str, "athletics"),
        deception=calc_skill(ability_mods.cha, "deception"),
        history=calc_skill(ability_mods.int, "history"),
        insight=calc_skill(ability_mods.wis, "insight"),
        intimidation=calc_skill(ability_mods.cha, "intimidation"),
        investigation=calc_skill(ability_mods.int, "investigation"),
        medicine=calc_skill(ability_mods.wis, "medicine"),
        nature=calc_skill(ability_mods.int, "nature"),
        perception=calc_skill(ability_mods.wis, "perception"),
        performance=calc_skill(ability_mods.cha, "performance"),
        persuasion=calc_skill(ability_mods.cha, "persuasion"),
        religion=calc_skill(ability_mods.int, "religion"),
        sleight_of_hand=calc_skill(ability_mods.dex, "sleight_of_hand"),
        stealth=calc_skill(ability_mods.dex, "stealth"),
        survival=calc_skill(ability_mods.wis, "survival")
    )


def build_character(init_char_data: InitialCharacterData) -> CharacterData:
    level =\
        calc_level(init_char_data.experience_points)
    prof_bonus =\
        calc_prof_bonus(level)
    ability_modifiers =\
        calc_ability_modifier(init_char_data.ability_scores)
    saving_throws =\
        calc_saving_throws(ability_modifiers, init_char_data.character_class, prof_bonus)
    skills =\
        calc_skills(ability_modifiers, init_char_data.skill_profs, prof_bonus)

    return CharacterData(
        init_char_data.name,
        init_char_data.character_class,
        init_char_data.ability_scores,
        init_char_data.experience_points,
        init_char_data.skill_profs,
        level,
        prof_bonus,
        ability_modifiers,
        saving_throws,
        skills
    )


if __name__ == '__main__':
    initial_char_data = InitialCharacterData(
        name="Midnight",
        character_class=bard,
        ability_scores=AbilityScores(15, 10, 10, 10, 10, 10),
        experience_points=0,
        skill_profs=("acrobatics", "arcana", "deception")
    )
    char_data = build_character(initial_char_data)
    from pprint import pprint
    pprint(char_data._asdict())

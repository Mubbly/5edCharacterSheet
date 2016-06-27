from copy import deepcopy
from character_classes import *
from typing import Dict, Union

_CharDataValues = Union[str, CharacterClass, int]
CharData = Dict[str, _CharDataValues]

character_data = {
    "name": "Midnight",
    "character_class": bard,
    "experience_points": 0,
    "abilities": {
        "str": 10,
        "dex": 10,
        "con": 10,
        "int": 10,
        "wis": 10,
        "cha": 10
    },
    "skill_profs": ("performance", "deception", "investigation")
}


def pipe(init_input, *args):
    value = init_input
    for func in args:
        value = func(value)
    return value


def add_level(char_data: CharData) -> CharData:
    assert "experience_points" in char_data.keys()
    new_char_data = deepcopy(char_data)

    xp = new_char_data["experience_points"]

    leveling_points = (
        0, 300, 900, 2700, 6500,
        14000, 23000, 34000, 48000, 64000,
        85000, 100000, 120000, 140000, 165000,
        195000, 225000, 265000, 305000, 355000
    )

    level = 0

    for leveling_point in leveling_points:
        if xp >= leveling_point:
            level += 1
        else:
            break

    new_char_data["level"] = level
    return new_char_data


def add_prof_bonus(char_data: CharData) -> CharData:
    assert "level" in char_data.keys()
    new_char_data = deepcopy(char_data)
    level = new_char_data["level"]
    prof_bonus = 2

    prof_bonus_gaining_levels = (5, 9, 13, 17)

    for prof_gaining_level in prof_bonus_gaining_levels:
        if level >= prof_gaining_level:
            prof_bonus += 1
        else:
            break

    new_char_data["prof_bonus"] = prof_bonus
    return new_char_data


def add_ability_modifiers(char_data: CharData) -> CharData:
    ability_score_keys = ("str", "dex", "con", "int", "wis", "cha")
    for ability_score in ability_score_keys:
        assert ability_score in char_data["abilities"].keys()
    new_char_data = deepcopy(char_data)
    ability_scores = char_data["abilities"]

    def calc_modifier(ability_score: int) -> int:
        from math import floor
        return floor((ability_score - 10) / 2)

    for score_key in ability_score_keys:
        modifier_key = score_key + "_modifier"
        ability_score = ability_scores[score_key]
        modifier = calc_modifier(ability_score)
        new_char_data[modifier_key] = modifier

    return new_char_data


def add_saving_throws(char_data: CharData) -> CharData:
    # as = ability scores
    as_keys = ("str", "dex", "con", "int", "wis", "cha")
    mod_keys = tuple([key + "_modifier" for key in as_keys])
    saving_throw_keys = tuple([key + "_saving_throw" for key in as_keys])

    for key in mod_keys:
        assert key in char_data.keys()
    new_char_data = deepcopy(char_data)

    for i in range(len(as_keys)):
        mod_key = mod_keys[i]
        saving_throw_key = saving_throw_keys[i]
        new_char_data[saving_throw_key] = \
            new_char_data[mod_key]

    char_class = new_char_data["character_class"]
    bonus_stats = char_class.saving_throw_bonuses
    prof_bonus = new_char_data["prof_bonus"]

    for stat in bonus_stats:
        saving_throw_key = stat + "_saving_throw"
        new_char_data[saving_throw_key] += prof_bonus

    return new_char_data


def add_skills(char_data: CharData) -> CharData:
    as_keys = ("str", "dex", "con", "int", "wis", "cha")
    mod_keys = tuple([key + "_modifier" for key in as_keys])

    skills = (
        ("acrobatics", "dex"),
        ("animal_handling", "wis"),
        ("arcana", "int"),
        ("athletics", "str"),
        ("deception", "cha"),
        ("history", "int"),
        ("insight", "wis"),
        ("intimidation", "cha"),
        ("investigation", "int"),
        ("medicine", "wis"),
        ("nature", "int"),
        ("perception", "wis"),
        ("performance", "cha"),
        ("persuasion", "cha"),
        ("religion", "int"),
        ("sleight_of_hand", "dex"),
        ("stealth", "dex"),
        ("survival", "wis")
    )

    for key in mod_keys:
        assert key in char_data.keys()
    assert "skill_profs" in char_data.keys()
    assert "prof_bonus" in char_data.keys()
    new_char_data = deepcopy(char_data)

    char_skills = {}

    for skill, ability in skills:
        ability_mod_key = ability + "_modifier"
        char_skills[skill] = new_char_data[ability_mod_key]

    skill_profs = new_char_data["skill_profs"]
    prof_bonus = new_char_data["prof_bonus"]

    for skill_prof in skill_profs:
        char_skills[skill_prof] += prof_bonus

    new_char_data["skills"] = char_skills

    return new_char_data


def build_character(char_data: CharData) -> CharData:
    return pipe(
        char_data,
        add_level,
        add_prof_bonus,
        add_ability_modifiers,
        add_saving_throws,
        add_skills
        # todo
    )


if __name__ == '__main__':
    from pprint import pprint
    pprint(build_character(character_data))

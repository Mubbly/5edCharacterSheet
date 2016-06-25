from copy import deepcopy
from character_classes import *
from typing import Dict, Union

_CharDataValues = Union[str, CharacterClass, int]
CharData = Dict[str, _CharDataValues]

character_data = {
    "name": "Midnight",
    "character_class": bard,
    "experience_points": 0,
    "str": 10,
    "dex": 10,
    "con": 10,
    "int": 10,
    "wis": 10,
    "cha": 10
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
        assert ability_score in char_data.keys()
    new_char_data = deepcopy(char_data)

    def calc_modifier(ability_score: int) -> int:
        from math import floor
        return floor((ability_score - 10) / 2)

    for score_key in ability_score_keys:
        modifier_key = score_key + "_modifier"
        ability_score = new_char_data[score_key]
        modifier = calc_modifier(ability_score)
        new_char_data[modifier_key] = modifier

    return new_char_data


if __name__ == '__main__':
    pass

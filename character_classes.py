from collections import namedtuple


CharacterClass = namedtuple(
    "CharacterClass",
    ["hp_per_level", "saving_throw_bonuses"]
    # TODO: code skills for classes
)

barbarian = \
    CharacterClass(12, ("str", "con"))
bard = \
    CharacterClass(8, ("dex", "cha"))
cleric = \
    CharacterClass(8, ("wis", "cha"))
druid = \
    CharacterClass(8, ("int", "wis"))
fighter = \
    CharacterClass(10, ("str", "con"))
monk = \
    CharacterClass(8, ("str", "dex"))
paladin = \
    CharacterClass(10, ("wis", "cha"))
ranger = \
    CharacterClass(10, ("str", "dex"))
rouge = \
    CharacterClass(8, ("dex", "int"))
sorcerer = \
    CharacterClass(6, ("con", "cha"))
warlock = \
    CharacterClass(8, ("wis", "cha"))
wizard = \
    CharacterClass(6, ("int", "wis"))

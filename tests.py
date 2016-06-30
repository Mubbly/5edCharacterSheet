import unittest
from character_sheet import *


class MyTests(unittest.TestCase):
    def test_calc_level(self):
        input_and_expected = (
            (0, 1),
            (14000, 6),
            (265000, 18)
        )

        for inp, expected in input_and_expected:
            self.assertEqual(calc_level(inp), expected)

    def test_calc_prof_bonus(self):
        input_and_expected = (
            (1, 2),
            (6, 3),
            (18, 6),
        )

        for inp, expected in input_and_expected:
            self.assertEqual(calc_prof_bonus(inp), expected)

    def test_calc_ability_modifiers(self):
        input_and_expected = (
            (AbilityScores(12, 13, 11, 16, 18, 13), AbilityModifiers(1, 1, 0, 3, 4, 1)),
            (AbilityScores(15, 11, 13, 17, 14, 15), AbilityModifiers(2, 0, 1, 3, 2, 2)),
        )

        for inp, expected in input_and_expected:
            self.assertEqual(calc_ability_modifier(inp), expected)

    def test_calc_saving_throws(self):
        input_and_expected = (
            (
                {
                    "ability_mods": AbilityModifiers(0, 0, 0, 0, 0, 0),
                    "char_class": bard,
                    "prof_bonus": 2
                },
                SavingThrows(str=0, dex=2, con=0, int=0, wis=0, cha=2)
            ),
            (
                {
                    "ability_mods": AbilityModifiers(2, 3, 1, -2, -1, 0),
                    "char_class": monk,
                    "prof_bonus": 4
                },
                SavingThrows(str=6, dex=7, con=1, int=-2, wis=-1, cha=0)
            )
        )
        for inp, expected in input_and_expected:
            self.assertEqual(calc_saving_throws(**inp), expected)

    def test_calc_skills(self):
        inp = {
            "ability_mods": AbilityModifiers(
                str=0,
                dex=1,
                con=2,
                int=3,
                wis=4,
                cha=5),
            "skill_profs": ("acrobatics", "arcana", "deception"),
            "prof_bonus": 2
        }
        expected = SkillScores(
            acrobatics=3,
            animal_handling=4,
            arcana=5,
            athletics=0,
            deception=7,
            history=3,
            insight=4,
            intimidation=5,
            investigation=3,
            medicine=4,
            nature=3,
            perception=4,
            performance=5,
            persuasion=5,
            religion=3,
            sleight_of_hand=1,
            stealth=1,
            survival=4
        )

        self.assertEqual(calc_skills(**inp), expected)


if __name__ == '__main__':
    unittest.main()
import unittest
from character_sheet import *


def inc(x: int) -> int:
    return x + 1


class MyTests(unittest.TestCase):

    def test_pipe(self):
        result = pipe(
            1,
            inc,
            inc,
            inc
        )
        self.assertEqual(result, 4)

    def test_add_level(self):
        test_data1 = {"experience_points": 0}
        test_data2 = {"experience_points": 20000}
        test_data3 = {"experience_points": 300000}

        real_and_expected = (
            (add_level(test_data1)["level"], 1),
            (add_level(test_data2)["level"], 6),
            (add_level(test_data3)["level"], 18)
        )

        for real, expected in real_and_expected:
            self.assertEqual(real, expected)

    def test_add_prof_bonus(self):
        test_data1 = {"level": 1}
        test_data2 = {"level": 6}
        test_data3 = {"level": 18}

        real_and_expected = (
            (add_prof_bonus(test_data1)["prof_bonus"], 2),
            (add_prof_bonus(test_data2)["prof_bonus"], 3),
            (add_prof_bonus(test_data3)["prof_bonus"], 6),
        )

        for real, expected in real_and_expected:
            self.assertEqual(real, expected)

    def test_add_ability_modifiers(self):
        test_data1 = {
            "abilities": {
                "str": 12,
                "dex": 13,
                "con": 11,
                "int": 16,
                "wis": 18,
                "cha": 13
            }
        }

        expected_result1 = dict(
            test_data1,
            **{
                "str_modifier": 1,
                "dex_modifier": 1,
                "con_modifier": 0,
                "int_modifier": 3,
                "wis_modifier": 4,
                "cha_modifier": 1
            }
        )

        test_data2 = {
            "abilities": {
                "str": 15,
                "dex": 11,
                "con": 13,
                "int": 17,
                "wis": 14,
                "cha": 15
            }
        }

        expected_result2 = dict(
            test_data2,
            **{
                "str_modifier": 2,
                "dex_modifier": 0,
                "con_modifier": 1,
                "int_modifier": 3,
                "wis_modifier": 2,
                "cha_modifier": 2
            }
        )

        real_and_expected = (
            (add_ability_modifiers(test_data1), expected_result1),
            (add_ability_modifiers(test_data2), expected_result2)
        )

        for real, expected in real_and_expected:
            self.assertEqual(real, expected)

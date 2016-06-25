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

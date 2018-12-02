"""
    Day02 tests.
"""

import unittest

from days.d02 import Day02


class Day01Tests(unittest.TestCase):
    """Tests for `Day01`."""

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        data = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab",
        ]
        day = Day02(data)

        self.assertEqual(day.solve_part_one(), 12)

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        data = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz",
        ]
        day = Day02(data)

        self.assertEqual(day.solve_part_two(), "fgij")

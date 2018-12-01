"""
    Day01 tests.
"""

import unittest

from days.d01 import Day01


class Day01Tests(unittest.TestCase):
    """Tests for `Day01`."""

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        tests = [
            (["+1", "+1", "+1"], 3),
            (["+1", "+1", "-2"], 0),
            (["-1", "-2", "-3"], -6),
        ]

        for test in tests:
            day = Day01(test[0])
            self.assertEqual(day.solve_part_one(), test[1])

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        tests = [
            (["+1", "-1"], 0),
            (["+3", "+3", "+4", "-2", "-4"], 10),
            (["-6", "+3", "+8", "+5", "-6"], 5),
            (["+7", "+7", "-2", "-7", "-4"], 14),
        ]

        for test in tests:
            day = Day01(test[0])
            self.assertEqual(day.solve_part_two(), test[1])

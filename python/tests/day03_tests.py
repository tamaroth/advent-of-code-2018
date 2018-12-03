"""
    Day03 tests.
"""

import unittest

from days.d03 import Day03


class Day03Tests(unittest.TestCase):
    """Tests for `Day03`."""

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        data = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
        ]
        day = Day03(data)

        self.assertEqual(day.solve_part_one(), 4)

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        data = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
        ]
        day = Day03(data)

        day.solve_part_one()

        self.assertEqual(day.solve_part_two(), 3)

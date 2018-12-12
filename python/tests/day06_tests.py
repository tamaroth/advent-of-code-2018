"""
    Day06 tests.
"""

import unittest

from days.d06 import Day06


class Day06Tests(unittest.TestCase):
    """Tests for `Day06`."""

    def setUp(self):
        self._day = Day06(['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9'], max_distance=32)

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_one(), 17)

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        self._day.solve_part_one()

        self.assertEqual(self._day.solve_part_two(), 16)

"""
    Day05 tests.
"""

import unittest

from days.d05 import Day05


class Day05Tests(unittest.TestCase):
    """Tests for `Day05`."""

    def setUp(self):
        self._day = Day05('dabAcCaCBAcCcaDA')

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_one(), 10)

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_two(), 4)

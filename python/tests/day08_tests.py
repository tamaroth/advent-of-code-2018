"""
    Day08 tests.
"""

import unittest

from days.d08 import Day08


class Day08Tests(unittest.TestCase):
    """Tests for `Day08`."""

    def setUp(self):
        self._day = Day08(
            '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
        )

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_one(), 138)

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_two(), 65)

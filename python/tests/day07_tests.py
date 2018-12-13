"""
    Day07 tests.
"""

import unittest

from days.d07 import Day07


class Day07Tests(unittest.TestCase):
    """Tests for `Day07`."""

    def setUp(self):
        self._day = Day07(
            [
                'Step C must be finished before step A can begin.',
                'Step C must be finished before step F can begin.',
                'Step A must be finished before step B can begin.',
                'Step A must be finished before step D can begin.',
                'Step B must be finished before step E can begin.',
                'Step D must be finished before step E can begin.',
                'Step F must be finished before step E can begin.',
            ],
            worker_count=2,
            starter_time=0
        )

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_one(), 'CABDFE')

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        self.assertEqual(self._day.solve_part_two(), 15)

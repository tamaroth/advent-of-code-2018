"""
    Day04 tests.
"""

import unittest

from days.d04 import Day04


class Day04Tests(unittest.TestCase):
    """Tests for `Day04`."""

    def setUp(self):
        super().setUp()

        self._data = [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up',
        ]

    def test_solve_part_one_solves_the_puzzle_correctly(self):
        day = Day04(self._data)

        self.assertEqual(day.solve_part_one(), 240)

    def test_solve_part_two_solves_the_puzzle_correctly(self):
        day = Day04(self._data)

        day.solve_part_one()
        self.assertEqual(day.solve_part_two(), 4455)

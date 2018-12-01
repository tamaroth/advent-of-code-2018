"""
    Day 1: Chronal Calibration
"""

from days import Day
from utils.file import read_lines_of_datafile


class Day01(Day):
    """
        A solution to Day 1: Chronal Calibration problem.
    """

    def __init__(self, data):
        super().__init__("Day 1: Chronal Calibration")

        self._data = self._convert_input_to_integers(data)

    def solve_part_one(self):
        self._part_one = 0
        for value in self._data:
            self._part_one += value

        return self._part_one

    def solve_part_two(self):
        self._part_two = 0
        helper = {0}
        while True:
            for value in self._data:
                self._part_two += value
                if self._part_two in helper:
                    return self._part_two
                helper.add(self._part_two)

        return self._part_two

    def _convert_input_to_integers(self, data):
        return [int(value) for value in data]


def get_day_01():
    return Day01(
        read_lines_of_datafile(__file__, 'day_01_data.txt')
    )

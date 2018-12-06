"""
    Day 2: Inventory Management System
"""

from days import Day
from utils.file import read_lines_of_datafile


class Day02(Day):
    """
        A solution to Day 2: Inventory Management System problem.
    """

    def __init__(self, data):
        super().__init__("Day 2: Inventory Management System")

        self._data = data

    def solve_part_one(self):
        self._part_one = 0
        twice = 0
        thrice = 0
        for line in self._data:
            r = self._has_repeated_characters_twice_or_thrice_in_string(line)
            twice += 1 if r[0] else 0
            thrice += 1 if r[1] else 0
        self._part_one = twice * thrice
        return self._part_one

    def solve_part_two(self):
        key1, key2 = self._find_two_similar_strings(self._data)
        return self._get_common_string(key1, key2)

    def _find_two_similar_strings(self, elements):
        """Finds two strings in a list that differ by at most one character."""
        if len(elements) == 1:
            return (None, None)
        key = elements[0]
        sub = elements[1:]
        for subkey in sub:
            if self._are_strings_similar(key, subkey):
                return (key, subkey)
        return self._find_two_similar_strings(sub)

    def _are_strings_similar(self, key1, key2):
        """Checks whether two strings differ by at most one character."""
        ok = False
        for c1, c2 in zip(key1, key2):
            if c1 != c2:
                if ok:
                    return False
                else:
                    ok = True
        return ok

    def _get_common_string(self, key1, key2):
        """Returns a string that comprises of only common characters between two strings."""
        result = ""
        for c1, c2 in zip(key1, key2):
            if c1 == c2:
                result += c1
        return result

    def _has_repeated_characters_twice_or_thrice_in_string(self, line):
        """Returns a tuple with the number of characters in a string that appear
        there exactly twice and thrice.
        """
        d = dict.fromkeys(line, 0)
        for c in line:
            d[c] += 1
        twice = False
        thrice = False
        for c, count in d.items():
            if count == 2:
                twice = True
            elif count == 3:
                thrice = True
        return (twice, thrice)

def get_day_02():
    """Returns the ``Day02`` for the puzzle data."""
    return Day02(
        read_lines_of_datafile('day_02_data.txt')
    )

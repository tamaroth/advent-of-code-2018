"""
    Day 5: Alchemical Reduction
"""

from days import Day
from utils.file import read_lines_of_datafile


def get_day_05():
    return Day05(
        read_lines_of_datafile('day_05_data.txt')[0]
    )


class Day05(Day):
    """A solution to Day 5: Alchemical Reduction."""

    def __init__(self, data):
        super().__init__('Day 5: Alchemical Reduction')

        self._polymer = data

    def solve_part_one(self):
        """Solves the first part of the task.

        It reacts the whole polymer and returns its length.
        """
        return len(self._react_polymer(self._polymer))

    def solve_part_two(self):
        """Solves the second part of the task.

        Finds all possible units of the polymer, then for each unit it completely
        removes it from polymer and finally reacts it. The solution is the shortest
        of all possible reduced and reacted polymers.
        """
        units = self._get_possible_units(self._polymer)
        shortest = len(self._polymer)
        for unit in units:
            polymer = self._reduce_polymer(self._polymer, unit)
            shortest = min(shortest, len(self._react_polymer(polymer)))
        return shortest

    def _react_polymer(self, polymer):
        """Reacts the given polymer.

        Process of polymer reaction tries to find two adjacent units of the same
        type but opposite polarity. When they are found, they are removed and
        the process of polymer reaction starts again from the last visited unit.
        """
        reactive = True
        index = 0
        while reactive:
            # For each pass compute the length of the polymer.
            end = len(polymer)
            while index + 1 < end:
                this = polymer[index]
                next = polymer[index + 1]
                if self._are_identical_same_types(this, next) and self._are_opposite_polarity(this, next):
                    polymer = polymer[:index] + polymer[index+2:]
                    # If the current index is not at the beginning of the polymer,
                    # we need to react it again.
                    if index != 0:
                        index -= 1
                    break
                index += 1
            if index + 1 >= len(polymer):
                reactive = False

        return polymer

    def _reduce_polymer(self, polymer, unit):
        """Reduces the given polymer by the given unit (irrespective of its
        polarity).
        """
        return polymer.translate({
            ord(unit.lower()): '',
            ord(unit.upper()): '',
        })

    def _get_possible_units(self, polymer):
        """Get all possible units from the given polymer.

        The returned dictionary consists only of lowercase units.
        """
        possibilities = set()
        for c in polymer:
            if c.lower() not in possibilities:
                possibilities.add(c.lower())
        return possibilities

    def _are_identical_same_types(self, unit_a, unit_b):
        """Checks whether the two given units have the same type."""
        return unit_a.lower() == unit_b.lower()

    def _are_opposite_polarity(self, unit_a, unit_b):
        """Checks whether the two given units have opposite polarity."""
        return ((unit_a.islower() and unit_b.isupper()) or (unit_a.isupper() and unit_b.islower()))

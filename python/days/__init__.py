"""
    A base abstract class for all days.
"""

import abc


class Day(abc.ABC):
    """A base abstract class for solutions to problems given each single day."""

    def __init__(self, title):
        self._title = title
        self._part_one = None
        self._part_two = None

    @abc.abstractmethod
    def solve_part_one(self, *args, **kwargs):
        """Solves the part one of the given day."""

    @abc.abstractmethod
    def solve_part_two(self, *args, **kwargs):
        """Solves the part two of the given day."""

    @property
    def part_one(self):
        """Returns the solution to the first part."""
        return self._part_one

    @property
    def part_two(self):
        """Returns the solution to the second part."""
        return self._part_two

    @property
    def title(self):
        return self._title

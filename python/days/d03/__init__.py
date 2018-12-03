"""
    Day 3: No Matter How You Slice It
"""

import re

from days import Day
from utils.file import read_lines_of_datafile


def get_day_03():
    return Day03(
        read_lines_of_datafile('day_03_data.txt')
    )


class Claim:
    """A single claim.

    Claim is a string that declares how piece of cloth should be cut. It's in the
    form of "#1 @ 1,3: 4x4" and it represents:
     - the ID of the claim
     - the left margin
     - the top margin
     - width
     - height

    This class converts the string representation and stores the numerical
    values.
    """

    def __init__(self, claim):
        match = re.search(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', claim)
        if len(match.groups()) != 5:
            raise ValueError(
                f'bad claim: {claim}, found {len(match.groups())} groups')
        try:
            self._id = int(match.group(1))
            self._left = int(match.group(2))
            self._top = int(match.group(3))
            self._width = int(match.group(4))
            self._height = int(match.group(5))
        except ValueError as e:
            print(e)
            raise

    @property
    def id(self):
        """The ID of the claim."""
        return self._id

    @property
    def left(self):
        """How much space should be left on the left side?"""
        return self._left

    @property
    def top(self):
        """How much space should be left from the top?."""
        return self._top

    @property
    def width(self):
        """How wide the material should be?"""
        return self._width

    @property
    def height(self):
        """How tall the material should be?"""
        return self._height


class Day03(Day):
    """A solution to Day 3: No Matter How You Slice It"""

    def __init__(self, data):
        super().__init__("Day 1: Chronal Calibration")

        self._data = [Claim(line) for line in data]
        self._claims = []
        self._sheet = {}

    def solve_part_one(self):
        """Solves the first part of the task.

        Given a list of claims, we should count number of squares that are
        overlapping. We do so by placing each claim on the sheet (a dictionary
        of coordinates and number of claims that want to use a specific square)
        and finally counting the number of squares with number of claims greater
        or equal to 2.
        """
        for claim in self._data:
            if not self._place_claim_in_data_sheet(claim):
                self._claims.append(claim)

        result = 0
        for _, value in self._sheet.items():
            if value >= 2:
                result += 1
        return result

    def solve_part_two(self):
        """Solves the second part of the task.

        Given the sheet from the first part, we investigate whether each claim
        has overlapping squares. If it does not, we return it as a solution,
        otherwise we return ``None``.
        """
        for claim in self._claims:
            if not self._is_overlapped(claim):
                return claim.id
        return None

    def _place_claim_in_data_sheet(self, claim):
        """Places the given claim on the sheet.

        :returns: ``True`` if a claim is not overlapping, otherwise ``False``.

        note: If a claim is not overlapped, it still might be in the future.
        """
        overlapped = False
        for row in range(claim.height):
            for column in range(claim.width):
                idx = (claim.left + column, claim.top + row)
                val = self._sheet.get(idx, 0) + 1
                self._sheet[idx] = val
                if val >= 2:
                    overlapped = True
        return overlapped

    def _is_overlapped(self, claim):
        """Checks whether the given claim is overlapped."""
        for row in range(claim.height):
            for column in range(claim.width):
                idx = (claim.left + column, claim.top + row)
                if self._sheet.get(idx, 2) >= 2:
                    return True
        return False

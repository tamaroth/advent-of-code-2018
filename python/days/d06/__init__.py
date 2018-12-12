"""
    Day 6: Chronal Coordinates
"""

from days import Day
from utils.file import read_lines_of_datafile


def get_day_06():
    return Day06(
        read_lines_of_datafile('day_06_data.txt')
    )


class Day06(Day):
    """A solution to Day 6: Chronal Coordinates."""

    def __init__(self, data, max_distance=None):
        super().__init__('Day 6: Chronal Coordinates')

        self._points = Points.from_string_lines(data)
        self._min_x, self._min_y = self._points.min()
        self._max_x, self._max_y = self._points.max()
        self._max_distance = max_distance if max_distance is not None else 10000

    def solve_part_one(self):
        """Solves the first part of the task."""
        grid = self._get_distance_grid()
        finite_points = self._get_finite_points(grid)
        return max([point.get_score_on_grid(grid) for point in finite_points])

    def solve_part_two(self):
        """Solves the second part of the task."""
        assert self._max_distance, 'total distance is not set'
        region_size = 0
        for x in self._get_x_range():
            for y in self._get_y_range():
                if self._get_distance_to_all_coords(x, y) < self._max_distance:
                    region_size += 1

        return region_size

    def _get_distance_grid(self):
        grid = {}
        init_max = Point.generate_id(self._max_x, self._max_y)
        for x in self._get_x_range():
            for y in self._get_y_range():
                max_distance = init_max
                for point in self._points:
                    distance = point.distance_from(x, y)
                    if distance < max_distance:
                        grid[(x, y)] = point.id
                        max_distance = distance
                    elif distance == max_distance and distance != init_max:
                        grid[(x, y)] = -1
        return grid

    def _get_finite_points(self, grid):
        return [point for point in self._points if not self._is_point_infinite(point, grid)]

    def _is_point_infinite(self, point, grid):
        for x in self._get_x_range():
            if grid[(x, self._min_y)] == point.id or grid[(x, self._max_y - 1)] == point.id:
                return True
        for y in self._get_y_range():
            if grid[(self._min_x, y)] == point.id or grid[(self._max_x - 1, y)] == point.id:
                return True
        return False

    def _get_distance_to_all_coords(self, x, y):
        score = 0
        for point in self._points:
            score += point.distance_from(x, y)
        return score

    def _get_x_range(self):
        return range(self._min_x, self._max_x)

    def _get_y_range(self):
        return range(self._min_y, self._max_y)


class Point:
    """A point on the board."""

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._id = Point.generate_id(x, y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def id(self):
        return self._id

    def distance_from(self, x, y):
        return abs(self._x - x) + abs(self._y - y)

    def get_score_on_grid(self, grid):
        score = 0
        for id in grid.values():
            if id == self.id:
                score += 1
        return score

    @classmethod
    def from_string(cls, string):
        elements = string.split(sep=', ')
        return cls(int(elements[0]), int(elements[1]))

    @staticmethod
    def generate_id(x, y):
        if x > y:
            return x**2 + y
        else:
            return (y+1)**2 - 1 - x


class Points(list):
    """A list of Points."""

    def min(self):
        """Returns a tuple of minimal x and y coordinates between all points.

        Values are reduced by 1 to include margin.
        """
        return (
            min(point.x for point in self) - 1,
            min(point.y for point in self) - 1
        )

    def max(self):
        """Returns a tuple of maximal x and y coordinates between all points.

        Values are increased by 2 to include margin.
        """
        return (
            max(point.x for point in self) + 2,
            max(point.y for point in self) + 2
        )

    @classmethod
    def from_string_lines(cls, lines):
        return cls(Point.from_string(line) for line in lines)

"""
    Day 8: Memory Maneuver
"""

import collections
import re

from days import Day
from utils.file import read_line_of_datafile


def get_day_08():
    return Day08(
        read_line_of_datafile('day_08_data.txt')
    )


class Node:
    """A node of the tree.

    :param list nodes: List of all children nodes.
    :param list metadata: List of all metadata values."""

    def __init__(self, nodes, metadata):
        self._nodes = nodes
        self._metadata = metadata

    @property
    def value(self):
        """Return the strict value of the tree."""
        if not self._nodes:
            return sum(self._metadata)

        metadata = 0
        for index in self._metadata:
            if index > 0 and index <= len(self._nodes):
                metadata += self._nodes[index-1].value
        return metadata

    @property
    def absolute_value(self):
        """Return the absolute value of the tree."""
        return sum(self._metadata) + sum([node.absolute_value for node in self._nodes])

    @classmethod
    def from_stream(cls, stream):
        """Creates a tree from the given stream of data."""
        children_count = int(stream.popleft())
        metadata_count = int(stream.popleft())

        nodes = []
        for _ in range(children_count):
            nodes.append(Node.from_stream(stream))

        metadata = []
        for _ in range(metadata_count):
            metadata.append(int(stream.popleft()))

        return cls(nodes, metadata)


class Day08(Day):
    """A solution to Day 8: Memory Maneuver."""

    def __init__(self, data):
        super().__init__('Day 8: Memory Maneuver')
        self._tree = Node.from_stream(collections.deque(data.split(sep=' ')))

    def solve_part_one(self):
        """Solves the first part of the task."""
        return self._tree.absolute_value

    def solve_part_two(self):
        """Solves the second part of the task."""
        return self._tree.value

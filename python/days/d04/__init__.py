"""
    Day 4: Repose Record
"""

import datetime
import enum
import re

from days import Day
from utils.file import read_lines_of_datafile


def get_day_04():
    return Day04(
        read_lines_of_datafile('day_04_data.txt')
    )


class Guard:
    """Guard details.

    :param int id: ID of the guard
    """

    def __init__(self, id):
        self._id = id
        self._minutes = {}
        self._total_asleep = 0

    def falls_asleep(self, timestamp):
        """Records the time when the guard falls asleep."""
        self._falls_asleep = self._to_datetime(timestamp)

    def wakes_up(self, timestamp):
        """Records the time when the guard wakes up and updates their sleep
        pattern.
        """
        self._update_sleep_pattern(self._to_datetime(timestamp))
        self._falls_asleep = None

    @property
    def id(self):
        """The ID of the guard."""
        return self._id

    @property
    def total_asleep(self):
        """How many minutes overall was the guard asleep?"""
        return self._total_asleep

    @property
    def best_minute(self):
        """What is the minute that the guard was asleep the most times at.

        If there is no record of the guard's sleep pattern, ``None`` is returned.
        """
        return max(self._minutes, key=self._minutes.get) if self._minutes else None

    def get_times_asleep_on_minute(self, minute):
        """Returns the number of times the guard was asleep on the given minute."""
        if minute is None:
            return 0
        return self._minutes.get(minute, 0)

    def _to_datetime(self, timestamp):
        """Converts the timestamp to ``datetime`` object."""
        return datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')

    def _update_sleep_pattern(self, woke_up):
        """Updates the sleep pattern by marking down each minute the guard was
        asleep on his sleep chart.
        """
        td = woke_up - self._falls_asleep
        self._total_asleep += (td.seconds//60) % 60
        for x in range(self._falls_asleep.minute, woke_up.minute):
            self._minutes[x] = self._minutes.get(x, 0) + 1

    def __repr__(self):
        return f'<Guard id={self._id} asleep={self._total_asleep} minutes={self._minutes}>'


class Action(enum.Enum):
    GUARD = 1           # Guard begins shift
    FALLS_ASLEEP = 2    # Guard falls asleep
    WAKES_UP = 3        # Guard wakes up


class Day04(Day):
    """A solution to Day 4: Repose Record"""

    def __init__(self, data):
        super().__init__("Day 4: Repose Record")

        self._data = data
        self._guards = {}
        self._guard = None

    def solve_part_one(self):
        """Solves the first part of the task.

        It records the sleep patterns of all the guards and then finds a guard
        that has slept the most minutes overall. For that guard it finds their
        best minute and returns a product of the guard's ID and their best
        minute.
        """
        for line in self._data:
            self._parse_input_line(line)

        sleep_time = 0
        for guard in self._guards.values():
            if guard.total_asleep > sleep_time:
                self._guard = guard
                sleep_time = guard.total_asleep
        return self._guard.id * self._guard.best_minute

    def solve_part_two(self):
        """Solves the second part of the task.

        Given the sleep patterns, finds a guard that sleeps on his best minute
        the most and returns a product of their ID and that minute.
        """
        times = 0
        for guard in self._guards.values():
            guard_times = guard.get_times_asleep_on_minute(guard.best_minute)
            if guard_times > times:
                self._guard = guard
                times = guard_times
        return self._guard.id * self._guard.best_minute

    def _parse_input_line(self, line):
        """Parses the input line to create a sleep pattern entries."""
        # Record timestamp.
        timestamp = self._get_timestamp(line)
        if timestamp is None:
            raise AssertionError(f'could not parse timestamp: {line}')

        # Record actions.
        action = self._get_action(line)
        if action == Action.GUARD:
            if self._guard is not None:
                self._guards[self._guard.id] = self._guard
            id = self._get_guard_id(line)
            self._guard = self._guards.get(id, Guard(id))
        elif action == Action.FALLS_ASLEEP:
            self._guard.falls_asleep(timestamp)
        elif action == Action.WAKES_UP:
            self._guard.wakes_up(timestamp)

    def _get_timestamp(self, line):
        """Returns timestamp parsed from the log line."""
        match = re.search(r'\[(.+)\](.*)', line)
        if match is not None:
            return match.group(1)
        return None

    def _get_action(self, line):
        """Returns the action from the log line."""
        if re.match(r'(.*)Guard #(\d+) begins shift', line) is not None:
            return Action.GUARD
        if re.match(r'(.*)falls asleep', line):
            return Action.FALLS_ASLEEP
        if re.match(r'(.*)wakes up', line):
            return Action.WAKES_UP
        raise AssertionError(f'unknown action: {line}')

    def _get_guard_id(self, line):
        """Returns the ID of the guard."""
        match = re.search(r'#(\d+)', line)
        if match is not None:
            return int(match.group(1))
        return None

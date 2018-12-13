"""
    Day 7: The Sum of Its Parts
"""

import collections
import re

from days import Day
from utils.file import read_lines_of_datafile


def get_day_07():
    return Day07(
        read_lines_of_datafile('day_07_data.txt')
    )


class Day07(Day):
    """A solution to Day 7: The Sum of Its Parts."""

    def __init__(self, data, worker_count=None, starter_time=None):
        super().__init__('Day 7: The Sum of Its Parts')

        self._tasks = set()
        self._depends = collections.defaultdict(set)
        self._worker_count = worker_count if worker_count is not None else 5
        self._starter_time = starter_time if starter_time is not None else 60

        for line in data:
            first, second = re.findall(r' ([A-Z]) ', line)
            self._tasks |= {first, second}
            self._depends[second].add(first)

    def solve_part_one(self):
        """Solves the first part of the task."""
        finished_tasks = []
        for _ in self._tasks:
            finished_tasks.append(
                self._get_next_available_task(finished_tasks))

        return ''.join(finished_tasks)

    def solve_part_two(self):
        """Solves the second part of the task."""
        remaining_tasks = self._tasks
        finished_tasks = set()
        elapsed = 0
        worker_timers = [0] * self._worker_count
        worker_tasks = [''] * self._worker_count
        while True:
            self._update_timers_for_workers(
                worker_timers, worker_tasks, finished_tasks)
            while 0 in worker_timers:
                worker_id = worker_timers.index(0)
                task = self._find_suitable_task(
                    remaining_tasks, finished_tasks)
                if task is None:
                    break

                self._update_worker_with_new_task(
                    worker_id, remaining_tasks, task, worker_timers, worker_tasks)
            if sum(worker_timers) == 0:
                break
            elapsed += 1
        return elapsed

    def _update_timers_for_workers(self, worker_timers, worker_tasks, finished_tasks):
        """Updates all timers for all workers.

        If a worker has finished a task, that task will be added to finished tasks collection.
        """
        for index, time_left in enumerate(worker_timers):
            # When working for the last second, add the current task to the list
            # of finished tasks.
            if time_left == 1:
                finished_tasks.add(worker_tasks[index])
            # Reduce time left by one.
            worker_timers[index] = max(0, time_left - 1)

    def _update_worker_with_new_task(self, worker_id, remaining_tasks, task, worker_timers, worker_tasks):
        """Updates the status of a worker with the task."""
        remaining_tasks.remove(task)
        worker_timers[worker_id] = self._get_task_timer(task)
        worker_tasks[worker_id] = task

    def _get_next_available_task(self, finished_tasks):
        """Returns next available task from the list of all tasks that are not
        already finished.
        """
        next_available_tasks = []
        for task in self._tasks:
            if task not in finished_tasks and self._depends[task].issubset(set(finished_tasks)):
                next_available_tasks.append(task)
        return min(next_available_tasks)

    def _find_suitable_task(self, tasks, finished_tasks):
        """Finds a suitable task for the worker.

        If there are no suitable tasks or no tasks left at all, ``None`` is returned.
        """
        suitable_tasks = [
            x for x in tasks if self._depends[x].issubset(finished_tasks)]
        if not suitable_tasks:
            return None
        return min(suitable_tasks)

    def _get_task_timer(self, task):
        """Returns the number of seconds needed for the given task."""
        return ord(task) - ord('A') + self._starter_time + 1

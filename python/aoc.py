#!/usr/bin/env python3
"""
    The main script.
"""

import click
import nose
import os
import time
import timeit

from days.d01 import get_day_01
from days.d02 import get_day_02
from days.d03 import get_day_03
from days.d04 import get_day_04
from days.d05 import get_day_05
from days.d06 import get_day_06


# All days solved so far.
DAYS = [
    get_day_01(),
    get_day_02(),
    get_day_03(),
    get_day_04(),
    get_day_05(),
    get_day_06(),
]


timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""


@click.group()
def aoc():
    """Runs the solutions and tests of Advent of Code 2018."""


@aoc.command(name='solve')
@click.argument('day')
def solve(day):
    """Solves the given day."""
    if day == 'all':
        print('Solving all...')
        for d in DAYS:
            _solve_and_print_day(d)
        return
    try:
        d = int(day)
        if d > len(DAYS) or d < 1:
            print('Not solved yet...')
            return
        _solve_and_print_day(DAYS[d-1])
    except ValueError:
        print(f'unknown day: {day}')


@aoc.command(name='test')
def test():
    """Run tests on all days."""
    print('Testing...')
    file_path = os.path.abspath(__file__)
    tests_path = os.path.join(
        os.path.abspath(os.path.dirname(file_path)),
        "tests"
    )
    nose.run(argv=[os.path.abspath(__file__), tests_path])


def _solve_and_print_day(d):
    print(d.title)
    part1 = timeit.Timer(d.solve_part_one).timeit(number=1)
    print(f'\tPart one: {part1[1]} in {part1[0]}s')
    part2 = timeit.Timer(d.solve_part_two).timeit(number=1)
    print(f'\tPart two: {part2[1]} in {part2[0]}s')


if __name__ == '__main__':
    aoc()

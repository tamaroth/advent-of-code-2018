"""
    The main script.
"""

import click
import nose
import os

from days.d01 import get_day_01


# All days solved so far.
DAYS = [
    get_day_01()
]


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
    print(
        '{}:\n\tPart one: {}\n\tPart two: {}\n'.format(
            d.title,
            d.solve_part_one(),
            d.solve_part_two()
        )
    )


if __name__ == '__main__':
    aoc()

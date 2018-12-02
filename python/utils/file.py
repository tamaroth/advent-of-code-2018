"""
    File operations.
"""

import inspect
import os
import sys


def get_real_path_of_datafile(datafile):
    """Returns the real path to the given datafile (relative to the script file)."""
    return os.path.join(
        os.path.join(
            os.path.dirname(  # ./
                os.path.dirname(  # ./python/
                    os.path.dirname(  # ./python/utils/
                        os.path.realpath(__file__)  # ./python/utils/file.py
                    )
                )
            ),
            'inputs/'
        ),
        datafile
    )


def read_lines_from_file(filename):
    """Read lines from the file with the given filename."""
    return [line.rstrip('\n') for line in open(filename)]


def read_lines_of_datafile(datafile):
    """Reads the lines from the datafile located relatively to the script file."""
    return read_lines_from_file(
        get_real_path_of_datafile(datafile)
    )

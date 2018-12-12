# [AdventOfCode2018](http://adventofcode.com/2018/) solutions

## Solution table

| Day | Name                                                                    | C++ | Python |
|:---:|:------------------------------------------------------------------------|:------:|:------:|
| 01  |  Chronal Calibration | :x: | :heavy_check_mark: |
| 02  |  Inventory Management System | :x: | :heavy_check_mark: |
| 03  |  No Matter How You Slice It | :x: | :heavy_check_mark: |
| 04  |  Repose Record | :x: | :heavy_check_mark: |
| 05  |  Alchemical Reduction | :x: | :heavy_check_mark: |
| 06 | Day 6: Chronal Coordinates | :x: | :heavy_check_mark: |

## Building C++
To build the code you will need:
 * [git](https://git-scm.com)
 * [CMake 3.6+](https://cmake.org)
 * [GCC 7.2+](https://gcc.gnu.org/gcc-7/)

Follow the steps:
 * from within terminal, go to a directory you wish to contain the code. (e.g. `cd ~/code`)
 * clone the repo: `git clone https://github.com/tamaroth/advent-of-code-2018.git`
 * enter the repo: `cd advent-of-code-2018`
 * create build directory: `mkdir build`
 * enter build directory: `cd build`
 * run cmake: `cmake ..`
 * run make: `make -j`
 * to run the solutions: `./advent/advent`
 * to run the tests: `./advent/advent tests`

## Running Python code

You will need [Python 3.7](https://www.python.org/downloads/release/python-370/) and then you can simply run:

 * `./setup.sh` to install all necessary packages (on windows just install the missing ones when you run the script).
 * run `./python/aoc.py test` to run tests
 * run `./python/aoc.py solve all` to run all solutions
 * run `./python/aoc.py solve X` to run a solution for the specific day, where `X` is that day's number, e.g. `6`

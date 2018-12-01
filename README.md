# [AdventOfCode2018](http://adventofcode.com/2018/) solutions

## Solution table

| Day | Name                                                                    | C++ | Python |
|:---:|:------------------------------------------------------------------------|:------:|:------:|
| 01  |  Chronal Calibration | :x: | :heavy_check_mark: |


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

 * `python python/aoc.py solve ID` to solve a single day
 * `python python/aoc.py solve all` to solve all days
 * `python python/aoc.py test` to run all tests

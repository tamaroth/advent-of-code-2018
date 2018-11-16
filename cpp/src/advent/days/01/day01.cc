/// @file
///
/// Day 01: Inverse Captcha
///

#include <iostream>
#include <string>
#include <vector>

#include "advent/days/01/day01.hh"
#include "advent/utils/misc.hh"

namespace advent {

// Override.
void Day01::solve_part_one() {
	std::cout << part_one() << solve_for_input("one_input") << std::endl;
}

// Override.
void Day01::solve_part_two() {
	std::cout << part_two() << solve_for_input("one_input", 1) << std::endl;
}

// Override.
std::string Day01::part_one() const {
	return __COMPACT_PRETTY_FUNCTION__;
}

// Override.
std::string Day01::part_two() const {
	return __COMPACT_PRETTY_FUNCTION__;
}

///
/// The method returns sum all values of digits in input that have that same
/// value as `distance` distant character while treating input as a circular
/// buffer.
///
int Day01::solve_for_input(const std::string& input, int distance) {
	int sum = 0;
	int length = input.length();
	for (int i = 0; i < length; ++i) {
		if (input[i] == input[(i + distance) % length]) {
			sum += (input[i] - '0');
		}
	}

	return sum;
}

}  // namespace advent

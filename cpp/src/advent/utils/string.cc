/// @file
///
/// String utilities.
///

#include <regex>

#include "advent/utils/string.hh"

namespace advent {

std::vector<std::string> split(const std::string& input, const std::string regex) {
	std::regex re(regex);
	std::sregex_token_iterator first{input.begin(), input.end(), re, -1}, last;
	return {first, last};
}

}  // namespace advent

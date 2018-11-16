/// @file
///
/// String utilities.
///

#include <string>
#include <type_traits>
#include <vector>

namespace advent {

/// @name String to Type conversion.
/// @{

///
/// Converts from a string to a type.
///
/// @tparam T Type to convert to
/// @param input String to convert from
/// @result converted value
///
/// For now supported convertion types:
///  - @a int
///  - @a std::string (no convertion)
///
template <typename T>
T convert_to(const std::string& input) {
	static_assert(std::is_same<T, int>::value || std::is_same<T, std::string>::value,
				  "unsupported convertion type");
	if constexpr (std::is_same<T, int>::value) {
		return std::stoi(input);
	} else {
		return input;
	}
}
/// @}

/// @name String splitting.
/// @{
std::vector<std::string> split(const std::string& input, const std::string regex = " ");

///
/// Splits a string by a delimiter into a vector.
///
template <typename T>
std::vector<T> split_to(const std::string& input, const std::string delimiter = " ") {
	auto split_string = split(input, delimiter);
	std::vector<T> result;
	for (const auto& element : split_string) {
		result.push_back(convert_to<T>(element));
	}
	return result;
}
/// @}

}  // namespace advent

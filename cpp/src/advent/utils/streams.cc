/// @file
///
/// Streams utilities.
///

#include "advent/utils/streams.hh"

namespace advent {

std::ostream& operator<<(std::ostream& os, const Matrix& mx) {
	os << "{" << std::endl;
	for (const auto& row : mx) {
		os << "    { ";
		for (const auto& element : row) {
			os << element << ", ";
		}
		os << "}," << std::endl;
	}
	os << "}" << std::endl;
	return os;
}

std::ostream& print_one(std::ostream& os) {
	return os;
}

std::mutex& get_cout_mutex() {
	static std::mutex m;
	return m;
}
}  // namespace advent

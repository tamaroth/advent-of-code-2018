/// @file
///
/// File utilities.
///

#include "advent/utils/file.hh"

namespace advent {

///
/// Reads a single line from a file with the given file name.
///
std::optional<std::string> read_line_from_file(const std::string& file_name) {
	std::string line;
	std::ifstream file_stream(file_name);

	if (!file_stream.is_open()) {
		std::cerr << "Could not find input file " << file_name
				  << ". Make sure it's located in current directory." << std::endl;
		return std::nullopt;
	}

	std::getline(file_stream, line);
	return line;
}

}  // namespace advent

/// @file
///
/// File utilities.
///

#pragma once

#include <fstream>
#include <iostream>
#include <optional>
#include <vector>

#include "advent/utils/string.hh"

namespace advent {

template <typename LineT = std::string>
using Lines = std::vector<LineT>;

///
/// Read lines from a text file and stores then in a vector.
///
/// @tparam T Type of value stored in a single line.
/// @param file_name The Name of the file to be read.
/// @return A vector of type T containing values read from the given file.
///
template <typename T = std::string>
std::vector<T> read_lines_from_file(const std::string& file_name) {
	std::vector<T> lines;
	std::ifstream file_stream(file_name);
	if (!file_stream.is_open()) {
		std::cerr << "Could not find input file " << file_name
				  << ". Make sure it's located in current directory." << std::endl;
		return lines;
	}
	std::string line;
	while (std::getline(file_stream, line)) {
		lines.push_back(convert_to<T>(line));
	}

	return lines;
}

std::optional<std::string> read_line_from_file(const std::string& file_name);
/// @}

}  // namespace advent

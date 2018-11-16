/// @file
///
/// Stream utilities.
///

#pragma once

#include <deque>
#include <iostream>
#include <mutex>
#include <vector>

#include "advent/utils/types.hh"

namespace advent {

/// @name Streaming.
/// @{
std::ostream& operator<<(std::ostream& os, const Matrix& mx);

///
/// Streams vector of objects to ostream.
///
/// @tparam T The type of vector to stream.
///
template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T> vec) {
	os << "{ ";
	for (const auto& element : vec) {
		os << element << ", ";
	}
	os << "}";
	return os;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::deque<T> que) {
	os << "{ ";
	for (const auto& element : que) {
		os << element << ", ";
	}
	os << "}";
	return os;
}

std::mutex& get_cout_mutex();
std::ostream& print_one(std::ostream& os);

template <class A0, class... Args>
std::ostream& print_one(std::ostream& os, const A0& a0, const Args&... args) {
	os << a0;
	return print_one(os, args...);
}

template <class... Args>
std::ostream& print(std::ostream& os, const Args&... args) {
	return print_one(os, args...);
}

template <class... Args>
std::ostream& print(const Args&... args) {
	std::lock_guard<std::mutex> lock(get_cout_mutex());
	return print(std::cout, args...);
}
/// @}

}  // namespace advent

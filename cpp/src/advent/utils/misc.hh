/// @file
///
/// Miscellaneous functions and macros.
///

#pragma once

#include <string>
#include <type_traits>

namespace advent {

/// @name Decorative method names
/// @{
std::string method_name(const std::string& function, const std::string& pretty_function);
#define __COMPACT_PRETTY_FUNCTION__ method_name(__FUNCTION__, __PRETTY_FUNCTION__)
/// @}

}  // namespace advent

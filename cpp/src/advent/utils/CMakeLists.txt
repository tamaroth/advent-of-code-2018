##
## CMake configuration file for utilities.
##

set(UTILS_SOURCES
	base.cc
	file.cc
	misc.cc
	solutions.cc
	streams.cc
	string.cc
)
add_library(utils SHARED ${UTILS_SOURCES})
target_include_directories(utils PUBLIC ${SRC_DIR})
target_link_libraries(utils PUBLIC boost)

##
## CMake configuration for the source files.
##

set(DAYS_SOURCES
	01/day01.cc
)

add_library(days SHARED ${DAYS_SOURCES})
target_include_directories(days PUBLIC ${SRC_DIR})
target_link_libraries(days PUBLIC
	boost
	fmt
)

##
## Copy input files for certain days
##

## Day 01 input
add_custom_command(TARGET days POST_BUILD
	COMMAND ${CMAKE_COMMAND} -E copy
		${SRC_DIR}/advent/days/01/day_01_input.txt ${PROJECT_BINARY_DIR})

##
## CMake configuration file for tests.
##

include(gtest)

set(TESTS_SOURCES
	main.cc
	day_01_tests.cc
)

add_executable(tests ${TESTS_SOURCES})
target_include_directories(tests PUBLIC "${PROJECT_SOURCE_DIR}")
target_link_libraries(tests PUBLIC
	utils
	days
	gtest
)
install(TARGETS tests DESTINATION "${INSTALL_BIN_DIR}/tests")

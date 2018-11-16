/// @file
///
/// All solutions.
///

#include "advent/utils/solutions.hh"
#include "advent/utils/assert.hh"
#include "advent/utils/base.hh"
#include "advent/utils/container.hh"

namespace advent {

Solutions::Solutions() = default;
Solutions::~Solutions() = default;

// Copying is allowed.
Solutions::Solutions(const Solutions&) = default;
Solutions& Solutions::operator=(const Solutions&) = default;

// Moving is allowed.
Solutions::Solutions(Solutions&&) = default;
Solutions& Solutions::operator=(Solutions&&) = default;

///
/// Get a pointer to the given task. If the given task does not exist
/// in the cache create new one and store it in cache.
///
std::shared_ptr<Task> Solutions::get_task(TaskID task) {
	if (contains(solutions, task)) {
		return solutions[task];
	}

	switch (task) {
		default:
			ABORT("unknown task");
	}

	return solutions[task];
}

}  // namespace advent

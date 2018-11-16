/// @file
///
/// Day 01: Inverse Captcha
///

#include <string>

#include "advent/utils/base.hh"

namespace advent {

class Day01 : public Task {
   public:
	Day01() = default;
	~Day01() override = default;

	virtual void solve_part_one() override;
	virtual void solve_part_two() override;

	virtual std::string part_one() const override;
	virtual std::string part_two() const override;

   protected:
	int solve_for_input(const std::string& input, int distance = 1);
};

}  // namespace advent


#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;

class Solution {
public:
	int numberOfArithmeticSlices(vector<int>& nums) {
		if (nums.size() < 3)
		{
			return 0;
		}
		int slow = 0;
		int fast = 1;
		int ans = 0;
		int cur_dif = nums[1] - nums[0];
		while (fast + 1 <= nums.size() - 1)
		{
			fast++;
			if (nums[fast] - nums[fast - 1] == cur_dif)
			{

			}
			else
			{
				if (fast + 2 > nums.size() - 1)
				{
					if (nums[fast]-nums[fast-1]==cur_dif)
					{
						ans += sum_helper(fast, slow);

					}
					
					break;
				}
				else
				{
					ans += sum_helper(fast, slow);
					slow = fast;
					fast++;
					cur_dif = nums[fast] - nums[slow];
				}
			}
		}
		fast++;
		if (fast-slow==2)
		{

		}
		else
		{
			ans += sum_helper(fast, slow);

		}
		
		return ans;


	}

	int sum_helper(int fast, int slow) {
		int ans = 0;
		if (fast-slow<=3)
		{
			return 0;
		}
		for (size_t i = 0; i <= fast - slow - 3; i++)
		{
			ans += (i + 1);
		}
		return ans;


	}
};
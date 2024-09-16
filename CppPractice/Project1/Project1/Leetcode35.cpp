#include <string>

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
    int searchInsert(vector<int>& nums, int target) {
		int ans = 0;
		for (int i = 0; i < nums.size(); i++)
		{
			if (nums[i]>=target)
			{
				return i;
			}

		}
		return nums.size();

    }
};
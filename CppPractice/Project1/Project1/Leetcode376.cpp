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
	int wiggleMaxLength(vector<int>& nums) {
		int pre_dif = 0;
		int cur_dif = 0;
		int anchor_begin = 0;
		int anchor_end = 0;
		int ans = 1;
		if (nums.size() < 2)
		{
			return nums.size();
		}
		anchor_begin = nums[0];
		for (int i = 1; i < nums.size(); i++)
		{
			anchor_end = nums[i];
			if (anchor_begin == anchor_end)
			{

			}
			else
			{
				if (ans == 1)
				{
					ans++;
					pre_dif = anchor_end - anchor_begin;
					anchor_begin = nums[i];
				}
				else
				{
					cur_dif = anchor_end - anchor_begin;
					if (cur_dif * pre_dif < 0)
					{
						ans++;
						anchor_begin = nums[i];
						pre_dif = cur_dif;
					}
					else
					{
						anchor_begin = nums[i];

					}
				}
			}
		}
		return ans;
	}
};
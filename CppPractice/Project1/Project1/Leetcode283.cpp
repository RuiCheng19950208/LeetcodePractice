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
    void moveZeroes(vector<int>& nums) {
		int record = 0;
		for (int i = 0; i < nums.size(); i++)
		{
			if (nums[i]!=0)
			{
				nums[record] = nums[i];
				record++;
			}
		}
		for (int i = record; i < nums.size(); i++)
		{
			nums[i] = 0;

		}
		

    }
};
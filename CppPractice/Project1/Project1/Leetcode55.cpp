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
    bool canJump(vector<int>& nums) {
        int next_max = 0;
        int cur_max = 0;
        int cur = 0;
        int step = 0;
        if (nums.size() == 1)
        {
            return 0;

        }

        while (cur <= next_max)
        {

            if (cur > cur_max)
            {
                step++;
                cur_max = next_max;

            }
            next_max = max(next_max, nums[cur] + cur);
            if (next_max >= nums.size() - 1)
            {
                return true;
            }
            cur++;
        }
        return false;

    }
};

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
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        for (int i = 0; i < nums.size(); i++)
        {
            if (i==0)
            {
                dp[i] = nums[0];

            }
            else if (i==1)
            {
                dp[i] = max(dp[0], nums[i]);

            }
            else
            {
                dp[i] = max(dp[i-2]+nums[i], dp[i-1]);

            }

        }


        return dp.back();

    }
};